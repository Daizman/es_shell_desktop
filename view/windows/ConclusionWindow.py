from PyQt5 import QtCore, QtGui, QtWidgets


class UIConclusionWindow(object):
    def setup_ui(self, conclusion_view):
        conclusion_view.setObjectName('conclusion_view')
        conclusion_view.resize(360, 180)
        self.central_widget = QtWidgets.QWidget(conclusion_view)
        self.central_widget.setObjectName('central_widget')

        self.add_button = QtWidgets.QPushButton(self.central_widget)
        self.add_button.setGeometry(QtCore.QRect(310, 10, 40, 25))
        self.add_button.setObjectName('add_button')

        self.combo = QtWidgets.QComboBox(self.central_widget)
        self.combo.setGeometry(QtCore.QRect(10, 10, 300, 20))
        self.combo.setObjectName('combo')

        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setGeometry(QtCore.QRect(10, 90, 340, 15))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName('line')

        self.eq_label = QtWidgets.QLabel(self.central_widget)
        self.eq_label.setGeometry(QtCore.QRect(180, 40, 15, 15))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eq_label.setFont(font)
        self.eq_label.setObjectName('eq_label')

        self.cancel_button = QtWidgets.QPushButton(self.central_widget)
        self.cancel_button.setGeometry(QtCore.QRect(270, 110, 75, 25))
        self.cancel_button.setObjectName('cancel_button')

        self.ok_button = QtWidgets.QPushButton(self.central_widget)
        self.ok_button.setGeometry(QtCore.QRect(190, 110, 75, 25))
        self.ok_button.setObjectName('ok_button')

        self.value_combo = QtWidgets.QComboBox(self.central_widget)
        self.value_combo.setGeometry(QtCore.QRect(10, 60, 340, 20))
        self.value_combo.setObjectName('value_combo')

        conclusion_view.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(conclusion_view)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 360, 20))
        self.menu_bar.setObjectName('menu_bar')
        conclusion_view.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(conclusion_view)
        self.status_bar.setObjectName('status_bar')
        conclusion_view.setStatusBar(self.status_bar)

        self.retranslate_ui(conclusion_view)
        QtCore.QMetaObject.connectSlotsByName(conclusion_view)

    def retranslate_ui(self, conclusion_view):
        _translate = QtCore.QCoreApplication.translate
        conclusion_view.setWindowTitle(_translate('conclusion_view', 'Факт заключения'))
        self.add_button.setText(_translate('conclusion_view', '+'))
        self.eq_label.setText(_translate('conclusion_view', '='))
        self.cancel_button.setText(_translate('conclusion_view', 'Отмена'))
        self.ok_button.setText(_translate('conclusion_view', 'OK'))

    def connectButtons(self):
        self.ok_button.clicked.connect(self.okClick)
        self.add_button.clicked.connect(self.addVar)
        self.combo.currentTextChanged.connect(self.onSelectVar)
        self.cancel_button.clicked.connect(lambda: self.conclusionEditorWindow.close())

    def fillConclusion(self):
        varIdx = self.combo.findText(self.conclusion.getVar().getName())
        self.combo.setCurrentIndex(varIdx)
        valIdx = self.value_combo.findText(self.conclusion.getVal())
        self.value_combo.setCurrentIndex(valIdx)

    def addVar(self):
        self.addVarWindow = QtWidgets.QMainWindow()
        self.addVarUI = Ui_EditVarWindow()
        self.addVarWindow.prevWindow = self
        self.addVarUI.setup_ui(self.addVarWindow)
        self.addVarWindow.show()

    def onSelectVar(self):
        self.fillValues()

    def onVarsChange(self):
        self.conclusionEditorWindow.prevWindow.editRuleWindow.prevWindow.on_vars_change()
        self.fillVars()
        self.combo.setCurrentIndex(self.combo.count() - 1)

    def ondomainsChange(self):
        self.conclusionEditorWindow.prevWindow.editRuleWindow.prevWindow.on_domains_change()
        self.fillVars()
        self.combo.setCurrentIndex(self.combo.count() - 1)

    def fillVars(self):
        self.combo.clear()
        esVars = self.expShellMainWindow.expertSystem.getVariables()
        for var in esVars:
            if var.getVarType() != VarType.REQUESTED:
                self.combo.addItem(var.getName())

    def fillValues(self):
        self.value_combo.clear()
        var = self.combo.currentText()
        if var == '':
            return False
        vals = self.expShellMainWindow.expertSystem.getVariableByName(var).getdomain().getValues()
        for val in vals:
            self.value_combo.addItem(val)

    def okClick(self):
        expSys = self.conclusionEditorWindow.prevWindow.es_main_window.expertSystem
        if self.combo.currentText() == '':
            error = QtWidgets.QErrorMessage(self.conclusionEditorWindow)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Необходимо указать переменную')
            return False
        var = expSys.getVariableByName(self.combo.currentText())
        val = self.value_combo.currentText()
        if self.conclusion is not None:
            self.conclusion.setVar(var)
            self.conclusion.setVal(val)
        else:
            self.conclusionEditorWindow.prevWindow.conclusionFacts.append(Fact(var, val))
        self.conclusionEditorWindow.prevWindow.onConclusionChanged()
        self.conclusionEditorWindow.close()

