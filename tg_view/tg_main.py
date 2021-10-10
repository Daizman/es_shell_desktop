import telebot
import telebot.types as telebot_types
from telegram.ext.dispatcher import run_async


import tg_view.env_constants as env_constants

from model.Consult import Consult as ConsultModel

from model.Shell import Shell as ShellModel
from model.types.VarType import *


bot = telebot.TeleBot(env_constants.API_TOKEN)
shell = ShellModel()
shell.load(env_constants.ES_PATH)
consult_model = ConsultModel(shell.vars, shell.rules)
goals = list(filter(lambda var: var.can_be_goal, shell.vars))
goal = None


def print_help(message):
    bot.send_message(message.chat.id,
                     'Привет, я бот созданный для консультации по вопросам, связанным '
                     'с поиском ТЗ, инструкций и других документов. Задай мне вопрос, '
                     'в котором укажи кто ты (разработчик/аналитик/тестировщик/оператор), '
                     'и что ты ищешь, а дальше я постараюсь найти нужную тебе статью или '
                     'задам уточняющие вопросы.')


def print_error(message):
    bot.send_message(message.chat.id, text='Не удалось распознать команду')


async def ask_var(var, message):
    keyboard = telebot_types.InlineKeyboardMarkup()
    for value in var.domain.values:
        key = telebot_types.InlineKeyboardButton(text=value, callback_data=value)
        keyboard.add(key)

    key = telebot_types.InlineKeyboardButton(text='Выйти', callback_data='Выйти')
    keyboard.add(key)

    bot.send_message(message.chat.id, text=var.question, reply_markup=keyboard)
    return await handle_callback_query()


def start_consult(message):
    keyboard = telebot_types.InlineKeyboardMarkup()
    for _goal in goals:
        key = telebot_types.InlineKeyboardButton(text=_goal.name, callback_data=_goal.name)
        keyboard.add(key)

    key = telebot_types.InlineKeyboardButton(text='Выйти', callback_data='Выйти')
    keyboard.add(key)

    bot.send_message(message.chat.id, text='Выберите цель консультации:', reply_markup=keyboard)


async def do_consult(var, message):
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
                            var_value = await ask_var(var_to_ask, message)
                            if not var_value:
                                return exit_consult(message)
                            consult_model.add_var_with_value(var_to_ask, var_value)
                            if var_value != reason.value:
                                follow_rule = False
                        elif var_to_ask.var_type == VarType.OUTPUT_REQUESTED:
                            try_goal = do_consult(var_to_ask, message)
                            if try_goal == '':
                                var_value = await ask_var(var_to_ask, message)
                                if not var_value:
                                    return exit_consult(message)
                                consult_model.add_var_with_value(var_to_ask, var_value)
                                if var_value != reason.value:
                                    follow_rule = False
                            elif not try_goal:
                                return False
                            else:
                                var_value = consult_model.vars_with_values[var_to_ask]
                                if var_value != reason.value:
                                    follow_rule = False
                        else:
                            try_goal = do_consult(var_to_ask, message)
                            if try_goal == '':
                                follow_rule = False
                            elif not try_goal:
                                return False
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


def exit_consult(message):
    global goal
    bot.send_message(message.chat.id, text='Выход из консультации')
    consult_model.clear()
    goal = None
    return False


@bot.callback_query_handler(func=lambda call: True)
async def handle_callback_query(call):
    global goal
    if call.data == 'Выйти':
        return exit_consult(call.message)
    if goal is not None:
        return call.data
    goal = shell.get_var_by_name(call.data)
    bot.send_message(call.message.chat.id, text=f'Начало консультации по теме:{goal.name}')
    consult_model.clear()
    await do_consult(goal, call.message)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    text = message.text.strip().lower().replace('/', '')
    if text in default_handlers:
        default_handlers[text](message)
    else:
        print_error(message)


default_handlers = {
    'help': print_help,
    'hello': print_help,
    'привет': print_help,
    'start': start_consult,
    'консультация': start_consult
}

bot.polling(non_stop=True, interval=1)
