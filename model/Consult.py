class Consult:
    def __init__(self, variants, rules):
        self.__active_rules = []
        self.__vars_with_values = {}

        self.__rules = rules
        self.__variants = variants

    @property
    def active_rules(self):
        return self.__active_rules

    @property
    def vars_with_values(self):
        return self.__vars_with_values

    @property
    def rules(self):
        return self.__rules

    @property
    def variants(self):
        return self.__variants

    def add_active_rule(self, rule):
        self.__active_rules.append(rule)

    def add_var_with_value(self, var, value):
        self.__vars_with_values[var] = value

    def clear_active_rules(self):
        self.__active_rules = []

    def clear_vars_with_values(self):
        self.__vars_with_values = {}

    def clear(self):
        self.__active_rules = []
        self.__vars_with_values = {}
