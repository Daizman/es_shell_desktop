from PyQt5 import QtCore, QtWidgets

from view.pyqt5_exten.TableWidgetDragRows import TableWidgetDragRows


class UIMainWindow(object):
    def setup_ui(self, shell_view):
        shell_view.setObjectName('shell_view')
        shell_view.resize(660, 525)

        self.central_widget = QtWidgets.QWidget(shell_view)
        self.central_widget.setObjectName('central_widget')

        self.tab_panel = QtWidgets.QTabWidget(self.central_widget)
        self.tab_panel.setEnabled(True)
        self.tab_panel.setGeometry(QtCore.QRect(0, 0, 660, 460))

        self.tab_panel.setObjectName('tab_panel')

        self.rule_tab = QtWidgets.QWidget()
        self.rule_tab.setObjectName('rule_tab')

        self.edit_rules_gb = QtWidgets.QGroupBox(self.rule_tab)
        self.edit_rules_gb.setGeometry(QtCore.QRect(460, 0, 190, 90))
        self.edit_rules_gb.setObjectName('edit_rules_gb')

        self.add_rule_button = QtWidgets.QPushButton(self.edit_rules_gb)
        self.add_rule_button.setGeometry(QtCore.QRect(5, 15, 180, 25))
        self.add_rule_button.setObjectName('add_rule_button')

        self.edit_rule_button = QtWidgets.QPushButton(self.edit_rules_gb)
        self.edit_rule_button.setGeometry(QtCore.QRect(5, 40, 180, 25))
        self.edit_rule_button.setObjectName('edit_rule_button')

        self.del_rule_button = QtWidgets.QPushButton(self.edit_rules_gb)
        self.del_rule_button.setGeometry(QtCore.QRect(5, 65, 180, 25))
        self.del_rule_button.setObjectName('del_rule_button')

        self.requisite_box = QtWidgets.QGroupBox(self.rule_tab)
        self.requisite_box.setGeometry(QtCore.QRect(460, 100, 190, 160))
        self.requisite_box.setObjectName('requisite_box')

        self.requisite_text = QtWidgets.QTextEdit(self.requisite_box)
        self.requisite_text.setEnabled(False)
        self.requisite_text.setGeometry(QtCore.QRect(10, 20, 170, 130))
        self.requisite_text.setObjectName('requisite_text')

        self.conclusion_box = QtWidgets.QGroupBox(self.rule_tab)
        self.conclusion_box.setGeometry(QtCore.QRect(460, 270, 190, 160))
        self.conclusion_box.setObjectName('conclusion_box')

        self.conclusion_text = QtWidgets.QTextEdit(self.conclusion_box)
        self.conclusion_text.setEnabled(False)
        self.conclusion_text.setGeometry(QtCore.QRect(10, 20, 170, 130))
        self.conclusion_text.setObjectName('conclusion_text')

        self.rules_view = TableWidgetDragRows(self.rule_tab, drop_event_callback=shell_view.drop_rule_cb)
        self.rules_view.setGeometry(QtCore.QRect(0, 0, 460, 430))
        self.rules_view.setObjectName('rules_view')
        self.rules_view.setColumnCount(2)
        self.rules_view.setHorizontalHeaderLabels(['Имя', 'Описание'])
        self.rules_view.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.rules_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tab_panel.addTab(self.rule_tab, '')

        self.var_tab = QtWidgets.QWidget()
        self.var_tab.setObjectName('var_tab')

        self.edit_var_gb = QtWidgets.QGroupBox(self.var_tab)
        self.edit_var_gb.setGeometry(QtCore.QRect(460, 0, 190, 90))
        self.edit_var_gb.setObjectName('edit_var_gb')

        self.add_var_button = QtWidgets.QPushButton(self.edit_var_gb)
        self.add_var_button.setGeometry(QtCore.QRect(5, 15, 180, 25))
        self.add_var_button.setObjectName('add_var_button')

        self.edit_var_button = QtWidgets.QPushButton(self.edit_var_gb)
        self.edit_var_button.setGeometry(QtCore.QRect(5, 40, 180, 25))
        self.edit_var_button.setObjectName('edit_var_button')

        self.del_var_button = QtWidgets.QPushButton(self.edit_var_gb)
        self.del_var_button.setGeometry(QtCore.QRect(5, 65, 180, 25))
        self.del_var_button.setObjectName('del_var_button')

        self.question_tb = QtWidgets.QGroupBox(self.var_tab)
        self.question_tb.setGeometry(QtCore.QRect(460, 100, 190, 160))
        self.question_tb.setObjectName('question_tb')

        self.question_text = QtWidgets.QTextEdit(self.question_tb)
        self.question_text.setEnabled(False)
        self.question_text.setGeometry(QtCore.QRect(10, 20, 170, 130))
        self.question_text.setObjectName('question_text')

        self.domains_var_box = QtWidgets.QGroupBox(self.var_tab)
        self.domains_var_box.setGeometry(QtCore.QRect(460, 270, 190, 160))
        self.domains_var_box.setObjectName('domains_var_box')

        self.domains_var_text = QtWidgets.QTextEdit(self.domains_var_box)
        self.domains_var_text.setEnabled(False)
        self.domains_var_text.setGeometry(QtCore.QRect(10, 20, 170, 130))
        self.domains_var_text.setObjectName('domains_var_text')

        self.vars_view = QtWidgets.QTableWidget(self.var_tab)
        self.vars_view.setGeometry(QtCore.QRect(0, 0, 460, 430))
        self.vars_view.setObjectName('vars_view')
        self.vars_view.setColumnCount(3)
        self.vars_view.setHorizontalHeaderLabels(['Имя', 'Тип', 'Домен'])
        self.vars_view.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.vars_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tab_panel.addTab(self.var_tab, '')

        self.domain_tab = QtWidgets.QWidget()
        self.domain_tab.setObjectName('domain_tab')

        self.domain_values_box = QtWidgets.QGroupBox(self.domain_tab)
        self.domain_values_box.setGeometry(QtCore.QRect(460, 100, 190, 330))
        self.domain_values_box.setObjectName('domain_values_box')

        self.domain_values = QtWidgets.QTextEdit(self.domain_values_box)
        self.domain_values.textChanged.connect(self.domain_values.undo)
        self.domain_values.setGeometry(QtCore.QRect(10, 20, 170, 300))
        self.domain_values.setObjectName('domain_values')

        self.edit_domain_gb = QtWidgets.QGroupBox(self.domain_tab)
        self.edit_domain_gb.setGeometry(QtCore.QRect(460, 0, 190, 90))
        self.edit_domain_gb.setObjectName('edit_domain_gb')

        self.add_domain_button = QtWidgets.QPushButton(self.edit_domain_gb)
        self.add_domain_button.setGeometry(QtCore.QRect(5, 15, 180, 25))
        self.add_domain_button.setObjectName('add_domain_button')

        self.edit_domain_button = QtWidgets.QPushButton(self.edit_domain_gb)
        self.edit_domain_button.setGeometry(QtCore.QRect(5, 40, 180, 25))
        self.edit_domain_button.setObjectName('edit_domain_button')

        self.del_domain_button = QtWidgets.QPushButton(self.edit_domain_gb)
        self.del_domain_button.setGeometry(QtCore.QRect(5, 65, 180, 25))
        self.del_domain_button.setObjectName('del_domain_button')

        self.domains_view = QtWidgets.QTableWidget(self.domain_tab)
        self.domains_view.setGeometry(QtCore.QRect(0, 0, 460, 430))
        self.domains_view.setObjectName('domains_view')
        self.domains_view.setColumnCount(1)
        self.domains_view.setHorizontalHeaderLabels(['Имя'])
        self.domains_view.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.tab_panel.addTab(self.domain_tab, '')

        self.consult_button = QtWidgets.QPushButton(self.central_widget)
        self.consult_button.setGeometry(QtCore.QRect(0, 460, 650, 25))
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
        QtCore.QMetaObject.connectSlotsByName(shell_view)

        self.retranslate_ui(shell_view)

    def retranslate_ui(self, shell_view):
        _translate = QtCore.QCoreApplication.translate
        shell_view.setWindowTitle(_translate('shell_view', 'Экспертная система'))
        self.edit_rules_gb.setTitle(_translate('shell_view', 'Редактирование'))
        self.add_rule_button.setText(_translate('shell_view', 'Добавить'))
        self.edit_rule_button.setText(_translate('shell_view', 'Изменить'))
        self.del_rule_button.setText(_translate('shell_view', 'Удалить'))
        self.requisite_box.setTitle(_translate('shell_view', 'Посылка'))
        self.conclusion_box.setTitle(_translate('shell_view', 'Заключение'))
        self.tab_panel.setTabText(self.tab_panel.indexOf(self.rule_tab), _translate('shell_view', 'Правила'))
        self.edit_var_gb.setTitle(_translate('shell_view', 'Редактирование'))
        self.add_var_button.setText(_translate('shell_view', 'Добавить'))
        self.edit_var_button.setText(_translate('shell_view', 'Изменить'))
        self.del_var_button.setText(_translate('shell_view', 'Удалить'))
        self.question_tb.setTitle(_translate('shell_view', 'Вопрос'))
        self.domains_var_box.setTitle(_translate('shell_view', 'Значения'))
        self.tab_panel.setTabText(self.tab_panel.indexOf(self.var_tab), _translate('shell_view', 'Переменные'))
        self.domain_values_box.setTitle(_translate('shell_view', 'Значения домена'))
        self.edit_domain_gb.setTitle(_translate('shell_view', 'Редактирование'))
        self.add_domain_button.setText(_translate('shell_view', 'Добавить'))
        self.edit_domain_button.setText(_translate('shell_view', 'Изменить'))
        self.del_domain_button.setText(_translate('shell_view', 'Удалить'))
        self.tab_panel.setTabText(self.tab_panel.indexOf(self.domain_tab), _translate('shell_view', 'Домены'))
        self.consult_button.setText(_translate('shell_view', 'Пройти консультацию'))
        self.file_actions.setTitle(_translate('shell_view', 'Файл'))
        self.open_file.setText(_translate('shell_view', 'Открыть'))
        self.save_file_as.setText(_translate('shell_view', 'Сохранить как'))
        self.exit.setText(_translate('shell_view', 'Выход'))

    def openConsultWindow(self):
        self.consultWindow = QtWidgets.QMainWindow()
        self.consultUI = Ui_ConsultWindow()
        self.consultWindow.prevWindow = self
        self.consultUI.setupUi(self.consultWindow)
        self.consultWindow.show()

    # работа с правилами
    def openAddRuleWindow(self):
        self.addRuleWindow = QtWidgets.QMainWindow()
        self.addRuleUI = Ui_EditRuleWindow()
        selIt = self.rules_view.selectedItems()
        self.addRuleWindow.selIndex = self.shell_view.expertSystem.getRuleIndex(selIt[0].text()) + 1 if selIt \
            else len(self.shell_view.expertSystem.getRules())
        self.addRuleWindow.prevWindow = self
        self.addRuleUI.setupUi(self.addRuleWindow)
        self.addRuleWindow.show()

    def onRulesChange(self):
        rules = self.shell_view.expertSystem.getRules()
        self.rules_view.clear()
        self.rules_view.cellClicked.connect(self.onRuleSelect)
        self.rules_view.setColumnCount(2)
        self.rules_view.setHorizontalHeaderLabels(['Имя', 'Описание'])
        self.rules_view.setRowCount(len(rules))
        i = 0
        for rule in reversed(rules):
            rName = QtWidgets.QTableWidgetItem(rule.getName())
            rName.setToolTip(rule.getName())
            self.rules_view.setItem(i, 0, rName)
            descr = rule.getDescription() if rule.getDescription() != '' else str(rule)
            ruleItem = QtWidgets.QTableWidgetItem(descr)
            ruleItem.setToolTip(str(rule))
            self.rules_view.setItem(i, 1, ruleItem)
            i += 1

    def onRuleSelect(self):
        self.conclusion_text.clear()
        self.requisite_text.clear()
        selRule = self.shell_view.expertSystem.getRuleByName(self.rules_view.selectedItems()[0].text())
        if selRule:
            self.requisite_text.setText(', '.join([str(fact) for fact in selRule.getReasons()]))
            self.conclusion_text.setText(', '.join([str(fact) for fact in selRule.getConclusions()]))

    def openEditRuleWindow(self):
        self.addRuleWindow = QtWidgets.QMainWindow()
        self.addRuleUI = Ui_EditRuleWindow()
        self.addRuleWindow.prevWindow = self
        selRuleItems = self.rules_view.selectedItems()
        selRule = None
        self.requisite_text.clear()
        self.conclusion_text.clear()
        if len(selRuleItems) > 0:
            selRule = self.shell_view.expertSystem.getRuleByName(self.rules_view.selectedItems()[0].text())
        self.addRuleUI.setupUi(self.addRuleWindow, selRule)
        self.addRuleWindow.show()

    def delRule(self):
        if len(self.rules_view.selectedItems()) == 0:
            error = QtWidgets.QErrorMessage(self.shell_view)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Нужно выбрать правило')
            return False
        self.shell_view.expertSystem.deleteRule(self.rules_view.selectedItems()[0].text())
        self.conclusion_text.clear()
        self.requisite_text.clear()
        self.onRulesChange()

    # работа с переменными
    def openAddVarWindow(self):
        self.addVarWindow = QtWidgets.QMainWindow()
        self.addVarUI = Ui_EditVarWindow()
        self.addVarWindow.prevWindow = self
        self.addVarUI.setupUi(self.addVarWindow)
        self.addVarWindow.show()

    def onVarsChange(self):
        esVars = self.shell_view.expertSystem.getVariables()
        self.vars_view.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.vars_view.clear()
        self.vars_view.cellClicked.connect(self.onVarSelect)
        self.vars_view.setColumnCount(3)
        self.vars_view.setHorizontalHeaderLabels(['Имя', 'Тип', 'Домен'])
        self.vars_view.setRowCount(len(esVars))
        i = 0
        for var in esVars:
            self.vars_view.setItem(i, 0, QtWidgets.QTableWidgetItem(var.getName()))
            typeItem = QtWidgets.QTableWidgetItem(var.getVarTypeText())
            typeItem.setToolTip(var.getVarTypeText())
            self.vars_view.setItem(i, 1, typeItem)
            domItem = QtWidgets.QTableWidgetItem(var.getDomen().getName())
            domItem.setToolTip(str(var.getDomen()))
            self.vars_view.setItem(i, 2, domItem)
            i += 1
        self.vars_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def onVarSelect(self):
        self.question_text.clear()
        self.domains_var_text.clear()
        selVar = self.shell_view.expertSystem.getVariableByName(self.vars_view.selectedItems()[0].text())
        if selVar:
            self.question_text.setText(selVar.getQuestion())
            self.domains_var_text.setText(';\n'.join(selVar.getDomen().getValues()))

    def openEditVarWindow(self):
        self.addVarWindow = QtWidgets.QMainWindow()
        self.addVarUI = Ui_EditVarWindow()
        self.addVarWindow.prevWindow = self
        selVarItems = self.vars_view.selectedItems()
        selVar = None
        self.question_text.clear()
        if len(selVarItems) > 0:
            selVar = self.shell_view.expertSystem.getVariableByName(self.vars_view.selectedItems()[0].text())
        self.addVarUI.setupUi(self.addVarWindow, selVar)
        self.addVarWindow.show()

    def delVar(self):
        if len(self.vars_view.selectedItems()) == 0:
            error = QtWidgets.QErrorMessage(self.shell_view)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Нужно выбрать переменную')
            return False
        try:
            self.shell_view.expertSystem.deleteVariable(self.vars_view.selectedItems()[0].text())
            self.question_text.clear()
            self.onVarsChange()
        except Exception as e:
            error = QtWidgets.QErrorMessage(self.shell_view)
            error.setWindowTitle('Ошибка!')
            error.showMessage(str(e))

    # работа с доменами
    def openAddDomenWindow(self):
        self.addDomenWindow = QtWidgets.QMainWindow()
        self.addDomenWindow.prevWindow = self
        self.addDomenUI = Ui_DomenEditorWindow()
        self.addDomenUI.setupUi(self.addDomenWindow)
        self.addDomenWindow.show()

    def onDomensChange(self):
        domens = self.shell_view.expertSystem.getDomens()
        self.domains_view.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.domains_view.clear()
        self.domains_view.setColumnCount(1)
        self.domains_view.cellClicked.connect(self.onDomenSelect)
        self.domains_view.setHorizontalHeaderLabels(['Имя'])
        self.domains_view.setRowCount(len(domens))
        i = 0
        for dom in domens:
            self.domains_view.setItem(i, 0, QtWidgets.QTableWidgetItem(dom.getName()))
            i += 1
        self.domains_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def onDomenSelect(self):
        self.domain_values.clear()
        selDomName = self.domains_view.selectedItems()[0].text()
        selDom = self.shell_view.expertSystem.getDomenByName(selDomName)
        if selDom:
            self.domain_values.setText(',\n'.join(selDom.getValues()))

    def openEditDomenWindow(self):
        self.addDomenWindow = QtWidgets.QMainWindow()
        self.addDomenWindow.prevWindow = self
        self.addDomenUI = Ui_DomenEditorWindow()
        selDomItems = self.domains_view.selectedItems()
        selDom = None
        self.domain_values.clear()
        if len(selDomItems) > 0:
            selDom = self.shell_view.expertSystem.getDomenByName(self.domains_view.selectedItems()[0].text())
        self.addDomenUI.setupUi(self.addDomenWindow, selDom)
        self.addDomenWindow.show()

    def delDomen(self):
        if len(self.domain_values.selectedItems()) == 0:
            error = QtWidgets.QErrorMessage(self.shell_view)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Нужно выбрать домен')
            return False
        try:
            self.shell_view.expertSystem.deleteDomen(self.domains_view.selectedItems()[0].text())
            self.domain_values.clear()
            self.onDomensChange()
        except Exception as e:
            error = QtWidgets.QErrorMessage(self.shell_view)
            error.setWindowTitle('Ошибка!')
            error.showMessage(str(e))
