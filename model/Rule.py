class Rule:
    def __init__(self, name, description='', reasons=None, conclusions=None):
        self.__name = name.upper().strip()
        self.__description = description
        self.__reasons = reasons if reasons else []
        self.__conclusions = conclusions if conclusions else []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError('Попытка установить пустое имя для правила')
        self.__name = name.upper().strip()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not description or not description.strip():
            raise ValueError('Попытка установить пустое описание у правила')
        self.__description = description

    @property
    def reasons(self):
        return self.__reasons

    @reasons.setter
    def reasons(self, reasons):
        if not reasons:
            raise ValueError('Попытка установить пустую посылку для правила')
        self.clear_reasons()
        self.__reasons = reasons

    @property
    def conclusions(self):
        return self.__conclusions

    @conclusions.setter
    def conclusions(self, conclusions):
        if not conclusions:
            raise ValueError('Попытка установить пустые выводы из правила')
        self.clear_conclusions()
        self.__conclusions = conclusions

    def __str__(self):
        res = ''
        first = True
        for reason in self.__reasons:
            if first:
                res += 'if: ' + str(reason)
                first = False
            else:
                res += ' and ' + str(reason)
        first = True
        for conclusion in self.__conclusions:
            if first:
                res += ' then: ' + str(conclusion)
                first = False
            else:
                res += ' and ' + str(conclusion)
        return res

    def add_reason(self, reason):
        if not reason:
            raise ValueError('Попытка добавить пустую причину')
        if reason in self.reasons:
            raise ValueError('Поптыка добавить существующую причину')
        self.reasons.append(reason)

    def insert_reason(self, reason, pos):
        if not reason:
            raise ValueError('Не указана причина для вставки')
        if reason in self.reasons:
            raise ValueError('Поптыка вставить существующую причину')
        self.reasons.insert(pos, reason)

    def swap_reasons(self, pos_from, pos_to):
        if pos_from < 0 or pos_to >= len(self.__reasons):
            raise ValueError('Неправильные индексы для перестановки причин')
        temp = self.__reasons[pos_from]
        self.__reasons[pos_from] = self.__reasons[pos_to]
        self.__reasons[pos_to] = temp

    def remove_reason(self, reason):
        if not reason:
            raise ValueError('Попытка удалить пустую причину')
        self.__reasons.remove(reason)

    def clear_reasons(self):
        self.__reasons = []

    def add_conclusion(self, conclusion):
        if not conclusion:
            raise ValueError('Попытка добавить пустой вывод')
        if conclusion in self.conclusions:
            raise ValueError('Поптыка добавить существующий вывод')
        self.conclusions.append(conclusion)

    def insert_conclusion(self, conclusion, pos):
        if not conclusion:
            raise ValueError('Не указан вывод для вставки')
        if conclusion in self.conclusions:
            raise ValueError('Поптыка вставить существующий вывод')
        self.conclusions.insert(pos, conclusion)

    def swap_conclusions(self, pos_from, pos_to):
        if pos_from < 0 or pos_to >= len(self.conclusions):
            raise ValueError('Неправильные индексы для перестановки выводов')
        temp = self.conclusions[pos_from]
        self.conclusions[pos_from] = self.conclusions[pos_to]
        self.conclusions[pos_to] = temp

    def remove_conclusion(self, conclusion):
        if not conclusion:
            raise ValueError('Попытка удалить пустой вывод')
        self.__conclusions.remove(conclusion)

    def clear_conclusions(self):
        self.__conclusions = []
