from model.exceptions.UsedDomainError import UsedDomainError


class Domain:
    def __init__(self, name, values=None):
        self.__name = name.upper().strip()
        self.__values = values[:] if values else []
        self.__connected_vars = []

        self.__observers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError('Необходимо указать имя домена')
        if name.upper().strip() != self.name and self.used:
            raise UsedDomainError('Домен уже используется, поэтому его нельзя изменять')
        self.__name = name.upper().strip()
        self.notify_observers()

    @property
    def connected_vars(self):
        return self.__connected_vars

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values
        self.notify_observers()

    @property
    def used(self):
        return len(self.connected_vars) != 0

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        other_values = other.getValues()
        domain_size = len(self.name)
        if domain_size != len(other_values):
            return False
        for i in range(other_values):
            if other_values[i] != self.values[i]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.name + ':\n' + '\n'.join(map(str, self.values))

    def add_value(self, value):
        value = str(value).upper().strip()
        if value in self.values:
            raise ValueError('Попытка добавить в домен существующее значение')
        if self.used:
            raise UsedDomainError('Домен уже используется, поэтому его нельзя изменять')
        self.values.append(value)
        self.notify_observers()

    def remove_value(self, value):
        value = str(value).upper().strip()
        if self.used:
            raise UsedDomainError('Домен уже используется, поэтому его нельзя изменять')
        self.values.remove(value)
        self.notify_observers()

    def connect_var(self, var):
        if not var or not var.name.strip():
            raise ValueError('Необходимо указать имя переменной')
        self.connected_vars.append(var)
        self.notify_observers()

    def remove_var(self, var):
        if not var or not var.name.strip():
            raise ValueError('Необходимо указать имя переменной')
        if var not in self.connected_vars:
            raise ValueError('Попытка удалить переменную, которая не связана с доменом')
        self.connected_vars.remove(var)
        var.domain = []
        self.notify_observers()

    def add_observer(self, in_observer):
        self.__observers.append(in_observer)

    def remove_observer(self, in_observer):
        self.__observers.remove(in_observer)

    def notify_observers(self):
        for obs in self.__observers:
            obs.notify_model_is_changed()
