import telebot
import telebot.types as types
from typing import List

from functools import partial

import tg_view.env_constants as env_constants

from model.Consult import Consult as ConsultModel

from model.Shell import Shell as ShellModel
from model.types.VarType import *


def log(func):
    def wrapper(*args):
        print()
        print(f'called_func: {str(func)}')
        print('args:', ' '.join([str(arg) for arg in args]))
        val = func(*args)
        return val
    return wrapper


bot = telebot.TeleBot(env_constants.API_TOKEN)
shell = ShellModel()
shell.load(env_constants.ES_PATH)
consult_model = ConsultModel(shell.variants, shell.rules)
goals = {cur_var.name: cur_var for cur_var in filter(lambda var: var.can_be_goal, shell.variants)}
goal = None


def gen_reply_keyboard(options: List[str]) -> List[str]:
    reply_keyboard = [
        option
        for option in options
    ]

    reply_keyboard.append('Выйти')

    return reply_keyboard


def create_reply_keyboard_markup(reply_keyboard) -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for key in reply_keyboard:
        markup.add(key)
    return markup


@bot.message_handler(commands=['start'])
def start(message: types.Message) -> None:
    follow_rule = True
    global goal
    markup = create_reply_keyboard_markup(gen_reply_keyboard(list(goals.keys())))

    message = bot.send_message(
        message.chat.id,
        text='Выбери пожалуйста тему консультации.',
        reply_markup=markup
    )
    bot.register_next_step_handler(message, partial(consult_step, follow_rule, goal, None))


@log
def consult_step(follow_rule, var, reason, message):
    print('consult_step')
    print()
    if message.text == 'Выйти':
        exit_consult(message)
        return ''
    global goal
    if not goal:
        goal = goals[message.text]
        var = goal
    if var and var != goal and message.text in var.domain.values:
        consult_model.add_var_with_value(var, message.text)
        if message.text != reason.value:
            follow_rule = False
    goal_value = ''
    for rule_ind, rule in enumerate(shell.rules):
        var_val = ''

        if consult_model.check_conclusion(var, rule):
            for reason in rule.reasons:
                if follow_rule:
                    if consult_model.var_is_assigned(reason.var):
                        var_val = consult_model.vars_with_values[reason.var]
                        if var_val != reason.value:
                            follow_rule = False
                    else:
                        var_to_ask = reason.var
                        if var_to_ask.var_type == VarType.REQUESTED:
                            markup = create_reply_keyboard_markup(gen_reply_keyboard(var_to_ask.domain.values))
                            message = bot.send_message(
                                message.chat.id,
                                var_to_ask.question,
                                reply_markup=markup
                            )
                            bot.register_next_step_handler(message, partial(consult_step, follow_rule, var, reason))
                        elif var_to_ask.var_type == VarType.OUTPUT_REQUESTED:
                            try_goal = consult_step(follow_rule, var_to_ask, reason, message)
                            if try_goal == '':
                                markup = create_reply_keyboard_markup(gen_reply_keyboard(var_to_ask.domain.values))
                                message = bot.send_message(
                                    message.chat.id,
                                    var_to_ask.question,
                                    reply_markup=markup
                                )
                                bot.register_next_step_handler(message, partial(consult_step, follow_rule, var, reason))
                            elif not try_goal:
                                return False
                            else:
                                var_value = consult_model.vars_with_values[var_to_ask]
                                if var_value != reason.value:
                                    follow_rule = False
                        else:
                            try_goal = consult_step(follow_rule, var_to_ask, reason, message)
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

    if goal_value in goal.domain.values:
        bot.send_message(
            message.chat.id,
            f'Результат консультации: {goal_value}'
        )
        print(f'__RESULT__{goal_value}')

    return goal_value


def exit_consult(message: types.Message) -> None:
    global goal
    goal = None
    consult_model.clear()
    bot.send_message(message.chat.id, 'Выход из консультации.')


@bot.message_handler(commands=['help'])
def print_help(message: types.Message) -> None:
    bot.send_message(message.chat.id, 'Команда для начала консультации /start.')


bot.polling(non_stop=True, interval=1)
