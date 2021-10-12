import jsonpickle

from model.Memory import Memory
from model.Domain import Domain
from model.Var import Var
from model.Rule import Rule

from model.types.VarType import VarType


class Shell:
    def __init__(self, name=''):
        self.__name = name.upper().strip()
        self.__memory = Memory()

    @property
    def name(self):
        return self.__name

    @property
    def domains(self):
        return self.__memory.domains[:]

    @domains.setter
    def domains(self, domains):
        self.__memory.clear_domains()
        for domain in domains:
            self.__memory.add_domain(domain)

    @property
    def rules(self):
        return self.__memory.rules[:]

    @rules.setter
    def rules(self, rules):
        self.__memory.clear_rules()
        for rule in rules:
            self.__memory.add_rule(rule)

    @property
    def variants(self):
        return self.__memory.vars[:]

    @variants.setter
    def variants(self, variants):
        self.__memory.clear_vars()
        for var in variants:
            self.__memory.add_var(var)

    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError('Попытка установить пустое имя для ЭС')
        self.__name = name.upper().strip()

    def add_rule(self, name, description, reasons, conclusion):
        self.__memory.add_rule(Rule(name, description, reasons, conclusion))

    def add_var(self, name, domain, question='', var_type=VarType.REQUESTED):
        self.__memory.add_var(Var(name, domain, question, var_type))

    def add_domain(self, name, values):
        self.__memory.add_domain(Domain(name, values))

    def get_var_by_name(self, name):
        return self.__memory.get_var_by_name(name)

    def load(self, path):
        with open(path, 'r') as kb_backup:
            restored_es_json = kb_backup.readline()
            restored_es = jsonpickle.decode(restored_es_json)
            self.__name = restored_es.name
            self.domains = restored_es.domains
            self.variants = restored_es.variants
            self.rules = restored_es.rules

    def backup(self, path):
        with open(path, 'w') as backup:
            backup.write(jsonpickle.encode(self))

    def clear(self):
        self.__name = ''
        self.__memory = Memory()
