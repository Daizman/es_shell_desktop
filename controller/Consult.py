from model.types.VarType import VarType


class Consult:
    def __init__(self, model, view_class, parent=None):
        self.__model = model
        self.__view = view_class(self, parent)

    def show(self):
        self.__view.show()

    def get_vars(self):
        return self.__model.variants

    def consult(self, goal):
        self.__model.clear()
        return self.take_goal(goal)

    def take_goal(self, var):
        goal_value = ''
        for rule in self.__model.rules:
            follow_rule = True
            var_val = ''
            conclusion_has_var = any(
                conclusion.var.name == var.name
                and rule not in self.__model.active_rules
                for conclusion in rule.conclusions
            )

            if conclusion_has_var and rule not in self.__model.active_rules:
                for reason in rule.reasons:
                    if follow_rule:
                        if reason.var in self.__model.vars_with_values.keys():
                            var_val = self.__model.vars_with_values[reason.var]
                            if var_val != reason.value:
                                follow_rule = False
                        else:
                            var_to_ask = reason.var
                            if var_to_ask.var_type == VarType.REQUESTED:
                                var_value = self.ask_var(var_to_ask)
                                if not var_value:
                                    return self.reject_consult()
                                self.__model.add_var_with_value(var_to_ask, var_value)
                                if var_value != reason.value:
                                    follow_rule = False
                            elif var_to_ask.var_type == VarType.OUTPUT_REQUESTED:
                                try_goal = self.take_goal(var_to_ask)
                                if try_goal == '':
                                    var_value = self.ask_var(var_to_ask)
                                    if not var_value:
                                        return self.reject_consult()
                                    self.__model.add_var_with_value(var_to_ask, var_value)
                                    if var_value != reason.value:
                                        follow_rule = False
                                elif not try_goal:
                                    return False
                                else:
                                    var_value = self.__model.vars_with_values[var_to_ask]
                                    if var_value != reason.value:
                                        follow_rule = False
                            else:
                                try_goal = self.take_goal(var_to_ask)
                                if try_goal == '':
                                    follow_rule = False
                                elif not try_goal:
                                    return False
                                else:
                                    var_value = self.__model.vars_with_values[var_to_ask]
                                    if var_value != reason.value:
                                        follow_rule = False
                if follow_rule:
                    for fact in rule.conclusions:
                        if fact.var not in self.__model.vars_with_values.keys():
                            var_val = fact.value
                            self.__model.add_var_with_value(fact.var, fact.value)
                    goal_value = var_val
                    self.__model.add_active_rule(rule)
                    break
            if goal_value != '':
                break

        return goal_value

    def reject_consult(self):
        self.__view.show_error('Ошибка при получении значения запрашиваемой переменной')
        self.__view.reject()
        return False

    def ask_var(self, var_to_ask):
        return self.__view.ask_var(var_to_ask)
