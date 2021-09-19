from PyQt5.QtWidgets import QMainWindow,\
    QFileDialog,\
    QErrorMessage,\
    QAbstractItemView, \
    QTableWidgetItem

from utils.Observer import Observer
from utils.ObserverMeta import ObserverMeta

from view.windows.MainWindow import UIMainWindow

from model.Shell import Shell as ShellModel


class Shell(QMainWindow, Observer, metaclass=ObserverMeta):
    def __init__(self, controller, model, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.__controller = controller
        self.__model = model

        self.ui = UIMainWindow()
        self.ui.setup_ui(self)

        self.__model.add_observer(self)
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.consult_button.clicked.connect(self.open_consult_dialog)

        self.ui.open_file.triggered.connect(self.load)
        self.ui.save_file_as.triggered.connect(self.backup)
        self.ui.exit.triggered.connect(self.exit_es)

        self.ui.add_rule_button.clicked.connect(self.open_add_rule_dialog)
        self.ui.edit_rule_button.clicked.connect(self.open_edit_rule_dialog)
        self.ui.remove_rule_button.clicked.connect(self.remove_rule)

        self.ui.add_var_button.clicked.connect(self.open_add_var_dialog)
        self.ui.edit_var_button.clicked.connect(self.open_edit_var_dialog)
        self.ui.remove_var_button.clicked.connect(self.remove_var)

        self.ui.add_domain_button.clicked.connect(self.open_add_domain_dialog)
        self.ui.edit_domain_button.clicked.connect(self.open_edit_domain_dialog)
        self.ui.remove_domain_button.clicked.connect(self.remove_domain)

    def drop_rule_cb(self, drop_row, rows_to_move):
        for row_index, data in enumerate(rows_to_move):
            row_index += drop_row
            self.__controller.swap_rules(drop_row, row_index)
        self.notify_model_is_changed()

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
            self.notify_model_is_changed()
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

    def exit_es(self):
        self.__model = ShellModel('')
        self.notify_model_is_changed()

    def show_error(self, e):
        error_dialog = QErrorMessage(self)
        error_dialog.setWindowTitle('Ошибка!')
        error_dialog.showMessage(e)

    def open_consult_dialog(self):
        pass

    def open_add_domain_dialog(self):
        pass

    def open_edit_domain_dialog(self):
        pass

    def remove_domain(self):
        if len(self.ui.domain_values.selectedItems()) == 0:
            self.show_error('Нужно выбрать домен')
            return False
        try:
            self.__controller.remove_domain(self.ui.domains_view.selectedItems()[0].text())
            self.notify_model_is_changed()
        except ValueError as v_e:
            self.show_error(v_e)

    def open_add_var_dialog(self):
        pass

    def open_edit_var_dialog(self):
        pass

    def remove_var(self):
        if len(self.ui.vars_view.selectedItems()) == 0:
            self.show_error('Нужно выбрать переменную')
            return False
        try:
            self.__controller.remove_var(self.ui.vars_view.selectedItems()[0].text())
            self.notify_model_is_changed()
        except ValueError as v_e:
            self.show_error(v_e)

    def open_add_rule_dialog(self):
        pass

    def open_edit_rule_dialog(self):
        pass

    def remove_rule(self):
        if len(self.ui.rules_view.selectedItems()) == 0:
            self.show_error('Нужно выбрать правило')
            return False
        try:
            self.__controller.remove_rule(self.ui.rules_view.selectedItems()[0].text())
            self.notify_model_is_changed()
        except ValueError as v_e:
            self.show_error(v_e)

    def change_domains_view(self):
        self.ui.domain_values.clear()
        domains = self.__model.domains
        self.ui.domains_view.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.ui.domains_view.clear()
        self.ui.domains_view.setColumnCount(1)
        self.ui.domains_view.cellClicked.connect(self.change_domain_description)
        self.ui.domains_view.setHorizontalHeaderLabels(['Имя'])
        self.ui.domains_view.setRowCount(len(domains))
        for i, domain in enumerate(domains):
            self.ui.domains_view.setItem(i, 0, QTableWidgetItem(domain.name))
        self.ui.domains_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def change_domain_description(self):
        self.ui.domain_values.clear()
        domain = self.__controller.get_domain_by_name(self.ui.domains_view.selectedItems()[0].text())
        if domain:
            self.ui.domain_values.setText(',\n'.join(domain.values))

    def change_vars_view(self):
        self.ui.question_text.clear()
        self.ui.domains_var_text.clear()
        _vars = self.__model.vars
        self.ui.vars_view.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.ui.vars_view.clear()
        self.ui.vars_view.cellClicked.connect(self.change_var_description)
        self.ui.vars_view.setColumnCount(3)
        self.ui.vars_view.setHorizontalHeaderLabels(['Имя', 'Тип', 'Домен'])
        self.ui.vars_view.setRowCount(len(_vars))
        for i, var in enumerate(_vars):
            self.ui.vars_view.setItem(i, 0, QTableWidgetItem(var.name))
            var_type = QTableWidgetItem(var.var_type_str)
            var_type.setToolTip(var.var_type_str)
            self.ui.vars_view.setItem(i, 1, var_type)
            domain = QTableWidgetItem(var.domain.name)
            domain.setToolTip(str(var.domain))
            self.ui.vars_view.setItem(i, 2, domain)
        self.ui.vars_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def change_var_description(self):
        self.ui.question_text.clear()
        self.ui.domains_var_text.clear()
        try:
            selected_var = self.__controller.get_var_by_name(self.ui.vars_view.selectedItems()[0].text())
            self.ui.question_text.setText(selected_var.question)
            self.ui.domains_var_text.setText(';\n'.join(selected_var.domain.values))
        except ValueError as v_e:
            self.show_error(v_e)

    def change_rules_view(self):
        self.ui.conclusion_text.clear()
        self.ui.requisite_text.clear()
        rules = self.__model.rules
        self.ui.rules_view.clear()
        self.ui.rules_view.cellClicked.connect(self.change_rule_description)
        self.ui.rules_view.setColumnCount(2)
        self.ui.rules_view.setHorizontalHeaderLabels(['Имя', 'Описание'])
        self.ui.rules_view.setRowCount(len(rules))
        for i, rule in enumerate(reversed(rules)):
            name = QTableWidgetItem(rule.name)
            name.setToolTip(rule.name)
            self.rules_view.setItem(i, 0, name)
            description = rule.description if rule.description != '' else str(rule)
            description = QTableWidgetItem(description)
            description.setToolTip(str(rule))
            self.rules_view.setItem(i, 1, description)

    def change_rule_description(self):
        self.ui.conclusion_text.clear()
        self.ui.requisite_text.clear()
        selected_rule = self.__controller.get_rule_by_name(self.ui.rules_view.selectedItems()[0].text())
        if selected_rule:
            self.ui.requisite_text.setText(', '.join([str(fact) for fact in selected_rule.reasons]))
            self.ui.conclusion_text.setText(', '.join([str(fact) for fact in selected_rule.conclusions]))

    def notify_model_is_changed(self):
        self.change_domains_view()
        self.change_vars_view()
        self.change_rules_view()
