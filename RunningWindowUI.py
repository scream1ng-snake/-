# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_table.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class RunningWindowUI(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #0D0D0E;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MenuBox = QHBoxLayout()
        self.MenuBox.setObjectName(u"MenuBox")
        self.progressBarLabel = QLabel(self.centralwidget)
        self.progressBarLabel.setObjectName(u"progressBarLabel")
        self.progressBarLabel.setStyleSheet(u"color: white;\n"
"font-size: 16px;")

        self.MenuBox.addWidget(self.progressBarLabel)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"border: 1px solid #303030;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"border-radius: 8px;\n"
"background-color: #00AC4F;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.MenuBox.addWidget(self.progressBar)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(True)
        self.startButton.setStyleSheet(u"QPushButton:enabled {\n"
"background-color: #00AC4F;\n"
"border: 1px solid #00AC4F;\n"
"border-radius: 8px;\n"
"font-size: 14px;\n"
"color: white;\n"
"padding: 5px 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgba(0, 172, 79, 0.3);\n"
"border: 1px solid rgba(0, 172, 79, 0.3);\n"
"border-radius: 8px;\n"
"font-size: 14px;\n"
"color: rgba(255, 255, 255, 0.5);\n"
"padding: 5px 10px;\n"
"}")

        self.MenuBox.addWidget(self.startButton)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setStyleSheet(u"QPushButton:enabled {\n"
"background-color: #EB3223;\n"
"border: 1px solid #EB3223;\n"
"border-radius: 8px;\n"
"font-size: 14px;\n"
"color: white;\n"
"padding: 5px 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgba(235, 50, 35, 0.3);\n"
"border: 1px solid rgba(235, 50, 35, 0.3);\n"
"border-radius: 8px;\n"
"font-size: 14px;\n"
"color: rgba(255, 255, 255, 0.5);\n"
"padding: 5px 10px;\n"
"}")

        self.MenuBox.addWidget(self.stopButton)


        self.verticalLayout.addLayout(self.MenuBox)

        self.tableBox = QHBoxLayout()
        self.tableBox.setObjectName(u"tableBox")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)

        self.tableBox.addWidget(self.tableWidget)


        self.verticalLayout.addLayout(self.tableBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.progressBarLabel.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u044b \u043a \u0437\u0430\u043f\u0443\u0441\u043a\u0443", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0410\u0420\u0422", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u041e\u041f", None))
    # retranslateUi

