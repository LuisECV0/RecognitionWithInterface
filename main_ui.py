# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FrameSuperior = QtWidgets.QFrame(self.frame)
        self.FrameSuperior.setMaximumSize(QtCore.QSize(16777215, 45))
        self.FrameSuperior.setStyleSheet("QFrame {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"padding: 5px 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 0, 0);\n"
"}\n"
"")
        self.FrameSuperior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameSuperior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameSuperior.setObjectName("FrameSuperior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.FrameSuperior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.FrameSuperior)
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(354, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(self.FrameSuperior)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.FrameSuperior)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/maximizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.FrameSuperior)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.FrameSuperior)
        self.FrameInferior = QtWidgets.QFrame(self.frame)
        self.FrameInferior.setStyleSheet("background-color: rgb(0, 0, 127)")
        self.FrameInferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameInferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameInferior.setObjectName("FrameInferior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FrameInferior)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.FrameInferior)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:rgb(46, 42, 94) ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 127) ;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.box_img = QtWidgets.QPushButton(self.frame_2)
        self.box_img.setMaximumSize(QtCore.QSize(300, 300))
        self.box_img.setStyleSheet("")
        self.box_img.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/camara.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.box_img.setIcon(icon3)
        self.box_img.setIconSize(QtCore.QSize(200, 200))
        self.box_img.setObjectName("box_img")
        self.verticalLayout_3.addWidget(self.box_img)
        self.button_cam = QtWidgets.QPushButton(self.frame_2)
        self.button_cam.setStyleSheet("\n"
"color:rgb(255, 255, 255);\n"
"font-weight:600;\n"
"border-radius:5px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"padding: 5px 10px")
        self.button_cam.setObjectName("button_cam")
        self.verticalLayout_3.addWidget(self.button_cam)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.FrameInferior)
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color:rgb(46, 42, 94) ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 127) ;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setMaximumSize(QtCore.QSize(300, 300))
        self.pushButton_8.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/voz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setStyleSheet("\n"
"color:rgb(255, 255, 255);\n"
"font-weight:600;\n"
"border-radius:5px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"padding: 5px 10px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.FrameInferior)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_cam.setText(_translate("MainWindow", "Probar con Cámara"))
        self.pushButton_3.setText(_translate("MainWindow", "Probar con voz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
