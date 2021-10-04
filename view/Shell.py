from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTableWidgetItem, QAbstractItemView, QFileDialog

import sys

from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.ShellWindow import UIShellWindow

from utils.Mixins import *


class Shell(QMainWindow):
    change_signal = pyqtSignal()

    def __init__(self, shell, parent=None):
        super(Shell, self).__init__(parent)

        self.ui_shell = shell

        self.ui = UIShellWindow()
        self.ui.setup_ui(self)

        self.setup_buttons()

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

    def refresh_all(self):
        self.refresh_rules()
        self.refresh_vars()
        self.refresh_domains()

    def refresh_rules(self):
        self.ui.rules_view.clearContents()
        self.ui.rules_view.setRowCount(self.ui_shell.rules)
        for i, rule in enumerate(self.ui_shell.rules):
            name = QTableWidgetItem(rule.name)
            name.setToolTip(rule.name)
            self.ui.rules_view.setItem(i, 0, name)

            description = QTableWidgetItem(rule.description or str(rule))
            description.setToolTip(str(rule))
            self.ui.rules_view.setItem(i, 1, description)

    def refresh_vars(self):
        self.ui.vars_view.clearContents()
        self.ui.vars_view.setRowCount(len(self.ui_shell.vars))
        for i, var in enumerate(self.ui_shell.vars):
            self.ui.vars_view.setItem(i, 0, QTableWidgetItem(var.name))
            var_type = QTableWidgetItem(var.var_type_str)
            var_type.setToolTip(var.var_type_str)
            self.ui.vars_view.setItem(i, 1, var_type)
            domain = QTableWidgetItem(var.domain.name)
            domain.setToolTip(str(var.domain))
            self.ui.vars_view.setItem(i, 2, domain)

    def refresh_domains(self):
        self.ui.domains_view.clearContents()
        self.ui.domains_view.setRowCount(len(self.ui_shell.domains))
        for i, domain in enumerate(self.ui_shell.domains):
            self.ui.domains_view.setItem(i, 0, QTableWidgetItem(domain.name))

    def drop_rule_cb(self, drop_row, rows_to_move):
        pass

    def load(self):
        return
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getOpenFileName(self,
                                                'QFileDialog.getOpenFileName()',
                                                r'G:\10_tr\ExpSysShell\MyShell\\',
                                                'ExpSys Files(*.json)',
                                                options=options)
        try:
            self.__controller.load(f_name)
        except ValueError as v_e:
            self.show_error(v_e)

    def backup(self):
        return
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getSaveFileName(self,
                                                'QFileDialog.getSaveFileName()',
                                                r'G:\10_tr\ExpSysShell\MyShell\\' + self.__model.name,
                                                'ExpSys Files(*.json)',
                                                options=options)

        if f_name.endswith('.json'):
            f_name = f_name.replace('.json', '')

        try:
            self.__model.name = f_name.split('/')[-1]
            self.__controller.backup(f_name)
        except ValueError as v_e:
            self.show_error(v_e)

    def open_consult_dialog(self):
        pass

    def exit_sys(self):
        pass

    def open_add_domain_dialog(self):
        pass

    def open_edit_domain_dialog(self):
        pass

    def remove_domain(self):
        pass

    def open_add_var_dialog(self):
        pass

    def open_edit_var_dialog(self):
        pass

    def remove_var(self):
        pass

    def open_add_rule_dialog(self):
        pass

    def open_edit_rule_dialog(self):
        pass

    def remove_rule(self):
        pass

    def change_domains_view(self):
        pass

    def change_domain_description(self):
        pass

    def change_vars_view(self):
        pass

    def change_var_description(self):
        pass

    def change_rules_view(self):
        pass

    def change_rule_description(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = Shell(None)
    ui.show()
    sys.exit(app.exec_())
