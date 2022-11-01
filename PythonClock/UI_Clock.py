# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClockMFoScr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(240, 240)
        MainWindow.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.clockbox = QFrame(self.centralwidget)
        self.clockbox.setObjectName(u"clockbox")
        self.clockbox.setStyleSheet(u"")
        self.clockbox.setFrameShape(QFrame.StyledPanel)
        self.clockbox.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.clockbox)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.clock = QFrame(self.clockbox)
        self.clock.setObjectName(u"clock")
        self.clock.setMaximumSize(QSize(220, 220))
        self.clock.setStyleSheet(u"background-color: qconicalgradient(cx:0.495, cy:0.504386, angle:0, stop:0 rgba(32, 33, 30, 255));\n"
"border-radius:110px;")
        self.clock.setFrameShape(QFrame.StyledPanel)
        self.clock.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.clock)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.clockinternal = QFrame(self.clock)
        self.clockinternal.setObjectName(u"clockinternal")
        self.clockinternal.setMaximumSize(QSize(200, 200))
        self.clockinternal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:100px;")
        self.clockinternal.setFrameShape(QFrame.StyledPanel)
        self.clockinternal.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.clockinternal)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.timeframe = QFrame(self.clockinternal)
        self.timeframe.setObjectName(u"timeframe")
        self.timeframe.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.timeframe.setFrameShape(QFrame.StyledPanel)
        self.timeframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.timeframe)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 5, 1, 1)

        self.minute = QLabel(self.timeframe)
        self.minute.setObjectName(u"minute")
        self.minute.setMinimumSize(QSize(50, 50))
        self.minute.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setFamily(u"Segoe UI Semilight")
        font.setPointSize(34)
        self.minute.setFont(font)
        self.minute.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.minute, 2, 3, 1, 1)

        self.label = QLabel(self.timeframe)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 6)

        self.day = QLabel(self.timeframe)
        self.day.setObjectName(u"day")
        self.day.setFont(font1)
        self.day.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.day, 4, 0, 1, 6)

        self.AMPM = QLabel(self.timeframe)
        self.AMPM.setObjectName(u"AMPM")
        self.AMPM.setMinimumSize(QSize(52, 52))
        self.AMPM.setMaximumSize(QSize(52, 52))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(20)
        self.AMPM.setFont(font2)
        self.AMPM.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_5.addWidget(self.AMPM, 2, 4, 1, 1)

        self.colon_2 = QLabel(self.timeframe)
        self.colon_2.setObjectName(u"colon_2")
        self.colon_2.setMinimumSize(QSize(10, 50))
        self.colon_2.setMaximumSize(QSize(10, 50))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(30)
        self.colon_2.setFont(font3)
        self.colon_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_5.addWidget(self.colon_2, 2, 2, 1, 1)

        self.date = QLabel(self.timeframe)
        self.date.setObjectName(u"date")
        self.date.setFont(font1)
        self.date.setAlignment(Qt.AlignCenter)
        self.date.setWordWrap(True)

        self.gridLayout_5.addWidget(self.date, 5, 1, 2, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 0, 1, 6)

        self.hour = QLabel(self.timeframe)
        self.hour.setObjectName(u"hour")
        self.hour.setMinimumSize(QSize(50, 50))
        self.hour.setMaximumSize(QSize(50, 50))
        self.hour.setFont(font)
        self.hour.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.hour, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 7, 0, 1, 6)


        self.gridLayout_3.addWidget(self.timeframe, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.clockinternal, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.clock, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.clockbox, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.minute.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello,Yashraj", None))
        self.day.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.AMPM.setText(QCoreApplication.translate("MainWindow", u"AM", None))
        self.colon_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"April 12, 2022", None))
        self.hour.setText(QCoreApplication.translate("MainWindow", u"05", None))
    # retranslateUi

