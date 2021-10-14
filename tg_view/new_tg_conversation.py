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


def print_enter(func):
    def wrapper(*args):
        print(f'enter in function: {str(func).split()[1]}')
        print()
        val = func(*args)
        return val
    return wrapper


bot = telebot.TeleBot(env_constants.API_TOKEN)
shell = ShellModel()
shell.load(env_constants.ES_PATH)
consult_model = ConsultModel(shell.variants, shell.rules)
goals = {cur_var.name: cur_var for cur_var in filter(lambda var: var.can_be_goal, shell.variants)}
goal = None
i_asked_var = False
i_answered = False


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
    clear_all()
    markup = create_reply_keyboard_markup(gen_reply_keyboard(list(goals.keys())))
    message = bot.send_message(
        message.chat.id,
        text='Выбери пожалуйста тему консультации.',
        reply_markup=markup
    )
    bot.register_next_step_handler(message, partial(consult))


@print_enter
def consult(message) -> None:
    global goal
    if message.text == 'Выйти':
        exit_consult(message)
        return
    goal = goals[message.text]
    con_step(goal, message)


@print_enter
def con_step(c_goal, message):
    if not consult_model.check_var_can_be_reached(c_goal):
        return False
    if consult_model.check_var_is_assigned(c_goal):
        return True
    for rule in shell.rules:
        if consult_model.check_conclusion(c_goal, rule):
            check_rule(True, rule, None, 0, message)


@print_enter
def check_rule(follow_rule, rule, var_to_assign, cur_step, message) -> bool:
    global i_asked_var, goal, che

    if i_answered:
        return follow_rule

    if message.text == 'Выйти':
        exit_consult(message)
        return follow_rule

    check_goal(message)

    if var_to_assign is not None:
        if message.text in var_to_assign.domain.values:
            consult_model.add_var_with_value(var_to_assign, message.text)
            i_asked_var = False
            con_step(goal, message)
        return follow_rule

    if not follow_rule or i_asked_var:
        return follow_rule
    for step in range(cur_step, len(rule.reasons)):
        if consult_model.check_var_is_assigned(rule.reasons[step].var):
            if rule.reasons[step].value != consult_model.vars_with_values[rule.reasons[step].var]:
                follow_rule = False
        else:
            var = rule.reasons[step].var
            if var.var_type == VarType.REQUESTED:
                if not i_asked_var:
                    i_asked_var = True
                    ask_var(var, message, follow_rule, rule, step)
                break
            if var.var_type == VarType.INFERRED:
                con_step(var, message)
                break
            if not con_step(var, message):
                if not i_asked_var:
                    i_asked_var = True
                    ask_var(var, message, follow_rule, rule, step)
                break

    return follow_rule


@print_enter
def ask_var(var, message, follow_rule, rule, step) -> None:
    markup = create_reply_keyboard_markup(gen_reply_keyboard(var.domain.values))
    message = bot.send_message(
        message.chat.id,
        var.question,
        reply_markup=markup
    )
    bot.register_next_step_handler(message, partial(check_rule, follow_rule, rule, var, step))


def check_goal(message):
    global goal, i_answered
    if goal and consult_model.var_can_be_assigned_by_rule(goal):
        i_answered = True
        bot.send_message(
            message.chat.id,
            f'Результат консультации: {consult_model.vars_with_values[goal]}'
        )


def clear_all():
    global i_asked_var, i_answered, goal
    goal = None
    i_asked_var = False
    i_answered = False
    consult_model.clear()


def exit_consult(message: types.Message) -> None:
    clear_all()
    bot.send_message(message.chat.id, 'Выход из консультации.')


@bot.message_handler(commands=['help'])
def print_help(message: types.Message) -> None:
    bot.send_message(message.chat.id, 'Команда для начала консультации /start.')


bot.polling(non_stop=True, interval=1)
