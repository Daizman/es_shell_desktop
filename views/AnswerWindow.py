from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_answerWindow(object):
    def setupUi(self, answerWindow):
        answerWindow.setObjectName("answerWindow")
        answerWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(answerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.answerTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.answerTree.setGeometry(QtCore.QRect(10, 20, 781, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerTree.sizePolicy().hasHeightForWidth())
        self.answerTree.setSizePolicy(sizePolicy)
        self.answerTree.setColumnCount(1)
        self.answerTree.setHeaderLabels([''])
        self.answerTree.setObjectName("answerTree")
        self.descrLabel = QtWidgets.QLabel(self.centralwidget)
        self.descrLabel.setGeometry(QtCore.QRect(10, 0, 61, 16))
        self.descrLabel.setObjectName("descrLabel")
        self.goalLabel = QtWidgets.QLabel(self.centralwidget)
        self.goalLabel.setGeometry(QtCore.QRect(10, 410, 47, 13))
        self.goalLabel.setObjectName("goalLabel")

        self.memLabel = QtWidgets.QLabel(self.centralwidget)
        self.memLabel.setGeometry(QtCore.QRect(10, 450, 47, 13))
        self.memLabel.setObjectName("goalLabel")
        self.memLabel.setText("Раб.пам.")

        self.workMem = QtWidgets.QTextEdit(self.centralwidget)
        self.workMem.setGeometry(QtCore.QRect(10, 480, 700, 150))
        self.workMem.setObjectName("workMem")

        self.expAllBtn = QtWidgets.QPushButton(self.centralwidget)
        self.expAllBtn.setGeometry(QtCore.QRect(10, 650, 130, 30))
        self.expAllBtn.setObjectName("expAllBtn")
        self.expAllBtn.setText("Развернуть / свернуть")

        answerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(answerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        answerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(answerWindow)
        self.statusbar.setObjectName("statusbar")
        answerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(answerWindow)
        self.answerWindow = answerWindow
        QtCore.QMetaObject.connectSlotsByName(answerWindow)

    def retranslateUi(self, answerWindow):
        _translate = QtCore.QCoreApplication.translate
        answerWindow.setWindowTitle(_translate("answerWindow", "Ответ"))
        self.descrLabel.setText(_translate("answerWindow", "Обяснеие"))
        self.goalLabel.setText(_translate("answerWindow", "Цель:"))

    def expandCollapse(self):
        if not self.expanded:
            self.answerTree.expandAll()
            self.expanded = True
        else:
            self.answerTree.collapseAll()
            self.expanded = False

    def fillForm(self, es, var):
        self.goalLabel.resize(800, 48)
        if var is None or es.getMemory().getVarVal(var) is None:
            self.answerTree.clear()
            self.expAllBtn.hide()
            self.answerTree.addTopLevelItem(QtWidgets.QTreeWidgetItem(["Не удалось найти значение для цели"]))
            self.goalLabel.setText('Не удалось найти значение для цели')
        else:
            self.goalLabel.setText("Цель: " + var.getName() + " = " + es.getMemory().getVarVal(var)['value'])
            self.expanded = False
            self.expAllBtn.clicked.connect(self.expandCollapse)
        wMemText = ""
        for actFact in es.getMemory().getVarsAndVals().values():
            wMemText += actFact['variable'].getName() + ": " + actFact['value'] + "\n"
        self.workMem.setText(wMemText)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    answerWindow = QtWidgets.QMainWindow()
    ui = Ui_answerWindow()
    ui.setupUi(answerWindow)
    answerWindow.show()
    sys.exit(app.exec_())
