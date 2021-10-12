import logging

from typing import Dict, List

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from tg_view.env_constants import *

from model.Consult import Consult as ConsultModel
from model.Var import *

from model.Shell import Shell as ShellModel


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

shell = ShellModel()
shell.load(ES_PATH)
consult_model = ConsultModel(shell.variants, shell.rules)
goals = {cur_var.name: cur_var for cur_var in filter(lambda var: var.can_be_goal, shell.variants)}
goal = None
current_ask_var = None

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)


def gen_reply_keyboard(options: List[str]) -> List[List[str]]:
    reply_keyboard = []
    option_in_row_count = 3 if len(options) % 3 == 0 else 2
    row = []
    for opt_number, option in enumerate(options):
        row.append(option)
        if opt_number % option_in_row_count == 0:
            reply_keyboard.append(row[:])
            row = []
    reply_keyboard[-1].append('Выйти')

    return reply_keyboard


def create_reply_keyboard_markup(reply_keyboard):
    return ReplyKeyboardMarkup(reply_keyboard)


def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f'{key} - {value}' for key, value in user_data.items()]
    return "\n".join(facts).join(['\n', '\n'])


def start(update: Update, context: CallbackContext) -> int:
    markup = create_reply_keyboard_markup(gen_reply_keyboard(list(goals.keys())))

    update.message.reply_text(
        'Привет, я бот созданный для консультации по вопросам, связанным '
        'с поиском ТЗ, инструкций и других документов.'
        'Выбери пожалуйста тему консультации.',
        reply_markup=markup,
    )

    return CHOOSING


def regular_choice(update: Update, context: CallbackContext) -> int:
    """Ask the user for info about the selected predefined choice."""
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(f'Your {text.lower()}? Yes, I would love to hear about that!')

    return TYPING_REPLY


def custom_choice(update: Update, context: CallbackContext) -> int:
    """Ask the user for a description of a custom category."""
    update.message.reply_text(
        'Alright, please send me the category first, for example "Most impressive skill"'
    )

    return TYPING_CHOICE


def do_consult(var: Var, update: Update) -> str:
    global current_ask_var
    goal_value = ''
    for rule_ind, rule in enumerate(shell.rules):
        follow_rule = True
        var_val = ''
        conclusion_has_var = any(
            conclusion.var.name == var.name
            and rule not in consult_model.active_rules
            for conclusion in rule.conclusions
        )

        if conclusion_has_var and rule not in consult_model.active_rules:
            for reason in rule.reasons:
                if follow_rule:
                    if reason.var in consult_model.vars_with_values.keys():
                        var_val = consult_model.vars_with_values[reason.var]
                        if var_val != reason.value:
                            follow_rule = False
                    else:
                        var_to_ask = reason.var
                        if var_to_ask.var_type == VarType.REQUESTED:
                            markup = create_reply_keyboard_markup(gen_reply_keyboard(var_to_ask.domain.values))

                            update.message.reply_text(
                                var_to_ask.question,
                                reply_markup=markup,
                            )
                            var_value = await ask_var(var_to_ask, message)
                            if not var_value:
                                return ''
                            consult_model.add_var_with_value(var_to_ask, var_value)
                            if var_value != reason.value:
                                follow_rule = False
                        elif var_to_ask.var_type == VarType.OUTPUT_REQUESTED:
                            try_goal = do_consult(var_to_ask, message)
                            if try_goal == '':
                                var_value = await ask_var(var_to_ask, message)
                                if not var_value:
                                    return ''
                                consult_model.add_var_with_value(var_to_ask, var_value)
                                if var_value != reason.value:
                                    follow_rule = False
                            elif not try_goal:
                                return ''
                            else:
                                var_value = consult_model.vars_with_values[var_to_ask]
                                if var_value != reason.value:
                                    follow_rule = False
                        else:
                            try_goal = do_consult(var_to_ask, message)
                            if try_goal == '':
                                follow_rule = False
                            elif not try_goal:
                                return ''
                            else:
                                var_value = consult_model.vars_with_values[var_to_ask]
                                if var_value != reason.value:
                                    follow_rule = False
            if follow_rule:
                for fact in rule.conclusions:
                    if fact.var not in consult_model.vars_with_values.keys():
                        var_val = fact.value
                        consult_model.add_var_with_value(fact.var, fact.value)
                goal_value = var_val
                consult_model.add_active_rule(rule)
                break
        if goal_value != '':
            break

    return goal_value


def received_information(update: Update, context: CallbackContext) -> int:
    """Store info provided by user and ask for the next category."""
    text = update.message.text
    global goal
    if goal is None:
        goal = goals[text]
        consult_model.clear()
        do_consult(goal, update)
    else:
        pass

    return CHOOSING


def done(update: Update, context: CallbackContext) -> int:
    """Display the gathered info and end the conversation."""
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text(
        'Выход из консультации',
        reply_markup=ReplyKeyboardRemove(),
    )

    user_data.clear()
    global goal
    consult_model.clear()
    goal = None

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            CommandHandler('consult', start)
        ],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(Age|Favourite colour|Number of siblings)$'), regular_choice
                ),
                MessageHandler(Filters.regex('^Something else...$'), custom_choice),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Выйти$')), regular_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Выйти$')),
                    received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Выйти$'), done)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
