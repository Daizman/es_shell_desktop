from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExplainWindow(object):
    def setupUi(self, ExplainWindow):
        ExplainWindow.setObjectName('ExplainWindow')
        ExplainWindow.resize(610, 288)
        self.centralwidget = QtWidgets.QWidget(ExplainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.ruleLabel = QtWidgets.QLabel(self.centralwidget)
        self.ruleLabel.setGeometry(QtCore.QRect(10, 0, 51, 16))
        self.ruleLabel.setObjectName('ruleLabel')
        self.expandRulesButton = QtWidgets.QPushButton(self.centralwidget)
        self.expandRulesButton.setGeometry(QtCore.QRect(10, 220, 261, 25))
        self.expandRulesButton.setObjectName('expandRulesButton')
        self.rulesTree = QtWidgets.QTreeView(self.centralwidget)
        self.rulesTree.setGeometry(QtCore.QRect(10, 20, 261, 192))
        self.rulesTree.setObjectName('rulesTree')
        self.varLabel = QtWidgets.QLabel(self.centralwidget)
        self.varLabel.setGeometry(QtCore.QRect(280, 0, 61, 16))
        self.varLabel.setObjectName('varLabel')
        self.varsView = QtWidgets.QTableView(self.centralwidget)
        self.varsView.setGeometry(QtCore.QRect(280, 20, 321, 221))
        self.varsView.setObjectName('varsView')
        ExplainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExplainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName('menubar')
        ExplainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExplainWindow)
        self.statusbar.setObjectName('statusbar')
        ExplainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ExplainWindow)
        QtCore.QMetaObject.connectSlotsByName(ExplainWindow)

    def retranslateUi(self, ExplainWindow):
        _translate = QtCore.QCoreApplication.translate
        ExplainWindow.setWindowTitle(_translate('ExplainWindow', 'Объяснение'))
        self.ruleLabel.setText(_translate('ExplainWindow', 'Правила'))
        self.expandRulesButton.setText(_translate('ExplainWindow', 'Раскрыть все'))
        self.varLabel.setText(_translate('ExplainWindow', 'Переменные'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExplainWindow = QtWidgets.QMainWindow()
    ui = Ui_ExplainWindow()
    ui.setupUi(ExplainWindow)
    ExplainWindow.show()
    sys.exit(app.exec_())
