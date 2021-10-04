class Memory:
    def __init__(self):
        self.__rules = []
        self.__vars = []
        self.__domains = []

    @property
    def vars(self):
        return self.__vars

    @property
    def domains(self):
        return self.__domains

    @property
    def rules(self):
        return self.__rules

    def clear_domains(self):
        self.__domains = []

    def clear_vars(self):
        self.__vars = []

    def clear_rules(self):
        self.__rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def insert_rule(self, rule, pos):
        if not rule:
            raise ValueError('Попытка вставить правило, которого нет')
        if rule in self.rules:
            raise ValueError('Попытка вставить правило, которое уже есть')
        self.rules.insert(pos, rule)

    def swap_rules(self, pos_from, pos_to):
        if pos_from < 0 or pos_to >= len(self.rules):
            raise ValueError('Неправильные индексы для перестановки правил')
        temp = self.rules[pos_from]
        self.rules[pos_from] = self.rules[pos_to]
        self.rules[pos_to] = temp

    def get_rule_index(self, name):
        return self.rules.index(name.upper().strip())

    def remove_rule(self, rule):
        if rule not in self.rules:
            raise ValueError('Попытка удалить правило, которого нет')
        for reason in rule.reasons:
            reason.var.remove_fact(reason)
        for conclusion in rule.conclusions:
            conclusion.var.remove_fact(conclusion)
        self.rules.remove(rule)

    def add_domain(self, domain):
        self.domains.append(domain)

    def add_var(self, var):
        self.vars.append(var)

    def remove_var(self, var):
        if var not in self.vars:
            raise ValueError('Попытка удалить переменную, которой нет')
        if var.used:
            raise ValueError('Попытка удалить переменную, которая уже используется')
        var.domain.remove_var(var)
        self.vars.remove(var)

    def remove_domain(self, domain):
        if domain not in self.domains:
            raise ValueError('Попытка удалить домен, которого нет')
        if domain.used:
            raise ValueError('Данный домен уже используется')
        self.domains.remove(domain)
