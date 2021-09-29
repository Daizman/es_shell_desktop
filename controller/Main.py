import view.Main as ShellView


class Shell:
    def __init__(self, model):
        self.__model = model
        self.__view = ShellView.Shell(self, self.__model)

        self.__view.show()

    def get_name(self):
        return self.__model.name

    def consult(self):
        pass

    def load(self, path):
        if not path or not path.strip():
            raise ValueError('Не найден файл с БЗ')
        self.__model.load(path)

    def backup(self, path):
        if not path or not path.strip():
            raise ValueError('Не указан файл для бекапа')
        self.__model.backup(path)

    def get_goals(self):
        return list(filter(lambda el: el.may_be_goal, self.__model.vars))

    def take_goal(self):
        pass

    def ask_question(self):
        pass

    def swap_rules(self, pos_from, pos_to):
        self.__model.swap_rules(pos_from, pos_to)

    def remove_domain(self, name):
        self.__model.remove_domain(name)

    def remove_var(self, name):
        self.__model.remove_var(name)

    def remove_rule(self, name):
        self.__model.remove_rule(name)

    def get_domain_by_name(self, name):
        self.__model.get_domain_by_name(name)

    def get_var_by_name(self, name):
        self.__model.get_var_by_name(name)

    def get_rule_by_name(self, name):
        self.__model.get_rule_by_name(name)
