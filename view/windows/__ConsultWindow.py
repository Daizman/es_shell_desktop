from PyQt5 import QtCore, QtWidgets
from models.VarType import VarType
from view.windows.__AnswerWindow import Ui_answerWindow


class Ui_ConsultWindow(object):
    def setupUi(self, ConsultWindow):
        ConsultWindow.setObjectName('ConsultWindow')
        ConsultWindow.resize(348, 150)
        self.centralwidget = QtWidgets.QWidget(ConsultWindow)
        self.centralwidget.setObjectName('central_widget')
        self.dialogFrame = QtWidgets.QFrame(self.centralwidget)
        self.dialogFrame.setGeometry(QtCore.QRect(10, 10, 331, 471))
        self.dialogFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dialogFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dialogFrame.setObjectName('dialogFrame')
        self.answerButton = QtWidgets.QPushButton(self.centralwidget)
        self.answerButton.setGeometry(QtCore.QRect(240, 52, 101, 25))
        self.answerButton.setObjectName('answerButton')
        self.answerCombo = QtWidgets.QComboBox(self.centralwidget)
        self.answerCombo.setGeometry(QtCore.QRect(10, 52, 221, 22))
        self.answerCombo.setObjectName('answerCombo')
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 82, 331, 25))
        self.exitButton.setObjectName('exitButton')
        self.questionText = QtWidgets.QLabel(self.centralwidget)
        self.questionText.setText('Выберите цель консультации')
        self.questionText.setGeometry(QtCore.QRect(10, 20, 170, 30))
        self.questionText.setObjectName('question_te')

        ConsultWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConsultWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName('menu_bar')
        ConsultWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConsultWindow)
        self.statusbar.setObjectName('status_bar')
        ConsultWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConsultWindow)
        self.consultWindow = ConsultWindow
        self.expShellMainWindow = ConsultWindow.prevWindow.es_main_window

        self.answerWindow = QtWidgets.QMainWindow()
        self.answerUI = Ui_answerWindow()
        self.answerWindow.prevWindow = self
        self.answerUI.setupUi(self.answerWindow)
        self.answerWindow.hide()

        self.connectButtons()
        self.consultGoal = None
        self.firstOpen = True
        self.questedVar = None

        QtCore.QMetaObject.connectSlotsByName(ConsultWindow)
        self.fillGoals()

    def retranslateUi(self, ConsultWindow):
        _translate = QtCore.QCoreApplication.translate
        ConsultWindow.setWindowTitle(_translate('ConsultWindow', 'Консультация'))
        self.answerButton.setText(_translate('ConsultWindow', 'Ответить'))
        self.exitButton.setText(_translate('ConsultWindow', 'Выход'))

    def connectButtons(self):
        self.answerButton.clicked.connect(self.getAnswer)
        self.exitButton.clicked.connect(lambda: self.consultWindow.close())

    def getAnswer(self):
        es = self.expShellMainWindow.expertSystem
        if self.firstOpen:
            self.firstOpen = False
            var = es.getVariableByName(self.answerCombo.currentText())
            if es.consult(var, self, self.answerUI) == -1:
                self.answerWindow.answerTree.addTopLevelItem(QtWidgets.QTreeWidgetItem('Произошел сбой'))
            self.answerUI.fillForm(es, var)
            self.answerWindow.show()
            self.consultWindow.close()

    def fillGoals(self):
        self.answerCombo.clear()
        variables = self.expShellMainWindow.expertSystem.getVariables()
        if not variables:
            error = QtWidgets.QErrorMessage(self.consultWindow)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Список выводимых переменных пуст')
            error.accepted.connect(lambda: self.consultWindow.close())
            return False
        for var in variables:
            if var.getVarType() == VarType.INFERRED:
                self.answerCombo.addItem(var.getName())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConsultWindow = QtWidgets.QMainWindow()
    ui = Ui_ConsultWindow()
    ui.setupUi(ConsultWindow)
    ConsultWindow.show()
    sys.exit(app.exec_())
