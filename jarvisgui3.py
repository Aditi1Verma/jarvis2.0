from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, -20, 1200, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\jarvis2.0\GUI_jarvis\Black_Template.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.iron_man = QtWidgets.QLabel(self.centralwidget)
        self.iron_man.setGeometry(QtCore.QRect(560, 10, 471, 271))
        self.iron_man.setText("")
        self.iron_man.setPixmap(QtGui.QPixmap("C:\jarvis2.0\GUI_jarvis\Iron_Template_1.gif"))
        self.iron_man.setScaledContents(True)
        self.iron_man.setObjectName("iron_man")
        self.voice_rec = QtWidgets.QLabel(self.centralwidget)
        self.voice_rec.setGeometry(QtCore.QRect(-20, 160, 431, 321))
        self.voice_rec.setText("")
        self.voice_rec.setPixmap(QtGui.QPixmap("C:\jarvis2.0\GUI_jarvis\Siri_1.gif"))
        self.voice_rec.setScaledContents(True)
        self.voice_rec.setObjectName("voice_rec")
        self.initial = QtWidgets.QLabel(self.centralwidget)
        self.initial.setGeometry(QtCore.QRect(50, 390, 301, 141))
        self.initial.setText("")
        self.initial.setPixmap(QtGui.QPixmap("C:\jarvis2.0\GUI_jarvis\initial.gif"))
        self.initial.setScaledContents(True)
        self.initial.setObjectName("initial")
        self.code1 = QtWidgets.QLabel(self.centralwidget)
        self.code1.setGeometry(QtCore.QRect(30, 10, 341, 191))
        self.code1.setText("")
        self.code1.setPixmap(QtGui.QPixmap("C:\jarvis2.0\GUI_jarvis\B.G_Template_1.gif"))
        self.code1.setScaledContents(True)
        self.code1.setObjectName("code1")
        self.human = QtWidgets.QLabel(self.centralwidget)
        self.human.setGeometry(QtCore.QRect(390, 10, 241, 171))
        self.human.setText("")
        self.human.setPixmap(QtGui.QPixmap("C:\jarvis2.0\GUI_jarvis\Health_Template.gif"))
        self.human.setScaledContents(True)
        self.human.setObjectName("human")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 220, 271, 281))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:\jarvis2.0\GUI_jarvis\Code_Template.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 310, 191, 71))
        self.pushButton.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"font: 22pt \"Roboto\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 420, 191, 71))
        self.pushButton_2.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"font: 22pt \"Roboto\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "END"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


