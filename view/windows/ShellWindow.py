from PyQt5 import QtCore, QtWidgets

from view.pyqt5_exten.TableWidgetDragRows import TableWidgetDragRows


class UIShellWindow(object):
    def setup_ui(self, shell_view):
        shell_view.setObjectName('shell_view')
        shell_view.resize(660, 525)

        self.central_widget = QtWidgets.QWidget(shell_view)
        self.central_widget.setObjectName('central_widget')

        self.tab_panel = QtWidgets.QTabWidget(self.central_widget)
        self.tab_panel.setEnabled(True)

        self.tab_panel.setObjectName('tab_panel')

        rule_tab = QtWidgets.QWidget()
        rule_tab.setWindowTitle('Правила')

        rule_grid = QtWidgets.QGridLayout()
        rule_tab.setLayout(rule_grid)

        edit_rules_gb = QtWidgets.QGroupBox(rule_tab)

        self.add_rule_button = QtWidgets.QPushButton(edit_rules_gb)
        self.add_rule_button.setObjectName('add_rule_button')

        self.edit_rule_button = QtWidgets.QPushButton(edit_rules_gb)
        self.edit_rule_button.setObjectName('edit_rule_button')

        self.remove_rule_button = QtWidgets.QPushButton(edit_rules_gb)
        self.remove_rule_button.setObjectName('remove_rule_button')

        requisite_gb = QtWidgets.QGroupBox(rule_tab)

        self.requisite_te = QtWidgets.QTextEdit(requisite_gb)
        self.requisite_te.setEnabled(False)
        self.requisite_te.setObjectName('requisite_te')

        conclusion_gb = QtWidgets.QGroupBox(rule_tab)

        self.conclusion_te = QtWidgets.QTextEdit(conclusion_gb)
        self.conclusion_te.setEnabled(False)
        self.conclusion_te.setObjectName('conclusion_te')

        self.rules_view = TableWidgetDragRows(rule_tab, drop_event_callback=shell_view.drop_rule_cb)
        self.rules_view.setObjectName('rules_view')
        self.rules_view.setColumnCount(2)
        self.rules_view.setHorizontalHeaderLabels(['Имя', 'Описание'])
        self.rules_view.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.rules_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tab_panel.addTab(rule_tab, '')

        var_tab = QtWidgets.QWidget()
        var_tab.setWindowTitle('Переменные')

        var_grid = QtWidgets.QGridLayout()
        var_tab.setLayout(var_grid)

        edit_var_gb = QtWidgets.QGroupBox(var_tab)

        self.add_var_button = QtWidgets.QPushButton(edit_var_gb)
        self.add_var_button.setObjectName('add_var_button')

        self.edit_var_button = QtWidgets.QPushButton(edit_var_gb)
        self.edit_var_button.setObjectName('edit_var_button')

        self.remove_var_button = QtWidgets.QPushButton(edit_var_gb)
        self.remove_var_button.setObjectName('remove_var_button')

        question_gb = QtWidgets.QGroupBox(var_tab)

        self.question_te = QtWidgets.QTextEdit(question_gb)
        self.question_te.setEnabled(False)
        self.question_te.setObjectName('question_te')

        domains_val_gb = QtWidgets.QGroupBox(var_tab)

        self.domains_val_te = QtWidgets.QTextEdit(domains_val_gb)
        self.domains_val_te.setEnabled(False)
        self.domains_val_te.setObjectName('domains_var_text')

        self.vars_view = QtWidgets.QTableWidget(var_tab)
        self.vars_view.setObjectName('vars_view')
        self.vars_view.setColumnCount(3)
        self.vars_view.setHorizontalHeaderLabels(['Имя', 'Тип', 'Домен'])
        self.vars_view.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.vars_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tab_panel.addTab(var_tab, '')

        domain_tab = QtWidgets.QWidget()
        domain_tab.setWindowTitle('Домены')

        domain_grid = QtWidgets.QGridLayout()
        domain_tab.setLayout(domain_grid)

        domain_values_gb = QtWidgets.QGroupBox(domain_tab)

        self.domain_values_te = QtWidgets.QTextEdit(domain_values_gb)
        self.domain_values_te.setObjectName('domain_values')

        edit_domain_gb = QtWidgets.QGroupBox(domain_tab)
        edit_domain_gb.setObjectName('edit_domain_gb')

        self.add_domain_button = QtWidgets.QPushButton(edit_domain_gb)
        self.add_domain_button.setObjectName('add_domain_button')

        self.edit_domain_button = QtWidgets.QPushButton(edit_domain_gb)
        self.edit_domain_button.setObjectName('edit_domain_button')

        self.remove_domain_button = QtWidgets.QPushButton(edit_domain_gb)
        self.remove_domain_button.setObjectName('remove_domain_button')

        self.domains_view = QtWidgets.QTableWidget(domain_tab)
        self.domains_view.setObjectName('domains_view')
        self.domains_view.setColumnCount(1)
        self.domains_view.setHorizontalHeaderLabels(['Имя'])
        self.domains_view.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.tab_panel.addTab(domain_tab, '')

        self.consult_button = QtWidgets.QPushButton(self.central_widget)
        self.consult_button.setObjectName('consult_button')

        shell_view.setCentralWidget(self.central_widget)

        self.main_menu = QtWidgets.QMenuBar(shell_view)
        self.main_menu.setGeometry(QtCore.QRect(0, 0, 660, 20))
        self.main_menu.setObjectName('main_menu')

        self.file_actions = QtWidgets.QMenu(self.main_menu)
        self.file_actions.setObjectName('file_actions')
        shell_view.setMenuBar(self.main_menu)

        self.status_bar = QtWidgets.QStatusBar(shell_view)
        self.status_bar.setObjectName('status_bar')
        shell_view.setStatusBar(self.status_bar)

        self.open_file = QtWidgets.QAction(shell_view)
        self.open_file.setObjectName('open_file')

        self.save_file_as = QtWidgets.QAction(shell_view)
        self.save_file_as.setObjectName('save_file_as')

        self.exit = QtWidgets.QAction(shell_view)
        self.exit.setObjectName('exit')

        self.file_actions.addSeparator()
        self.file_actions.addAction(self.open_file)
        self.file_actions.addAction(self.save_file_as)
        self.file_actions.addSeparator()
        self.file_actions.addAction(self.exit)

        self.main_menu.addAction(self.file_actions.menuAction())

        self.tab_panel.setCurrentIndex(0)
        self.retranslate_ui(shell_view)

    def retranslate_ui(self, shell_view):
        _translate = QtCore.QCoreApplication.translate
        shell_view.setWindowTitle(_translate('shell_view', 'Экспертная система'))
        self.add_rule_button.setText(_translate('shell_view', 'Добавить'))
        self.edit_rule_button.setText(_translate('shell_view', 'Изменить'))
        self.remove_rule_button.setText(_translate('shell_view', 'Удалить'))
        self.add_var_button.setText(_translate('shell_view', 'Добавить'))
        self.edit_var_button.setText(_translate('shell_view', 'Изменить'))
        self.remove_var_button.setText(_translate('shell_view', 'Удалить'))
        self.add_domain_button.setText(_translate('shell_view', 'Добавить'))
        self.edit_domain_button.setText(_translate('shell_view', 'Изменить'))
        self.remove_domain_button.setText(_translate('shell_view', 'Удалить'))
        self.consult_button.setText(_translate('shell_view', 'Пройти консультацию'))
        self.file_actions.setTitle(_translate('shell_view', 'Файл'))
        self.open_file.setText(_translate('shell_view', 'Открыть'))
        self.save_file_as.setText(_translate('shell_view', 'Сохранить как'))
        self.exit.setText(_translate('shell_view', 'Выход'))
