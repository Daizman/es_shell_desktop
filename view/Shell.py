from PyQt5.QtWidgets import QAction, QTableWidgetItem, QAbstractItemView, QFileDialog

from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.ShellWindow import UIShellWindow

from utils.Mixins import *


class Shell(IShowError):
    def __init__(self, shell, parent=None):
        super(Shell, self).__init__(parent)

        self.ui_shell = shell

        self.ui = UIShellWindow()
        self.ui.setup_ui(self)

    def connect_buttons(self):
        pass

    def drop_rule_cb(self, drop_row, rows_to_move):
        pass

    def load(self):
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
