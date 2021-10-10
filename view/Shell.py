import os

from PyQt5.QtWidgets import QMainWindow, QAction, QTableWidgetItem, QFileDialog

from PyQt5.QtCore import QModelIndex

from view.windows.ShellWindow import UIShellWindow

from model.Domain import Domain as DomainModel
from controller.Domain import Domain as DomainController

from model.Var import Var as VarModel
from controller.Var import Var as VarController

from model.Rule import Rule as RuleModel
from controller.Rule import Rule as RuleController

from model.Consult import Consult as ConsultModel
from controller.Consult import Consult as ConsultController

from view.Consult import Consult as ConsultView

from utils.Mixins import *


class Shell(QMainWindow, IShowError):
    def __init__(self, controller, parent=None):
        super(Shell, self).__init__(parent)

        self.controller = controller

        self.ui_name = controller.get_name()
        self.ui_shell_domains = controller.get_domains()
        self.ui_shell_vars = controller.get_variants()
        self.ui_shell_rules = controller.get_rules()

        self.ui = UIShellWindow()
        self.ui.setup_ui(self)

        self.setup_buttons()
        self.setup_events()

    def setup_buttons(self):
        acts = [self.open_consult_dialog, self.load, self.backup, self.exit_sys]
        for i, act in enumerate(self.ui.actions.in_action_names):
            self.findChild(QAction, act).triggered.connect(acts[i])

        self.ui.add_rule_button.clicked.connect(self.open_add_rule_dialog)
        self.ui.edit_rule_button.clicked.connect(self.open_edit_rule_dialog)
        self.ui.remove_rule_button.clicked.connect(self.remove_rule)

        self.ui.add_var_button.clicked.connect(self.open_add_var_dialog)
        self.ui.edit_var_button.clicked.connect(self.open_edit_var_dialog)
        self.ui.remove_var_button.clicked.connect(self.remove_var)

        self.ui.add_domain_button.clicked.connect(self.open_add_domain_dialog)
        self.ui.edit_domain_button.clicked.connect(self.open_edit_domain_dialog)
        self.ui.remove_domain_button.clicked.connect(self.remove_domain)

    def setup_events(self):
        self.ui.rules_view.set_drop_event_callback(self.drop_rule_cb)
        self.ui.domains_view.selectionModel().currentRowChanged[QModelIndex, QModelIndex].connect(self.fill_domain_info)
        self.ui.vars_view.selectionModel().currentRowChanged[QModelIndex, QModelIndex].connect(self.fill_var_info)
        self.ui.rules_view.selectionModel().currentRowChanged[QModelIndex, QModelIndex].connect(self.fill_rule_info)

    def refresh_all(self):
        self.refresh_rules()
        self.refresh_vars()
        self.refresh_domains()

    def refresh_rules(self):
        self.ui.rules_view.clearContents()
        self.ui.rules_view.setRowCount(len(self.ui_shell_rules))
        for i, rule in enumerate(reversed(self.ui_shell_rules)):
            name = QTableWidgetItem(rule.name)
            name.setToolTip(rule.name)
            self.ui.rules_view.setItem(i, 0, name)

            description = QTableWidgetItem(rule.description or str(rule))
            description.setToolTip(str(rule))
            self.ui.rules_view.setItem(i, 1, description)

    def refresh_vars(self):
        self.ui.vars_view.clearContents()
        self.ui.vars_view.setRowCount(len(self.ui_shell_vars))
        for i, var in enumerate(self.ui_shell_vars):
            var_name = QTableWidgetItem(var.name)
            var_name.setToolTip(var.name)
            self.ui.vars_view.setItem(i, 0, var_name)
            var_type = QTableWidgetItem(var.var_type_str)
            var_type.setToolTip(var.var_type_str)
            self.ui.vars_view.setItem(i, 1, var_type)
            domain = QTableWidgetItem(var.domain.name)
            domain.setToolTip(str(var.domain))
            self.ui.vars_view.setItem(i, 2, domain)

    def refresh_domains(self):
        self.ui.domains_view.clearContents()
        self.ui.domains_view.setRowCount(len(self.ui_shell_domains))
        for i, domain in enumerate(self.ui_shell_domains):
            self.ui.domains_view.setItem(i, 0, QTableWidgetItem(domain.name))

    def fill_rule_info(self, current, prev):
        if current.row() == -1:
            return
        row = len(self.ui_shell_rules) - current.row() - 1
        reasons = [f'{reason.var.name}={reason.value}' for reason in self.ui_shell_rules[row].reasons]
        self.ui.requisite_te.setText('\n'.join(reasons))
        conclusions = [f'{conclusion.var.name}={conclusion.value}' for conclusion in self.ui_shell_rules[row].conclusions]
        self.ui.conclusion_te.setText('\n'.join(conclusions))

    def fill_var_info(self, current, prev):
        row = current.row()
        self.ui.var_values_te.setText(str(self.ui_shell_vars[row].domain))
        self.ui.question_te.setText(str(self.ui_shell_vars[row].question))

    def fill_domain_info(self, current, prev):
        self.ui.domain_values_te.setText(str(self.ui_shell_domains[current.row()]))

    def load(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getOpenFileName(self,
                                                'Открытие ЭС',
                                                os.environ['BACKUP_FOLDER'],
                                                'ExpSys Files(*.json)',
                                                options=options)
        if not f_name.strip():
            return
        try:
            self.load_shell_from(f_name)
        except ValueError as v_e:
            self.show_error(v_e)
        except BaseException as b_e:
            self.show_error(b_e)

    def load_shell_from(self, f_name):
        self.controller.load(f_name)
        self.ui_shell_domains = self.controller.get_domains()
        self.ui_shell_vars = self.controller.get_variants()
        self.ui_shell_rules = self.controller.get_rules()
        self.refresh_all()

    def backup(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getSaveFileName(self,
                                                'QFileDialog.getSaveFileName()',
                                                os.environ['backup_folder'] + self.ui_name,
                                                'ExpSys Files(*.json)',
                                                options=options)
        if not f_name.strip():
            return

        if not f_name.endswith('.json'):
            f_name += '.json'
        try:
            self.backup_shell_to(f_name)
        except ValueError as v_e:
            self.show_error(v_e)

    def backup_shell_to(self, f_name):
        self.controller.set_name(f_name.split('/')[-1])
        self.controller.backup(f_name)

    def open_consult_dialog(self):
        if len(list(filter(lambda var: var.can_be_goal, self.controller.get_variants()))) == 0:
            self.show_error('Нет целей')
            return
        consult = ConsultModel(self.controller.get_variants(), self.controller.get_rules())
        consult_controller = ConsultController(consult, ConsultView, self)
        consult_controller.show()

    def exit_sys(self):
        self.controller.clear_shell()
        self.ui_name = self.controller.get_name()
        self.ui_shell_domains = self.controller.get_domains()
        self.ui_shell_vars = self.controller.get_variants()
        self.ui_shell_rules = self.controller.get_rules()
        self.refresh_all()

    def drop_rule_cb(self, drop_row, rows):
        rows_to_rem = [self.ui_shell_rules[row] for row in rows]
        for row in rows_to_rem:
            self.ui_shell_rules.remove(row)

        for i, row in enumerate(rows_to_rem):
            self.ui_shell_rules.insert(i + drop_row, row)
        self.refresh_rules()

    def open_add_domain_dialog(self):
        new_domain = DomainModel()
        new_domain_controller = DomainController(new_domain, self)
        if new_domain_controller.exec_view():
            self.controller.add_domain(new_domain)
            self.ui_shell_domains = self.controller.get_domains()
            self.refresh_all()

    def open_edit_domain_dialog(self):
        domain_idx = self.ui.domains_view.selectedIndexes()
        if len(domain_idx) == 0:
            self.show_error('Выберите домен')
        else:
            domain = self.ui_shell_domains[domain_idx[0].row()]
            domain_controller = DomainController(domain, self)
            if domain_controller.exec_view():
                self.controller.set_domains(self.ui_shell_domains)
                self.refresh_all()

    def remove_domain(self):
        domain_idx = self.ui.domains_view.selectedIndexes()
        if len(domain_idx) == 0:
            self.show_error('Выберите домен')
        else:
            domain = self.ui_shell_domains[domain_idx[0].row()]
            if domain.used:
                self.show_error('Попытка удалить используемый домен')
                return
            self.ui_shell_domains.remove(domain)
            self.controller.set_domains(self.ui_shell_domains)

        self.refresh_all()

    def open_add_var_dialog(self):
        new_var = VarModel()
        new_var_controller = VarController(new_var, self.ui_shell_domains, parent=self)
        if new_var_controller.get_var():
            self.controller.set_domains(self.ui_shell_domains)
            self.controller.add_var(new_var)
            self.ui_shell_vars = self.controller.get_variants()
            self.refresh_all()

    def open_edit_var_dialog(self):
        var_idx = self.ui.vars_view.selectedItems()
        if len(var_idx) == 0:
            self.show_error('Выберите переменную')
        else:
            var = self.ui_shell_vars[var_idx[0].row()]
            var_controller = VarController(var, self.ui_shell_domains, self)
            if var_controller.get_var():
                self.controller.set_domains(self.ui_shell_domains)
                self.controller.set_variants(self.ui_shell_vars)
                self.refresh_all()

    def remove_var(self):
        var_idx = self.ui.vars_view.selectedItems()
        if len(var_idx) == 0:
            self.show_error('Выберите переменную')
        else:
            var = self.ui_shell_vars[var_idx[0].row()]
            if var.used:
                self.show_error('Попытка удалить используемую переменную')
                return
            self.ui_shell_vars.remove(var)
            self.controller.set_variants(self.ui_shell_vars)

        self.refresh_all()

    def open_add_rule_dialog(self):
        new_rule = RuleModel()
        new_rule_controller = RuleController(new_rule, self.ui_shell_vars, self.ui_shell_domains, self)
        if new_rule_controller.get_rule():
            self.controller.set_domains(self.ui_shell_domains)
            self.controller.set_variants(self.ui_shell_vars)
            self.controller.add_rule(new_rule)
            self.ui_shell_rules = self.controller.get_rules()
            self.refresh_all()

    def open_edit_rule_dialog(self):
        rule_idx = self.ui.rules_view.selectedIndexes()
        if len(rule_idx) == 0:
            self.show_error('Выберите правило')
        else:
            rule = self.ui_shell_rules[len(self.ui_shell_rules) - rule_idx[0].row() - 1]
            rule_controller = RuleController(rule, self.ui_shell_vars, self.ui_shell_domains, self)
            if rule_controller.get_rule():
                self.controller.set_domains(self.ui_shell_domains)
                self.controller.set_variants(self.ui_shell_vars)
                self.controller.set_rules(self.ui_shell_rules)
                self.refresh_all()

    def remove_rule(self):
        rule_idx = self.ui.rules_view.selectedIndexes()
        if len(rule_idx) == 0:
            self.show_error('Выберите правило')
        else:
            rule = self.ui_shell_rules[len(self.ui_shell_rules) - rule_idx[0].row() - 1]
            self.ui_shell_rules.remove(rule)
            self.controller.set_rules(self.ui_shell_rules)

        self.refresh_all()
