from PyQt5 import QtCore, QtGui, QtWidgets
from view.RequisiteEditorWindow import Ui_RequisiteEditorWindow
from view.ConclusionEditorWindow import Ui_ConclusionEditorWindow


class Ui_EditRuleWindow(object):
    def setupUi(self, EditRuleWindow, rule=None):
        EditRuleWindow.setObjectName('EditRuleWindow')
        EditRuleWindow.resize(549, 379)
        EditRuleWindow.setMinimumSize(QtCore.QSize(549, 379))
        EditRuleWindow.setMaximumSize(QtCore.QSize(549, 379))

        self.centralwidget = QtWidgets.QWidget(EditRuleWindow)
        self.centralwidget.setObjectName('centralwidget')

        self.ruleNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.ruleNameLabel.setGeometry(QtCore.QRect(10, 0, 91, 16))
        self.ruleNameLabel.setObjectName('ruleNameLabel')

        self.ruleNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.ruleNameText.setGeometry(QtCore.QRect(10, 20, 531, 20))
        self.ruleNameText.setObjectName('ruleNameText')

        self.requisiteBox = QtWidgets.QGroupBox(self.centralwidget)
        self.requisiteBox.setGeometry(QtCore.QRect(10, 50, 251, 170))
        self.requisiteBox.setObjectName('requisiteBox')

        self.requisiteView = QtWidgets.QTableWidget(self.requisiteBox)
        self.requisiteView.setGeometry(QtCore.QRect(10, 20, 251, 121))
        self.requisiteView.setObjectName('requisiteView')
        self.requisiteView.setColumnCount(2)
        self.requisiteView.setHorizontalHeaderLabels(['Переменная', 'Значение'])
        self.requisiteView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.requisiteView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.addRequisiteButton = QtWidgets.QPushButton(self.requisiteBox)
        self.addRequisiteButton.setGeometry(QtCore.QRect(9, 140, 75, 25))
        self.addRequisiteButton.setObjectName('addRequisiteButton')

        self.editRequisiteButton = QtWidgets.QPushButton(self.requisiteBox)
        self.editRequisiteButton.setGeometry(QtCore.QRect(88, 140, 75, 25))
        self.editRequisiteButton.setObjectName('editRequisiteButton')

        self.delRequisiteButton = QtWidgets.QPushButton(self.requisiteBox)
        self.delRequisiteButton.setGeometry(QtCore.QRect(167, 140, 75, 25))
        self.delRequisiteButton.setObjectName('delRequisiteButton')

        self.conclusionBox = QtWidgets.QGroupBox(self.centralwidget)
        self.conclusionBox.setGeometry(QtCore.QRect(280, 50, 251, 170))
        self.conclusionBox.setObjectName('conclusionBox')

        self.conclusionView = QtWidgets.QTableWidget(self.conclusionBox)
        self.conclusionView.setGeometry(QtCore.QRect(10, 20, 251, 121))
        self.conclusionView.setObjectName('conclusionView')
        self.conclusionView.setColumnCount(2)
        self.conclusionView.setHorizontalHeaderLabels(['Переменная', 'Значение'])
        self.conclusionView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.conclusionView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.addConclusionButton = QtWidgets.QPushButton(self.conclusionBox)
        self.addConclusionButton.setGeometry(QtCore.QRect(9, 140, 75, 25))
        self.addConclusionButton.setObjectName('addConclusionButton')

        self.editConclusionButton = QtWidgets.QPushButton(self.conclusionBox)
        self.editConclusionButton.setGeometry(QtCore.QRect(88, 140, 75, 25))
        self.editConclusionButton.setObjectName('editConclusionButton')

        self.delConclusionButton = QtWidgets.QPushButton(self.conclusionBox)
        self.delConclusionButton.setGeometry(QtCore.QRect(167, 140, 75, 25))
        self.delConclusionButton.setObjectName('delConclusionButton')

        self.descrLabel = QtWidgets.QLabel(self.centralwidget)
        self.descrLabel.setGeometry(QtCore.QRect(10, 250, 61, 16))
        self.descrLabel.setObjectName('descrLabel')

        self.descrText = QtWidgets.QTextEdit(self.centralwidget)
        self.descrText.setGeometry(QtCore.QRect(10, 250, 531, 51))
        self.descrText.setObjectName('descrText')

        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(380, 310, 75, 25))
        self.okButton.setObjectName('okButton')

        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(460, 310, 75, 25))
        self.cancelButton.setObjectName('cancelButton')

        EditRuleWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(EditRuleWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 21))
        self.menubar.setObjectName('menubar')

        EditRuleWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(EditRuleWindow)
        self.statusbar.setObjectName('statusbar')

        EditRuleWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditRuleWindow)
        self.editRuleWindow = EditRuleWindow
        self.expShellMainWindow = EditRuleWindow.prevWindow.es_main_window
        self.connectButtons()
        self.requisiteFacts = []
        self.conclusionFacts = []
        QtCore.QMetaObject.connectSlotsByName(EditRuleWindow)
        self.rule = rule if rule is not None else None
        if self.rule is not None:
            self.fillRule()

    def retranslateUi(self, EditRuleWindow):
        _translate = QtCore.QCoreApplication.translate
        EditRuleWindow.setWindowTitle(_translate('EditRuleWindow', 'Редактирование правила'))
        self.ruleNameLabel.setText(_translate('EditRuleWindow', 'Имя правила:'))
        self.requisiteBox.setTitle(_translate('EditRuleWindow', 'Посылка'))
        self.addRequisiteButton.setText(_translate('EditRuleWindow', 'Добавить'))
        self.editRequisiteButton.setText(_translate('EditRuleWindow', 'Изменить'))
        self.delRequisiteButton.setText(_translate('EditRuleWindow', 'Удалить'))
        self.conclusionBox.setTitle(_translate('EditRuleWindow', 'Заключение'))
        self.addConclusionButton.setText(_translate('EditRuleWindow', 'Добавить'))
        self.editConclusionButton.setText(_translate('EditRuleWindow', 'Изменить'))
        self.delConclusionButton.setText(_translate('EditRuleWindow', 'Удалить'))
        self.descrLabel.setText(_translate('EditRuleWindow', 'Пояснение'))
        self.okButton.setText(_translate('EditRuleWindow', 'OK'))
        self.cancelButton.setText(_translate('EditRuleWindow', 'Отмена'))

    def connectButtons(self):
        self.okButton.clicked.connect(self.okClick)
        self.addRequisiteButton.clicked.connect(self.addRequisite)
        self.addConclusionButton.clicked.connect(self.addConclusion)
        self.editRequisiteButton.clicked.connect(self.editRequisite)
        self.editConclusionButton.clicked.connect(self.editConclusion)
        self.delRequisiteButton.clicked.connect(self.deleteRequisite)
        self.delConclusionButton.clicked.connect(self.deleteConclusion)
        self.cancelButton.clicked.connect(lambda: self.editRuleWindow.close())

    def fillRequisite(self):
        self.requisiteFacts = self.rule.getReasons()
        self.requisiteView.setRowCount(len(self.requisiteFacts))
        i = 0
        for fact in self.requisiteFacts:
            self.requisiteView.setItem(i, 0, QtWidgets.QTableWidgetItem(fact.getVar().getName()))
            self.requisiteView.setItem(i, 1, QtWidgets.QTableWidgetItem(fact.getVal()))
            i += 1
        self.requisiteView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def fillConclusion(self):
        self.conclusionFacts = self.rule.getConclusions()
        self.conclusionView.setRowCount(len(self.conclusionFacts))
        i = 0
        for fact in self.conclusionFacts:
            self.conclusionView.setItem(i, 0, QtWidgets.QTableWidgetItem(fact.getVar().getName()))
            self.conclusionView.setItem(i, 1, QtWidgets.QTableWidgetItem(fact.getVal()))
            i += 1
        self.conclusionView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def fillRule(self):
        self.ruleNameText.setText(self.rule.getName())
        self.fillRequisite()
        self.fillConclusion()
        self.descrText.setText(self.rule.getDescription())

    def addRequisite(self):
        self.addRequisiteWindow = QtWidgets.QMainWindow()
        self.addRequisiteWindow.prevWindow = self
        self.addRequisiteUI = Ui_RequisiteEditorWindow()
        self.addRequisiteUI.setupUi(self.addRequisiteWindow)
        self.addRequisiteWindow.show()

    def addConclusion(self):
        self.addConclusionWindow = QtWidgets.QMainWindow()
        self.addConclusionWindow.prevWindow = self
        self.addConclusionUI = Ui_ConclusionEditorWindow()
        self.addConclusionUI.setupUi(self.addConclusionWindow)
        self.addConclusionWindow.show()

    def editRequisite(self):
        self.addRequisiteWindow = QtWidgets.QMainWindow()
        self.addRequisiteWindow.prevWindow = self
        self.addRequisiteUI = Ui_RequisiteEditorWindow()
        selFactItems = self.requisiteView.selectedItems()
        selFact = self.findRequistedFact(selFactItems[0].text(), selFactItems[1].text()) if selFactItems else None
        self.addRequisiteUI.setupUi(self.addRequisiteWindow, selFact)
        self.addRequisiteWindow.show()

    def editConclusion(self):
        self.addConclusionWindow = QtWidgets.QMainWindow()
        self.addConclusionWindow.prevWindow = self
        self.addConclusionUI = Ui_ConclusionEditorWindow()
        selFactItems = self.conclusionView.selectedItems()
        selFact = self.findConclusionFact(selFactItems[0].text(), selFactItems[1].text()) if selFactItems else None
        self.addConclusionUI.setupUi(self.addConclusionWindow, selFact)
        self.addConclusionWindow.show()

    def deleteRequisite(self):
        selFactItems = self.requisiteView.selectedItems()
        rows = sorted(set(item.row() for item in selFactItems))
        i = 0
        while i < len(selFactItems):
            factToRem = self.findRequistedFact(selFactItems[i].text(), selFactItems[i + 1].text())
            factToRem.getVar().deleteFact(factToRem)
            self.requisiteFacts.remove(factToRem)
            i += 2
        for row_index in reversed(rows):
            self.requisiteView.removeRow(row_index)

    def deleteConclusion(self):
        selFactItems = self.conclusionView.selectedItems()
        rows = sorted(set(item.row() for item in selFactItems))
        i = 0
        while i < len(selFactItems):
            factToRem = self.findConclusionFact(selFactItems[i].text(), selFactItems[i + 1].text())
            factToRem.getVar().deleteFact(factToRem)
            self.conclusionFacts.remove(factToRem)
            i += 2
        for row_index in reversed(rows):
            self.conclusionView.removeRow(row_index)

    def onRequisiteChanged(self):
        self.requisiteView.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.requisiteView.clear()
        self.requisiteView.setColumnCount(2)
        self.requisiteView.setHorizontalHeaderLabels(['Переменная', 'Значение'])
        self.requisiteView.setRowCount(len(self.requisiteFacts))
        i = 0
        for fact in self.requisiteFacts:
            self.requisiteView.setItem(i, 0, QtWidgets.QTableWidgetItem(fact.getVar().getName()))
            self.requisiteView.setItem(i, 1, QtWidgets.QTableWidgetItem(fact.getVal()))
            i += 1
        self.requisiteView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def onConclusionChanged(self):
        self.conclusionView.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.conclusionView.clear()
        self.conclusionView.setColumnCount(2)
        self.conclusionView.setHorizontalHeaderLabels(['Переменная', 'Значение'])
        self.conclusionView.setRowCount(len(self.conclusionFacts))
        i = 0
        for fact in self.conclusionFacts:
            self.conclusionView.setItem(i, 0, QtWidgets.QTableWidgetItem(fact.getVar().getName()))
            self.conclusionView.setItem(i, 1, QtWidgets.QTableWidgetItem(fact.getVal()))
            i += 1
        self.conclusionView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def okClick(self):
        expSys = self.editRuleWindow.prevWindow.es_main_window.expertSystem
        if self.ruleNameText.text() == '':
            error = QtWidgets.QErrorMessage(self.editRuleWindow)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Необходимо указать имя')
            return False
        if expSys.getRuleByName(self.ruleNameText.text()):
            if self.rule is not None and self.rule.getName() != self.ruleNameText.text() or self.rule is None:
                error = QtWidgets.QErrorMessage(self.editRuleWindow)
                error.setWindowTitle('Ошибка!')
                error.showMessage('Данное имя уже используется')
                return False
        if self.rule is not None:
            self.rule.setName(self.ruleNameText.text())
            self.rule.setDescription(self.descrText.toPlainText())
            self.rule.setReasons(self.requisiteFacts)
            self.rule.setConclusions(self.conclusionFacts)
        else:
            expSys.insertRule(self.ruleNameText.text(),
                              self.descrText.toPlainText(),
                              self.requisiteFacts,
                              self.conclusionFacts,
                              self.editRuleWindow.selIndex)
        expSys.updateDicts()
        self.editRuleWindow.prevWindow.onRulesChange()
        self.editRuleWindow.close()

    def findRequistedFact(self, var, val):
        for fact in self.requisiteFacts:
            if fact.getVal() == val and fact.getVar().getName() == var:
                return fact

    def findConclusionFact(self, var, val):
        for fact in self.conclusionFacts:
            if fact.getVal() == val and fact.getVar().getName() == var:
                return fact


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditRuleWindow = QtWidgets.QMainWindow()
    ui = Ui_EditRuleWindow()
    ui.setupUi(EditRuleWindow)
    EditRuleWindow.show()
    sys.exit(app.exec_())
