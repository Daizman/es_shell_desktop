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

    def add_domain(self, domain):
        self.domains.append(domain)

    def add_var(self, var):
        self.vars.append(var)

    def get_var_by_name(self, name):
        for var in self.vars:
            if var.name == name.strip().upper():
                return var
