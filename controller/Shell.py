import view.Shell as ShellView


class Shell:
    def __init__(self, model):
        self.model = model
        self.view = ShellView.Shell(self, self.model)

        self.view.show()

    def get_name(self):
        return self.model.name

    def consult(self):
        pass

    def load(self, path):
        if not path or not path.strip():
            raise ValueError('Не найден файл с БЗ')
        self.model.load(path)

    def backup(self, path):
        if not path or not path.strip():
            raise ValueError('Не указан файл для бекапа')
        self.model.backup(path)

    def get_goals(self):
        return list(filter(lambda el: el.may_be_goal, self.model.vars))

    def take_goal(self):
        pass

    def ask_question(self):
        pass
