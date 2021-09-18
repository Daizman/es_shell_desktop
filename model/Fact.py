class Fact:
    def __init__(self, var, value):
        self.__var = var
        self.__value = value
        var.connect_fact(self)

    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var):
        if not var:
            raise ValueError('Попытка присвоить пустую переменную')
        self.__var.remove_fact(self)
        self.__var = var
        var.connect_fact(self)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not value:
            raise ValueError('Попытка присвоить пустое значение')
        self.__value = value

    @property
    def name(self):
        return self.__str__()

    def __str__(self):
        if self.__var and self.value:
            return f'{self.var.name} = {self.value}'
        return ''

    def __eq__(self, other):
        if other is not None and type(other) == 'Fact':
            return self.var == other.var and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)
