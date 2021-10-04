from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTableWidgetItem, QAbstractItemView, QFileDialog

import sys

from PyQt5.QtCore import pyqtSignal

from view.windows.ShellWindow import UIShellWindow

from model.Shell import Shell as ShellModel

from model.Domain import Domain as DomainModel
from controller.Domain import Domain as DomainController

from model.Var import Var as VarModel
from controller.Var import Var as VarController

from model.Rule import Rule as RuleModel
from controller.Rule import Rule as RuleController

from utils.Mixins import *


class Shell(QMainWindow, IShowError):
    change_signal = pyqtSignal()

    def __init__(self, shell, parent=None):
        super(Shell, self).__init__(parent)

        self.ui_name = shell.name

        self.ui_shell_domains = shell.domains
        self.ui_shell_vars = shell.vars
        self.ui_shell_rules = shell.rules

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
        self.ui.domains_view.cellClicked[int, int].connect(self.fill_domain_info)
        self.ui.vars_view.cellClicked[int, int].connect(self.fill_var_info)
        self.ui.rules_view.cellClicked[int, int].connect(self.fill_rule_info)

    def refresh_all(self):
        self.refresh_rules()
        self.refresh_vars()
        self.refresh_domains()

    def refresh_rules(self):
        self.ui.rules_view.clearContents()
        self.ui.rules_view.setRowCount(len(self.ui_shell_rules))
        for i, rule in enumerate(self.ui_shell_rules):
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
            self.ui.vars_view.setItem(i, 0, QTableWidgetItem(var.name))
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

    def fill_rule_info(self, row, col):
        reasons = [f'{reason.var.name}={reason.value}' for reason in self.ui_shell_rules[row].reasons]
        self.ui.requisite_te.setText('\n'.join(reasons))
        conclusions = [f'{conclusion.var.name}={conclusion.value}' for conclusion in self.ui_shell_rules[row].conclusions]
        self.ui.conclusion_te.setText('\n'.join(conclusions))

    def fill_var_info(self, row, col):
        self.ui.var_values_te.setText(str(self.ui_shell_vars[row].domain))
        self.ui.question_te.setText(str(self.ui_shell_vars[row].question))

    def fill_domain_info(self, row, col):
        self.ui.domain_values_te.setText(str(self.ui_shell_domains[row]))

    def load(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getOpenFileName(self,
                                                'Открытие ЭС',
                                                r'D:\projects\es_shell_desktop\backups\\',
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
        new_shell = ShellModel()
        new_shell.load(f_name)
        self.ui_shell_domains = new_shell.domains
        self.ui_shell_vars = new_shell.vars
        self.ui_shell_rules = new_shell.rules
        self.refresh_all()

    def backup(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getSaveFileName(self,
                                                'QFileDialog.getSaveFileName()',
                                                r'D:\projects\es_shell_desktop\backups\\' + self.ui_name,
                                                'ExpSys Files(*.json)',
                                                options=options)
        if not f_name.strip():
            return

        if not f_name.endswith('.json'):
            f_name += '.json'
        try:
            self.backup_shell_to(f_name)
            self.change_signal.emit()
        except ValueError as v_e:
            self.show_error(v_e)

    def backup_shell_to(self, f_name):
        self.ui_name = f_name.split('/')[-1]
        shell = ShellModel(self.ui_name)
        shell.domains = self.ui_shell_domains
        shell.vars = self.ui_shell_vars
        shell.rules = self.ui_shell_rules
        shell.backup(f_name)

    def open_consult_dialog(self):
        pass

    def exit_sys(self):
        shell = ShellModel('')
        self.ui_shell_domains = shell.domains
        self.ui_shell_vars = shell.vars
        self.ui_shell_rules = shell.rules
        self.refresh_all()

    def drop_rule_cb(self, drop_row, rows_to_move):
        rules = self.ui_shell_rules
        for row_index, data in enumerate(rows_to_move):
            row_index += drop_row
            temp = rules[drop_row]
            self.ui_shell_rules[drop_row] = rules[rows_to_move]
            self.ui_shell_rules[rows_to_move] = temp
        self.refresh_rules()

    def open_add_domain_dialog(self):
        new_domain = DomainModel()
        new_domain_controller = DomainController(new_domain, self)
        if new_domain_controller.exec_view():
            if new_domain in self.ui_shell_domains:
                self.show_error('Такой домен уже есть')
                return
            self.ui_shell_domains.append(new_domain)
            self.refresh_all()

    def open_edit_domain_dialog(self):
        domain_idx = self.ui.domains_view.selectedIndexes()
        if len(domain_idx) == 0:
            self.show_error('Выберите домен')
        else:
            domain = self.ui_shell_domains[domain_idx[0].row()]
            domain_controller = DomainController(domain, self)
            if domain_controller.exec_view():
                self.refresh_all()

    def remove_domain(self):
        for i in self.ui.domains_view.selectedIndexes():
            domain = self.ui_shell_domains[i]
            if domain.used:
                self.show_error('Попытка удалить используемый домен')
                return
            self.ui_shell_domains.remove(domain)

        self.refresh_all()

    def open_add_var_dialog(self):
        new_var = VarModel()
        new_var_controller = VarController(new_var, self.ui_shell_domains, parent=self)
        if new_var_controller.get_var():
            if new_var in self.ui_shell_vars:
                self.show_error('Такая переменная уже есть')
                return
            self.ui_shell_vars.append(new_var)
            self.refresh_all()

    def open_edit_var_dialog(self):
        var_idx = self.ui.vars_view.selectedItems()
        if len(var_idx) == 0:
            self.show_error('Выберите переменную')
        else:
            var = self.ui_shell_vars[var_idx[0].row()]
            var_controller = VarController(var, self.ui_shell_domains, self)
            if var_controller.get_var():
                self.refresh_all()

    def remove_var(self):
        for i in self.ui.vars_view.selectedIndexes():
            var = self.ui_shell_vars[i]
            if var.used:
                self.show_error('Попытка удалить используемую переменную')
                return
            self.ui_shell_vars.remove(var)

        self.refresh_all()

    def open_add_rule_dialog(self):
        new_rule = RuleModel()
        new_rule_controller = RuleController(new_rule, self.ui_shell_vars, self.ui_shell_domains, self)
        if new_rule_controller.get_rule():
            if new_rule in self.ui_shell_rules:
                self.show_error('Такое правило уже есть')
                return
            self.ui_shell_rules.append(new_rule)
            self.refresh_all()

    def open_edit_rule_dialog(self):
        rule_idx = self.ui.rules_view.selectedIndexes()
        if len(rule_idx) == 0:
            self.show_error('Выберите правило')
        else:
            rule = self.ui_shell_rules[rule_idx[0].row()]
            rule_controller = RuleController(rule, self.ui_shell_vars, self.ui_shell_domains, self)
            if rule_controller.get_rule():
                self.refresh_all()

    def remove_rule(self):
        for i in self.ui.rules_view.selectedIndexes():
            rule = self.ui_shell_rules[i]
            self.ui_shell_rules.remove(rule)

        self.refresh_all()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = Shell(ShellModel(''))
    ui.show()
    sys.exit(app.exec_())
