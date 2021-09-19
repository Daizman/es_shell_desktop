from PyQt5 import QtCore, QtGui, QtWidgets
from view.windows.VarWindow import Ui_EditVarWindow
from models.Fact import Fact
from models.VarType import VarType


class Ui_ConclusionEditorWindow(object):
    def setupUi(self, ConclusionEditorWindow, conclusion=None):
        ConclusionEditorWindow.setObjectName('ConclusionEditorWindow')
        ConclusionEditorWindow.resize(358, 177)
        self.centralwidget = QtWidgets.QWidget(ConclusionEditorWindow)
        self.centralwidget.setObjectName('central_widget')
        self.conclusionAddButton = QtWidgets.QPushButton(self.centralwidget)
        self.conclusionAddButton.setGeometry(QtCore.QRect(310, 9, 41, 24))
        self.conclusionAddButton.setObjectName('conclusionAddButton')
        self.conclusionCombo = QtWidgets.QComboBox(self.centralwidget)
        self.conclusionCombo.setGeometry(QtCore.QRect(10, 10, 301, 22))
        self.conclusionCombo.setObjectName('conclusionCombo')
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 90, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName('line')
        self.eqLabel = QtWidgets.QLabel(self.centralwidget)
        self.eqLabel.setGeometry(QtCore.QRect(180, 40, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eqLabel.setFont(font)
        self.eqLabel.setObjectName('eqLabel')
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(270, 110, 75, 25))
        self.cancelButton.setObjectName('cancel_button')
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(190, 110, 75, 25))
        self.okButton.setObjectName('ok_button')
        self.conclusionValueCombo = QtWidgets.QComboBox(self.centralwidget)
        self.conclusionValueCombo.setGeometry(QtCore.QRect(10, 60, 341, 22))
        self.conclusionValueCombo.setObjectName('conclusionValueCombo')
        ConclusionEditorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConclusionEditorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 358, 21))
        self.menubar.setObjectName('menu_bar')
        ConclusionEditorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConclusionEditorWindow)
        self.statusbar.setObjectName('status_bar')
        ConclusionEditorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConclusionEditorWindow)
        self.expShellMainWindow = ConclusionEditorWindow.prevWindow.es_main_window
        self.conclusionEditorWindow = ConclusionEditorWindow
        self.connectButtons()
        self.fillVars()
        self.conclusion = conclusion if conclusion is not None else None
        if self.conclusion is not None:
            self.fillConclusion()
        QtCore.QMetaObject.connectSlotsByName(ConclusionEditorWindow)

    def retranslateUi(self, ConclusionEditorWindow):
        _translate = QtCore.QCoreApplication.translate
        ConclusionEditorWindow.setWindowTitle(_translate('ConclusionEditorWindow', 'Факт заключения'))
        self.conclusionAddButton.setText(_translate('ConclusionEditorWindow', '+'))
        self.eqLabel.setText(_translate('ConclusionEditorWindow', '='))
        self.cancelButton.setText(_translate('ConclusionEditorWindow', 'Отмена'))
        self.okButton.setText(_translate('ConclusionEditorWindow', 'OK'))

    def connectButtons(self):
        self.okButton.clicked.connect(self.okClick)
        self.conclusionAddButton.clicked.connect(self.addVar)
        self.conclusionCombo.currentTextChanged.connect(self.onSelectVar)
        self.cancelButton.clicked.connect(lambda: self.conclusionEditorWindow.close())

    def fillConclusion(self):
        varIdx = self.conclusionCombo.findText(self.conclusion.getVar().getName())
        self.conclusionCombo.setCurrentIndex(varIdx)
        valIdx = self.conclusionValueCombo.findText(self.conclusion.getVal())
        self.conclusionValueCombo.setCurrentIndex(valIdx)

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
        self.conclusionCombo.setCurrentIndex(self.conclusionCombo.count() - 1)

    def onDomensChange(self):
        self.conclusionEditorWindow.prevWindow.editRuleWindow.prevWindow.on_domains_change()
        self.fillVars()
        self.conclusionCombo.setCurrentIndex(self.conclusionCombo.count() - 1)

    def fillVars(self):
        self.conclusionCombo.clear()
        esVars = self.expShellMainWindow.expertSystem.getVariables()
        for var in esVars:
            if var.getVarType() != VarType.REQUESTED:
                self.conclusionCombo.addItem(var.getName())

    def fillValues(self):
        self.conclusionValueCombo.clear()
        var = self.conclusionCombo.currentText()
        if var == '':
            return False
        vals = self.expShellMainWindow.expertSystem.getVariableByName(var).getDomen().getValues()
        for val in vals:
            self.conclusionValueCombo.addItem(val)

    def okClick(self):
        expSys = self.conclusionEditorWindow.prevWindow.es_main_window.expertSystem
        if self.conclusionCombo.currentText() == '':
            error = QtWidgets.QErrorMessage(self.conclusionEditorWindow)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Необходимо указать переменную')
            return False
        var = expSys.getVariableByName(self.conclusionCombo.currentText())
        val = self.conclusionValueCombo.currentText()
        if self.conclusion is not None:
            self.conclusion.setVar(var)
            self.conclusion.setVal(val)
        else:
            self.conclusionEditorWindow.prevWindow.conclusionFacts.append(Fact(var, val))
        self.conclusionEditorWindow.prevWindow.onConclusionChanged()
        self.conclusionEditorWindow.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConclusionEditorWindow = QtWidgets.QMainWindow()
    ui = Ui_ConclusionEditorWindow()
    ui.setupUi(ConclusionEditorWindow)
    ConclusionEditorWindow.show()
    sys.exit(app.exec_())
