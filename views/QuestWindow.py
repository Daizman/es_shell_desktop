from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_questWindow(object):
    def setupUi(self, questWindow):
        questWindow.setObjectName("questWindow")
        questWindow.resize(281, 166)
        self.centralwidget = QtWidgets.QWidget(questWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.varVals = QtWidgets.QComboBox(self.centralwidget)
        self.varVals.setGeometry(QtCore.QRect(10, 70, 261, 22))
        self.varVals.setObjectName("varVals")
        self.answBtn = QtWidgets.QPushButton(self.centralwidget)
        self.answBtn.setGeometry(QtCore.QRect(10, 100, 261, 23))
        self.answBtn.setObjectName("answBtn")
        self.questLabel = QtWidgets.QLabel(self.centralwidget)
        self.questLabel.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.questLabel.setObjectName("questLabel")
        questWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(questWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 21))
        self.menubar.setObjectName("menubar")
        questWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(questWindow)
        self.statusbar.setObjectName("statusbar")
        questWindow.setStatusBar(self.statusbar)

        self.retranslateUi(questWindow)
        QtCore.QMetaObject.connectSlotsByName(questWindow)

    def retranslateUi(self, questWindow):
        _translate = QtCore.QCoreApplication.translate
        questWindow.setWindowTitle(_translate("questWindow", "Вопрос"))
        self.answBtn.setText(_translate("questWindow", "Ответить"))
        self.questLabel.setText(_translate("questWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    questWindow = QtWidgets.QMainWindow()
    ui = Ui_questWindow()
    ui.setupUi(questWindow)
    questWindow.show()
    sys.exit(app.exec_())
