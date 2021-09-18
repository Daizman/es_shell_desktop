from PyQt5 import QtCore, QtGui, QtWidgets
from views.EditVarWindow import Ui_EditVarWindow
from models.Fact import Fact


class Ui_RequisiteEditorWindow(object):
    def setupUi(self, RequisiteEditorWindow, requisite=None):
        RequisiteEditorWindow.setObjectName("RequisiteEditorWindow")
        RequisiteEditorWindow.resize(355, 179)
        RequisiteEditorWindow.setMinimumSize(QtCore.QSize(355, 179))
        RequisiteEditorWindow.setMaximumSize(QtCore.QSize(355, 179))
        self.centralwidget = QtWidgets.QWidget(RequisiteEditorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.requisiteCombo = QtWidgets.QComboBox(self.centralwidget)
        self.requisiteCombo.setGeometry(QtCore.QRect(10, 10, 301, 22))
        self.requisiteCombo.setObjectName("requisiteCombo")
        self.requisiteValueCombo = QtWidgets.QComboBox(self.centralwidget)
        self.requisiteValueCombo.setGeometry(QtCore.QRect(10, 60, 341, 22))
        self.requisiteValueCombo.setObjectName("requisiteValueCombo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 90, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.requisiteAddButton = QtWidgets.QPushButton(self.centralwidget)
        self.requisiteAddButton.setGeometry(QtCore.QRect(310, 9, 41, 24))
        self.requisiteAddButton.setObjectName("requisiteAddButton")
        self.eqLabel = QtWidgets.QLabel(self.centralwidget)
        self.eqLabel.setGeometry(QtCore.QRect(180, 40, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eqLabel.setFont(font)
        self.eqLabel.setObjectName("eqLabel")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(190, 110, 75, 23))
        self.okButton.setObjectName("okButton")
        RequisiteEditorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RequisiteEditorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 21))
        self.menubar.setObjectName("menubar")
        RequisiteEditorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RequisiteEditorWindow)
        self.statusbar.setObjectName("statusbar")
        RequisiteEditorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RequisiteEditorWindow)
        self.expShellMainWindow = RequisiteEditorWindow.prevWindow.expShellMainWindow
        self.requisiteEditorWindow = RequisiteEditorWindow
        self.connectButtons()
        self.fillVars()
        self.requisite = requisite if requisite is not None else None
        if self.requisite is not None:
            self.fillRequisite()
        QtCore.QMetaObject.connectSlotsByName(RequisiteEditorWindow)

    def retranslateUi(self, RequisiteEditorWindow):
        _translate = QtCore.QCoreApplication.translate
        RequisiteEditorWindow.setWindowTitle(_translate("RequisiteEditorWindow", "Факт посылки"))
        self.requisiteAddButton.setText(_translate("RequisiteEditorWindow", "+"))
        self.eqLabel.setText(_translate("RequisiteEditorWindow", "="))
        self.cancelButton.setText(_translate("RequisiteEditorWindow", "Отмена"))
        self.okButton.setText(_translate("RequisiteEditorWindow", "OK"))

    def connectButtons(self):
        self.okButton.clicked.connect(self.okClick)
        self.requisiteAddButton.clicked.connect(self.addVar)
        self.requisiteCombo.currentTextChanged.connect(self.onSelectVar)
        self.cancelButton.clicked.connect(lambda: self.requisiteEditorWindow.close())

    def fillRequisite(self):
        varIdx = self.requisiteCombo.findText(self.requisite.getVar().getName())
        self.requisiteCombo.setCurrentIndex(varIdx)
        valIdx = self.requisiteValueCombo.findText(self.requisite.getVal())
        self.requisiteValueCombo.setCurrentIndex(valIdx)

    def addVar(self):
        self.addVarWindow = QtWidgets.QMainWindow()
        self.addVarUI = Ui_EditVarWindow()
        self.addVarWindow.prevWindow = self
        self.addVarUI.setupUi(self.addVarWindow)
        self.addVarWindow.show()

    def onSelectVar(self):
        self.fillValues()

    def onVarsChange(self):
        self.requisiteEditorWindow.prevWindow.editRuleWindow.prevWindow.onVarsChange()
        self.fillVars()
        self.requisiteCombo.setCurrentIndex(self.requisiteCombo.count() - 1)

    def onDomensChange(self):
        self.requisiteEditorWindow.prevWindow.editRuleWindow.prevWindow.onDomensChange()
        self.fillVars()
        self.requisiteCombo.setCurrentIndex(self.requisiteCombo.count() - 1)

    def fillVars(self):
        self.requisiteCombo.clear()
        esVars = self.expShellMainWindow.expertSystem.getVariables()
        for var in esVars:
            self.requisiteCombo.addItem(var.getName())

    def fillValues(self):
        self.requisiteValueCombo.clear()
        var = self.requisiteCombo.currentText()
        if var == "":
            return False
        vals = self.expShellMainWindow.expertSystem.getVariableByName(var).getDomen().getValues()
        for val in vals:
            self.requisiteValueCombo.addItem(val)

    def okClick(self):
        expSys = self.requisiteEditorWindow.prevWindow.expShellMainWindow.expertSystem
        if self.requisiteCombo.currentText() == "":
            error = QtWidgets.QErrorMessage(self.requisiteEditorWindow)
            error.setWindowTitle("Ошибка!")
            error.showMessage("Необходимо указать переменную")
            return False
        var = expSys.getVariableByName(self.requisiteCombo.currentText())
        val = self.requisiteValueCombo.currentText()
        if self.requisite is not None:
            self.requisite.setVar(var)
            self.requisite.setVal(val)
        else:
            self.requisiteEditorWindow.prevWindow.requisiteFacts.append(Fact(var, val))
        self.requisiteEditorWindow.prevWindow.onRequisiteChanged()
        self.requisiteEditorWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RequisiteEditorWindow = QtWidgets.QMainWindow()
    ui = Ui_RequisiteEditorWindow()
    ui.setupUi(RequisiteEditorWindow)
    RequisiteEditorWindow.show()
    sys.exit(app.exec_())
