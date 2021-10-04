from PyQt5 import QtCore, QtWidgets

from view.pyqt5_exten.TableWidgetDragRows import TableWidgetDragRows


class UIShellWindow(object):
    def setup_ui(self, shell_view):
        shell_view.setObjectName('shell_view')
        shell_view.resize(660, 525)

        self.central_widget = QtWidgets.QWidget(shell_view)
        self.central_widget.setObjectName('central_widget')

        v_layout = QtWidgets.QVBoxLayout()
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addLayout(v_layout)
        self.central_widget.setLayout(h_layout)

        self.tabs = QtWidgets.QTabWidget(self.central_widget)
        self.tabs.setEnabled(True)
        self.tabs.setObjectName('tabs')
        self.tabs.addTab(self._gen_rule_tab(), 'Правила')
        self.tabs.addTab(self._gen_var_tab(), 'Переменные')
        self.tabs.addTab(self._gen_domain_tab(), 'Домены')

        shell_view.setCentralWidget(self.central_widget)
        self._gen_menu(shell_view)

        self.tabs.setCurrentIndex(0)
        h_layout.addWidget(self.tabs)
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
        self.actions.setTitle(_translate('shell_view', 'Меню'))

        for i, name in enumerate(['Пройти консультацию', 'Открыть', 'Сохранить как', 'Выход']):
            shell_view.findChild(QtWidgets.QAction, self.actions.in_action_names[i]).setText(_translate('shell_view', name))

    def _gen_menu(self, shell_view):
        self.main_menu = QtWidgets.QMenuBar(shell_view)
        self.main_menu.setObjectName('main_menu')
        shell_view.setMenuBar(self.main_menu)
        self.actions = QtWidgets.QMenu(self.main_menu)
        self.actions.setObjectName('actions')
        self.actions.in_action_names = ['consult', 'open_file', 'save_file_as', 'exit']

        for act in self.actions.in_action_names:
            self.actions.addSeparator()
            self.actions.addAction(self._gen_action(shell_view, act))

        self.main_menu.addAction(self.actions.menuAction())

    def _gen_action(self, shell_view, action_name):
        action = QtWidgets.QAction(shell_view)
        action.setObjectName(action_name)
        return action

    def _gen_rule_tab(self):
        rule_tab, layout, edit_rules_gb, buttons_layout = self._gen_tab_template()

        self.add_rule_button = QtWidgets.QPushButton(edit_rules_gb)
        self.edit_rule_button = QtWidgets.QPushButton(edit_rules_gb)
        self.remove_rule_button = QtWidgets.QPushButton(edit_rules_gb)
        buttons_layout.addWidget(self.add_rule_button)
        buttons_layout.addWidget(self.edit_rule_button)
        buttons_layout.addWidget(self.remove_rule_button)

        self.requisite_te, req_gb = self._create_gb(
            rule_tab, 'requisite_te'
        )
        req_gb.setTitle('Посылка')

        self.conclusion_te, conc_gb = self._create_gb(
            rule_tab, 'conclusion_te'
        )
        conc_gb.setTitle('Заключение')

        self.rules_view = TableWidgetDragRows(rule_tab)
        self._setup_view(self.rules_view, ['Имя', 'Описание'])

        layout.addWidget(self.rules_view, 0, 0, 15, 4)
        layout.addWidget(req_gb, 2, 4, 7, 1)
        layout.addWidget(conc_gb, 9, 4, 6, 1)

        return rule_tab

    def _gen_var_tab(self):
        var_tab, layout, edit_var_gb, buttons_layout = self._gen_tab_template()

        self.add_var_button = QtWidgets.QPushButton(edit_var_gb)
        self.edit_var_button = QtWidgets.QPushButton(edit_var_gb)
        self.remove_var_button = QtWidgets.QPushButton(edit_var_gb)
        buttons_layout.addWidget(self.add_var_button)
        buttons_layout.addWidget(self.edit_var_button)
        buttons_layout.addWidget(self.remove_var_button)

        self.question_te, question_gb = self._create_gb(
            var_tab, 'question_te'
        )
        question_gb.setTitle('Вопрос')

        self.var_values_te, var_values_gb = self._create_gb(
            var_tab, 'var_values_te'
        )
        var_values_gb.setTitle('Значения')

        self.vars_view = QtWidgets.QTableWidget(var_tab)
        self._setup_view(self.vars_view, ['Имя', 'Тип', 'Домен'])

        layout.addWidget(self.vars_view, 0, 0, 15, 4)
        layout.addWidget(question_gb, 2, 4, 7, 1)
        layout.addWidget(var_values_gb, 9, 4, 6, 1)

        return var_tab

    def _gen_domain_tab(self):
        domain_tab, layout, edit_domain_gb, buttons_layout = self._gen_tab_template()

        self.add_domain_button = QtWidgets.QPushButton(edit_domain_gb)
        self.edit_domain_button = QtWidgets.QPushButton(edit_domain_gb)
        self.remove_domain_button = QtWidgets.QPushButton(edit_domain_gb)
        buttons_layout.addWidget(self.add_domain_button)
        buttons_layout.addWidget(self.edit_domain_button)
        buttons_layout.addWidget(self.remove_domain_button)

        self.domain_values_te, domain_values_gb = self._create_gb(
            domain_tab, 'dom_values_te'
        )
        domain_values_gb.setTitle('Значения')

        self.domains_view = QtWidgets.QTableWidget(domain_tab)
        self._setup_view(self.domains_view, ['Имя'])

        layout.addWidget(self.domains_view, 0, 0, 15, 4)
        layout.addWidget(domain_values_gb, 2, 4, 13, 1)

        return domain_tab

    def _create_gb(self, tab, name):
        gb = QtWidgets.QGroupBox(tab)
        te = QtWidgets.QTextEdit(gb)
        te.textChanged.connect(te.undo)
        te.setObjectName(name)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(te)
        gb.setLayout(layout)
        gb.setMaximumWidth(200)

        return te, gb

    def _setup_view(self, view, cols):
        view.setColumnCount(len(cols))
        view.setHorizontalHeaderLabels(cols)
        view.horizontalHeader().setSectionResizeMode(len(cols) - 1, QtWidgets.QHeaderView.Stretch)
        view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def _gen_tab_template(self):
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        gb = QtWidgets.QGroupBox(tab)
        buttons_layout = QtWidgets.QVBoxLayout()
        gb.setLayout(buttons_layout)
        gb.setTitle('Редактирование')
        layout.addWidget(gb, 0, 4, 2, 1)
        tab.setLayout(layout)

        return tab, layout, gb, buttons_layout
