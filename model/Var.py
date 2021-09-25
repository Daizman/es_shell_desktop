from model.types.VarType import VarType
from model.exceptions.UsedVarError import UsedVarError


class Var:
    def __init__(self, name='', domain=None, question='', var_type=VarType.INFERRED, may_be_goal=False):
        self.__name = name.upper().strip()
        self.__question = question.strip() if question else f'{self.__name}?'
        self.__var_type = var_type
        self.__may_be_goal = may_be_goal
        self.__facts = []
        self.__domain = domain
        if domain:
            self.__domain.connect_var(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError('Переменной нельзя присвоить пустое имя')
        if name.upper().strip() != self.name and self.used:
            raise UsedVarError('Переменная уже используется, поэтому ее нельзя изменять')
        self.__name = name.upper().strip()
        self.__question = f'{self.__name}?'

    @property
    def may_be_goal(self):
        return self.__may_be_goal

    @may_be_goal.setter
    def may_be_goal(self, may_be):
        self.__may_be_goal = may_be

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, domain):
        if not domain:
            raise ValueError('Переменной нельзя присвоить пустой домен')
        if domain != self.domain and self.used:
            raise UsedVarError('Переменная уже используется, поэтому ее нельзя изменять')
        self.__domain.remove_var(self)
        self.__domain = domain
        self.__domain.connect_var(self)

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, question):
        if not question and not question.strip():
            raise ValueError('Нельзя установить пустой вопрос')
        if question.strip() != self.question and self.used:
            raise UsedVarError('Переменная уже используется, поэтому ее нельзя изменять')
        self.__question = question.strip()

    @property
    def facts(self):
        return self.__facts

    @property
    def var_type(self):
        return self.__var_type

    @var_type.setter
    def var_type(self, var_type):
        if not var_type or not isinstance(var_type, VarType):
            raise ValueError('Попытка присвоить неверный тип переменной')
        if self.used:
            raise UsedVarError('Переменная уже используется, поэтому ее нельзя изменять')
        self.__var_type = var_type
        self.__question = f'{self.__name}?'

    @property
    def var_type_str(self):
        if self.var_type == VarType.REQUESTED:
            return 'Запрашиваемая'
        elif self.var_type == VarType.INFERRED:
            return 'Выводимая'
        else:
            return 'Запрашиваемо-выводимая'

    @property
    def used(self):
        return len(self.__facts) != 0

    def __eq__(self, other):
        return other.name == self.name \
               and other.domain == self.domain \
               and other.question == self.question \
               and other.var_type == self.var_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'Name: {self.name};' \
               f'\nDomain: {self.domain};' \
               f'\nQuestion: {self.question};' \
               f'\nType: {self.var_type_str}'

    def used_in_fact(self, fact):
        return fact in self.__facts

    def connect_fact(self, fact):
        if not fact:
            raise ValueError('Попытка добавить пустой факт')
        if fact in self.facts:
            raise ValueError('Попытка добавить существующий в связках факт')
        self.__facts.append(fact)

    def remove_fact(self, fact):
        if not fact:
            raise ValueError('Попытка удалить пустой факт')
        self.__facts.remove(fact)
