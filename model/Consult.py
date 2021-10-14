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

    def check_var_is_assigned(self, var):
        return var in self.__vars_with_values.keys()

    def check_conclusion(self, var, rule):
        return any(
            conclusion.var.name == var.name
            and rule not in self.active_rules
            for conclusion in rule.conclusions
        )

    def pass_the_rule(self, rule):
        for reason in rule.reasons:
            if not self.check_var_is_assigned(reason.var) or reason.value != self.vars_with_values[reason.var]:
                return False
        for conclusion in rule.conclusions:
            self.add_var_with_value(conclusion.var, conclusion.value)
        self.active_rules.append(rule)
        return True

    def var_can_be_assigned_by_rule(self, var):
        conclusions_with_var = set(
            filter(
                lambda rul: any(var == conclusion.var for conclusion in rul.conclusions),
                self.rules
            )
        )
        return any(self.pass_the_rule(rule) for rule in conclusions_with_var)

    def check_var_can_be_reached(self, var) -> bool:
        conclusions_with_var = set(
            filter(
                lambda rul: any(var == conclusion.var for conclusion in rul.conclusions),
                self.rules
            )
        )
        for rule in conclusions_with_var:
            if self.pass_the_rule(rule):
                return True

        rules_reasons = [rule.reasons for rule in conclusions_with_var]
        unique_vars = set()
        for rule_reasons in rules_reasons:
            for reason in rule_reasons:
                unique_vars.add(reason.var)
        return any(not self.check_var_is_assigned(variable) for variable in unique_vars)
