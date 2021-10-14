class Fact:
    def __init__(self, var=None, value=None):
        self.__var = var
        self.__value = value
        if var:
            var.connect_fact(self)

    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, variable):
        if not variable:
            raise ValueError('Попытка присвоить пустую переменную')
        if self.__var:
            self.__var.remove_fact(self)
        self.__var = variable
        variable.connect_fact(self)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not value:
            raise ValueError('Попытка присвоить пустое значение')
        if value not in self.var.domain.values:
            raise ValueError('Попытка присвоить значение не из домена переменной')
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
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
