class Memory:
    def __init__(self):
        self.__rules = []
        self.__rules_dict = {}
        self.__vars = []
        self.__vars_dict = {}
        self.__vars_values = {}
        self.__domains = []
        self.__domains_dict = {}
        self.__active_rules = []

    @property
    def vars_values(self):
        return self.__vars_values

    @vars_values.setter
    def vars_values(self, vars_values):
        self.__vars_values = vars_values

    @property
    def vars(self):
        return self.__vars

    @property
    def domains(self):
        return self.__domains

    @property
    def rules(self):
        return self.__rules

    @property
    def active_rules(self):
        return self.__active_rules

    @active_rules.setter
    def active_rules(self, rules):
        if not isinstance(rules, list):
            raise ValueError('Попытка установить список активных правил не списком')
        self.__active_rules = rules

    def add_var_with_value(self, var, value):
        self.vars_values[var.name] = {
            'variable': var,
            'value': value
        }

    def get_var_value(self, var):
        return self.get_var_value_by_name(var.name)

    def get_var_value_by_name(self, var_name):
        return self.vars_values[var_name]

    def remove_var_with_value(self, var, value):
        if (
            var.name in self.vars_values.keys()
            and self.vars_values[var.name] == value
        ):
            self.vars_values.pop(var.name)

    def clear_var_values(self):
        self.vars_values = {}

    def check_var_assign_by_name(self, var_name):
        return var_name in self.vars_values.keys()

    def check_var_assign(self, var):
        return self.check_var_assign_by_name(var.name)

    def add_rule(self, rule):
        self.__rules_dict[rule.name] = rule
        self.rules.append(rule)

    def insert_rule(self, rule, pos):
        if not rule:
            raise ValueError('Попытка вставить правило, которого нет')
        if rule in self.rules:
            raise ValueError('Попытка вставить правило, которое уже есть')
        self.__rules_dict[rule.name] = rule
        self.rules.insert(pos, rule)

    def swap_rules(self, pos_from, pos_to):
        if pos_from < 0 or pos_to >= len(self.rules):
            raise ValueError('Неправильные индексы для перестановки правил')
        temp = self.rules[pos_from]
        self.rules[pos_from] = self.rules[pos_to]
        self.rules[pos_to] = temp

    def get_rule_index(self, name):
        return self.rules.index(name.upper().strip())

    def get_rule_by_name(self, name):
        if not name or not name.strip():
            raise ValueError('Попытка получить правило с пустым именем')
        name = name.upper().strip()
        return self.__rules_dict[name]

    def remove_rule(self, rule):
        if rule not in self.rules:
            raise ValueError('Попытка удалить правило, которого нет')
        for reason in rule.reasons:
            reason.var.remove_fact(reason)
        for conclusion in rule.conclusions:
            conclusion.var.remove_fact(conclusion)
        self.rules.remove(rule)
        self.__rules_dict.pop(rule.name)

    def add_active_rule(self, rule):
        if not rule:
            raise ValueError('Попытка добавить правило, которое не создано')
        if rule in self.active_rules:
            raise ValueError('Попытка добавить уже активное правило')
        self.active_rules.append(rule)

    def insert_active_rule(self, rule, pos):
        if not rule:
            raise ValueError('Попытка вставить правило, которого нет')
        if rule in self.active_rules:
            raise ValueError('Попытка вставить уже активное правило')
        self.active_rules.insert(pos, rule)

    def remove_active_rule(self, rule):
        if not rule:
            raise ValueError('Попытка удалить правило, которого нет')
        self.active_rules.remove(rule)

    def clear_active_rules(self):
        self.__active_rules = []

    def add_var(self, var):
        self.__vars_dict[var.name] = var
        self.vars.append(var)

    def get_var_by_name(self, name):
        if not name or not name.strip():
            raise ValueError('Попытка получить переменную с пустым именем')
        name = name.upper().strip()
        return self.__vars_dict[name]

    def remove_var(self, var):
        if var not in self.vars:
            raise ValueError('Попытка удалить переменную, которой нет')
        if var.used:
            raise ValueError('Попытка удалить переменную, которая уже используется')
        var.domain.remove_var(var)
        self.vars.remove(var)
        self.__vars_dict.pop(var.name)

    def add_domain(self, domain):
        self.__domains_dict[domain.name] = domain
        self.domains.append(domain)

    def get_domain_by_name(self, name):
        if not name or not name.strip():
            raise ValueError('Попытка получить домен с пустым именем')
        name = name.upper().strip()
        return self.__domains_dict[name]

    def remove_domain(self, domain):
        if domain not in self.domains:
            raise ValueError('Попытка удалить домен, которого нет')
        if domain.used:
            raise ValueError('Данный домен уже используется')
        self.domains.remove(domain)
        self.__domains_dict.pop(domain.name)

    def update_dicts(self):
        self.__domains_dict = {dom.name: dom for dom in self.domains}
        self.__vars_dict = {var.name: var for var in self.vars}
        self.__rules_dict = {rule.name: rule for rule in self.rules}
