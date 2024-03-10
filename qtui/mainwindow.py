# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(300, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 600))
        MainWindow.setMaximumSize(QtCore.QSize(300, 600))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nodns_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nodns_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.nodns_btn.setObjectName("nodns_btn")
        self.verticalLayout.addWidget(self.nodns_btn)
        self.cloudflare_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cloudflare_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.cloudflare_btn.setObjectName("cloudflare_btn")
        self.verticalLayout.addWidget(self.cloudflare_btn)
        self.google_btn = QtWidgets.QPushButton(self.centralwidget)
        self.google_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.google_btn.setObjectName("google_btn")
        self.verticalLayout.addWidget(self.google_btn)
        self.electro_btn = QtWidgets.QPushButton(self.centralwidget)
        self.electro_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.electro_btn.setObjectName("electro_btn")
        self.verticalLayout.addWidget(self.electro_btn)
        self.radar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.radar_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.radar_btn.setObjectName("radar_btn")
        self.verticalLayout.addWidget(self.radar_btn)
        self.shecan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.shecan_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.shecan_btn.setObjectName("shecan_btn")
        self.verticalLayout.addWidget(self.shecan_btn)
        self.dns403_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dns403_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.dns403_btn.setObjectName("dns403_btn")
        self.verticalLayout.addWidget(self.dns403_btn)
        self.begzar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.begzar_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.begzar_btn.setObjectName("begzar_btn")
        self.verticalLayout.addWidget(self.begzar_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DNS App"))
        self.nodns_btn.setText(_translate("MainWindow", "No DNS"))
        self.cloudflare_btn.setText(_translate("MainWindow", "Cloudflare"))
        self.google_btn.setText(_translate("MainWindow", "Google"))
        self.electro_btn.setText(_translate("MainWindow", "Electro"))
        self.radar_btn.setText(_translate("MainWindow", "Radar"))
        self.shecan_btn.setText(_translate("MainWindow", "Shecan"))
        self.dns403_btn.setText(_translate("MainWindow", "403"))
        self.begzar_btn.setText(_translate("MainWindow", "Begzar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
