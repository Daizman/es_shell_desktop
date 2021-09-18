import model.Shell as ShellModel


class Shell:
    def __init__(self, name):
        self.__model = ShellModel.Shell(name)

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
