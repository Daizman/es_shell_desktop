from PyQt5.QtWidgets import QMainWindow, QFileDialog, QErrorMessage

from utils.Observer import Observer
from utils.ObserverMeta import ObserverMeta

from view.MainWindow import UIMainWindow

from model.Shell import Shell as ShellModel


class Shell(QMainWindow, Observer, metaclass=ObserverMeta):
    def __init__(self, controller, model, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.controller = controller
        self.model = model

        self.ui = UIMainWindow()
        self.ui.setup_ui(self)

        self.model.add_observer(self)

        # self.connect(self.ui., )

    def connect_buttons(self):
        self.consult_button.clicked.connect(self.openConsultWindow)

        self.open_file.triggered.connect(self.load)
        self.save_file_as.triggered.connect(self.backup)
        self.exit.triggered.connect(self.exit_es)

        self.add_rule_button.clicked.connect(self.openAddRuleWindow)
        self.edit_rule_button.clicked.connect(self.openEditRuleWindow)
        self.del_rule_button.clicked.connect(self.delRule)

        self.add_var_button.clicked.connect(self.openAddVarWindow)
        self.edit_var_button.clicked.connect(self.openEditVarWindow)
        self.del_var_button.clicked.connect(self.delVar)

        self.add_domain_button.clicked.connect(self.openAddDomenWindow)
        self.edit_domain_button.clicked.connect(self.openEditDomenWindow)
        self.del_domain_button.clicked.connect(self.delDomen)

    def drop_rule_cb(self, drop_row, rows_to_move):
        for row_index, data in enumerate(rows_to_move):
            row_index += drop_row
            self.controller.swap_rules(drop_row, row_index)

    def load(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getOpenFileName(self,
                                                'QFileDialog.getOpenFileName()',
                                                r'G:\10_tr\ExpSysShell\MyShell\\',
                                                'ExpSys Files(*.json)',
                                                options=options)

        try:
            self.controller.load(f_name)
            self.model_is_changed()
        except ValueError as v_e:
            self.show_error(v_e)

    def backup(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getSaveFileName(self,
                                                'QFileDialog.getSaveFileName()',
                                                r'G:\10_tr\ExpSysShell\MyShell\\' + self.model.name,
                                                'ExpSys Files(*.json)',
                                                options=options)

        if f_name.endswith('.json'):
            f_name = f_name.replace('.json', '')

        try:
            self.model.name = f_name.split('/')[-1]
            self.controller.backup(f_name)
            self.model_is_changed()
        except ValueError as v_e:
            self.show_error(v_e)

    def exit_es(self):
        self.model = ShellModel('')
        self.model_is_changed()

    def show_error(self, v_e):
        error_dialog = QErrorMessage(self)
        error_dialog.showMessage(v_e)

    def domains_changed(self):
        pass

    def vars_changed(self):
        pass

    def rules_changed(self):
        pass

    def model_is_changed(self):
        pass
