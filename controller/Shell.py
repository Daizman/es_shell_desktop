from view.Shell import Shell as ShellView

from utils.ControllerErrorHandler import *


class Shell:
    def __init__(self, model):
        self.__model = model
        self.__view = ShellView(self)

    def show(self):
        self.__view.show()

    def get_domains(self):
        return self.__model.domains

    def get_variants(self):
        return self.__model.variants

    def get_rules(self):
        return self.__model.rules

    def get_name(self):
        return self.__model.name

    @controller_setter
    def set_name(self, new_name):
        self.__model.name = new_name

    @controller_setter
    def set_domains(self, domains):
        self.__model.domains = domains

    @controller_setter
    def set_variants(self, variants):
        self.__model.variants = variants

    @controller_setter
    def set_rules(self, rules):
        self.__model.rules = rules

    @controller_setter
    def load(self, f_name):
        self.__model.load(f_name)

    def backup(self, f_name):
        self.__model.backup(f_name)

    def clear_shell(self):
        self.__model.clear()

    @controller_setter
    def add_domain(self, domain):
        self.__model.add_domain(domain.name, domain.values)

    @controller_setter
    def add_var(self, var):
        self.__model.add_var(var.name, var.domain, var.question, var.var_type)

    @controller_setter
    def add_rule(self, rule):
        self.__model.add_rule(rule.name, rule.description, rule.reasons, rule.conclusion)
