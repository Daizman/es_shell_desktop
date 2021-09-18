from PyQt5 import QtCore, QtGui, QtWidgets
from views.EditVarWindow import Ui_EditVarWindow
from model.Fact import Fact


class UiRequisiteEditorWindow(object):
    def __init__(self, requisite_editor_window, requisite=None):
        requisite_editor_window.setObjectName("requisite_editor_window")
        requisite_editor_window.resize(355, 179)
        requisite_editor_window.setMinimumSize(QtCore.QSize(355, 179))
        requisite_editor_window.setMaximumSize(QtCore.QSize(355, 179))

        self.central_widget = QtWidgets.QWidget(requisite_editor_window)
        self.central_widget.setObjectName("central_widget")

        self.requisite_combo = QtWidgets.QComboBox(self.central_widget)
        self.requisite_combo.setGeometry(QtCore.QRect(10, 10, 301, 22))
        self.requisite_combo.setObjectName("requisite_combo")

        self.requisiteValueCombo = QtWidgets.QComboBox(self.central_widget)
        self.requisiteValueCombo.setGeometry(QtCore.QRect(10, 60, 341, 22))
        self.requisiteValueCombo.setObjectName("requisiteValueCombo")

        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setGeometry(QtCore.QRect(10, 90, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.requisiteAddButton = QtWidgets.QPushButton(self.central_widget)
        self.requisiteAddButton.setGeometry(QtCore.QRect(310, 9, 41, 24))
        self.requisiteAddButton.setObjectName("requisiteAddButton")

        self.eqLabel = QtWidgets.QLabel(self.central_widget)
        self.eqLabel.setGeometry(QtCore.QRect(180, 40, 16, 16))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.eqLabel.setFont(font)
        self.eqLabel.setObjectName("eqLabel")

        self.cancelButton = QtWidgets.QPushButton(self.central_widget)
        self.cancelButton.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.okButton = QtWidgets.QPushButton(self.central_widget)
        self.okButton.setGeometry(QtCore.QRect(190, 110, 75, 23))
        self.okButton.setObjectName("okButton")

        requisite_editor_window.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(requisite_editor_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 21))
        self.menubar.setObjectName("menubar")

        requisite_editor_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(requisite_editor_window)
        self.statusbar.setObjectName("statusbar")

        requisite_editor_window.setStatusBar(self.statusbar)

        self.retranslate_ui(requisite_editor_window)

        self.expShellMainWindow = requisite_editor_window.prevWindow.expShellMainWindow
        self.requisiteEditorWindow = requisite_editor_window

        self.connect_buttons()
        self.fill_vars()

        self.requisite = requisite if requisite is not None else None

        if self.requisite is not None:
            self.fill_requisite()

        QtCore.QMetaObject.connectSlotsByName(requisite_editor_window)

    def retranslate_ui(self, requisite_editor_window):
        _translate = QtCore.QCoreApplication.translate
        requisite_editor_window.setWindowTitle(_translate("RequisiteEditorWindow", "Факт посылки"))
        self.requisiteAddButton.setText(_translate("RequisiteEditorWindow", "+"))
        self.eqLabel.setText(_translate("RequisiteEditorWindow", "="))
        self.cancelButton.setText(_translate("RequisiteEditorWindow", "Отмена"))
        self.okButton.setText(_translate("RequisiteEditorWindow", "OK"))

    def connect_buttons(self):
        self.okButton.clicked.connect(self.ok)
        self.requisiteAddButton.clicked.connect(self.add_var)
        self.requisite_combo.currentTextChanged.connect(self.on_select_var)
        self.cancelButton.clicked.connect(lambda: self.requisiteEditorWindow.close())

    def fill_requisite(self):
        var_index = self.requisite_combo.findText(self.requisite.getVar().getName())
        self.requisite_combo.setCurrentIndex(var_index)
        val_idx = self.requisiteValueCombo.findText(self.requisite.getVal())
        self.requisiteValueCombo.setCurrentIndex(val_idx)

    def add_var(self):
        self.addVarWindow = QtWidgets.QMainWindow()
        self.addVarUI = Ui_EditVarWindow()
        self.addVarWindow.prevWindow = self
        self.addVarUI.setupUi(self.addVarWindow)
        self.addVarWindow.show()

    def on_select_var(self):
        self.fill_values()

    def on_vars_change(self):
        self.requisiteEditorWindow.prevWindow.editRuleWindow.prevWindow.on_vars_change()
        self.fill_vars()
        self.requisite_combo.setCurrentIndex(self.requisite_combo.count() - 1)

    def on_domains_change(self):
        self.requisiteEditorWindow.prevWindow.editRuleWindow.prevWindow.on_domains_change()
        self.fill_vars()
        self.requisite_combo.setCurrentIndex(self.requisite_combo.count() - 1)

    def fill_vars(self):
        self.requisite_combo.clear()
        es_vars = self.expShellMainWindow.expertSystem.getVariables()
        for var in es_vars:
            self.requisite_combo.addItem(var.getName())

    def fill_values(self):
        self.requisiteValueCombo.clear()
        var = self.requisite_combo.currentText()
        if var == "":
            return False
        values = self.expShellMainWindow.expertSystem.getVariableByName(var).getDomen().getValues()
        for val in values:
            self.requisiteValueCombo.addItem(val)

    def ok(self):
        exp_sys = self.requisiteEditorWindow.prevWindow.expShellMainWindow.expertSystem
        if self.requisite_combo.currentText() == "":
            error = QtWidgets.QErrorMessage(self.requisiteEditorWindow)
            error.setWindowTitle("Ошибка!")
            error.showMessage("Необходимо указать переменную")
            return False
        var = exp_sys.getVariableByName(self.requisite_combo.currentText())
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
    ui = UiRequisiteEditorWindow(RequisiteEditorWindow)
    RequisiteEditorWindow.show()
    sys.exit(app.exec_())
