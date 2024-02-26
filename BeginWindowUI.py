# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'design.ui'
##
# Created by: Qt User Interface Compiler version 6.6.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc


class BeginWindowUI(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(438, 307)
        MainWindow.setStyleSheet(u"background-color: #0D0D0E;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo_box = QHBoxLayout()
        self.logo_box.setSpacing(10)
        self.logo_box.setObjectName(u"logo_box")
        self.logo_box.setContentsMargins(-1, 20, -1, 20)
        self.logo_spacer_left = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_box.addItem(self.logo_spacer_left)

        self.logo_icon = QLabel(self.frame)
        self.logo_icon.setObjectName(u"logo_icon")
        self.logo_icon.setPixmap(QPixmap(u":/icons/hello_icon.svg"))

        self.logo_box.addWidget(self.logo_icon)

        self.logo_text = QLabel(self.frame)
        self.logo_text.setObjectName(u"logo_text")
        self.logo_text.setStyleSheet(u"color: #F1950D;\n"
                                     "font-size: 24px;\n"
                                     "font-weight: 700;")

        self.logo_box.addWidget(self.logo_text)

        self.logo_spacer_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_box.addItem(self.logo_spacer_right)

        self.verticalLayout.addLayout(self.logo_box)

        self.file_form_box = QHBoxLayout()
        self.file_form_box.setObjectName(u"file_form_box")
        self.file_form_box.setContentsMargins(20, -1, 20, -1)
        self.horizontalSpacer = QSpacerItem(
            13, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.file_form_box.addItem(self.horizontalSpacer)

        self.file_form = QFormLayout()
        self.file_form.setObjectName(u"file_form")
        self.file_form.setHorizontalSpacing(10)
        self.path_suggest_label = QLabel(self.frame)
        self.path_suggest_label.setObjectName(u"path_suggest_label")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.path_suggest_label.sizePolicy().hasHeightForWidth())
        self.path_suggest_label.setSizePolicy(sizePolicy)
        self.path_suggest_label.setMinimumSize(QSize(140, 0))
        self.path_suggest_label.setStyleSheet(u"color: gray;")
        self.path_suggest_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.path_suggest_label.setWordWrap(True)
        self.path_suggest_label.setMargin(0)

        self.file_form.setWidget(
            0, QFormLayout.LabelRole, self.path_suggest_label)

        self.path_input_box = QHBoxLayout()
        self.path_input_box.setSpacing(0)
        self.path_input_box.setObjectName(u"path_input_box")
        self.path_browse_input = QLineEdit(self.frame)
        self.path_browse_input.setObjectName(u"path_browse_input")
        sizePolicy.setHeightForWidth(
            self.path_browse_input.sizePolicy().hasHeightForWidth())
        self.path_browse_input.setSizePolicy(sizePolicy)
        self.path_browse_input.setStyleSheet(u"background-color: #151519;\n"
                                             "border: 1px solid #303030;\n"
                                             "border-radius: 8px;\n"
                                             "color: gray;\n"
                                             "padding: 5px 10px;\n"
                                             "border-top-right-radius: 0;\n"
                                             "border-bottom-right-radius: 0;")

        self.path_input_box.addWidget(self.path_browse_input)

        self.path_browse_button = QPushButton(self.frame)
        self.path_browse_button.setObjectName(u"path_browse_button")
        sizePolicy.setHeightForWidth(
            self.path_browse_button.sizePolicy().hasHeightForWidth())
        self.path_browse_button.setSizePolicy(sizePolicy)
        self.path_browse_button.setStyleSheet(u"background-color: #00AC4F;\n"
                                              "border: 1px solid #00AC4F;\n"
                                              "border-radius: 8px;\n"
                                              "font-size: 14px;\n"
                                              "color: white;\n"
                                              "padding: 5px 10px;\n"
                                              "border-top-left-radius: 0;\n"
                                              "border-bottom-left-radius: 0;")

        self.path_input_box.addWidget(self.path_browse_button)

        self.file_form.setLayout(0, QFormLayout.FieldRole, self.path_input_box)

        self.error_path_alert = QLabel(self.frame)
        self.error_path_alert.setObjectName(u"error_path_alert")
        self.error_path_alert.setStyleSheet(u"color: red;")

        self.file_form.setWidget(
            1, QFormLayout.FieldRole, self.error_path_alert)

        self.files_on_dir_key = QLabel(self.frame)
        self.files_on_dir_key.setObjectName(u"files_on_dir_key")
        self.files_on_dir_key.setMinimumSize(QSize(140, 0))
        self.files_on_dir_key.setStyleSheet(u"color: gray;")
        self.files_on_dir_key.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.files_on_dir_key.setWordWrap(True)
        self.files_on_dir_key.setMargin(0)

        self.file_form.setWidget(
            2, QFormLayout.LabelRole, self.files_on_dir_key)

        self.files_on_dir_value = QLabel(self.frame)
        self.files_on_dir_value.setObjectName(u"files_on_dir_value")
        self.files_on_dir_value.setMinimumSize(QSize(0, 0))
        self.files_on_dir_value.setStyleSheet(u"color: gray;\n"
                                              "font-size: 20px;")
        self.files_on_dir_value.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.files_on_dir_value.setWordWrap(True)
        self.files_on_dir_value.setMargin(0)

        self.file_form.setWidget(
            2, QFormLayout.FieldRole, self.files_on_dir_value)

        self.file_form_box.addLayout(self.file_form)

        self.horizontalSpacer_2 = QSpacerItem(
            13, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.file_form_box.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.file_form_box)

        self.start_btn_box = QHBoxLayout()
        self.start_btn_box.setObjectName(u"start_btn_box")
        self.start_btn_box.setContentsMargins(-1, 20, -1, -1)
        self.left_space_start_btn = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.start_btn_box.addItem(self.left_space_start_btn)

        self.start_recogntion = QPushButton(self.frame)
        self.start_recogntion.setObjectName(u"start_recogntion")
        self.start_recogntion.setEnabled(True)
        self.start_recogntion.setStyleSheet(u"QPushButton:enabled {\n"
                                            "background-color: #F1950D;\n"
                                            "border: 1px solid #F1950D;\n"
                                            "border-radius: 8px;\n"
                                            "font-size: 14px;\n"
                                            "color: white;\n"
                                            "padding: 5px 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:disabled {\n"
                                            "background-color: rgba(241, 149, 13, 0.49);\n"
                                            "border-radius: 8px;\n"
                                            "font-size: 14px;\n"
                                            "color: rgba(255, 255, 255, 0.5);\n"
                                            "padding: 5px 10px;\n"
                                            "}")

        self.start_btn_box.addWidget(self.start_recogntion)

        self.right_space_start_btn = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.start_btn_box.addItem(self.right_space_start_btn)

        self.verticalLayout.addLayout(self.start_btn_box)

        self.spacer_bottom = QHBoxLayout()
        self.spacer_bottom.setObjectName(u"spacer_bottom")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.spacer_bottom.addItem(self.verticalSpacer)

        self.verticalLayout.addLayout(self.spacer_bottom)

        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.logo_icon.setText("")
        self.logo_text.setText(QCoreApplication.translate(
            "MainWindow", u"\u0421\u0422\u0410\u041d\u0426\u0418\u042f", None))
        self.path_suggest_label.setText(QCoreApplication.translate(
            "MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430\u043c\u0438 (jpeg):", None))
        self.path_browse_input.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"\u043f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435", None))
        self.path_browse_button.setText(QCoreApplication.translate(
            "MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.error_path_alert.setText(QCoreApplication.translate(
            "MainWindow", u"\u041f\u0430\u043f\u043a\u0430 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u0430*", None))
        self.files_on_dir_key.setText(QCoreApplication.translate(
            "MainWindow", u"\u0424\u0430\u0439\u043b\u043e\u0432 \u0432 \u043f\u0430\u043f\u043a\u0435:", None))
        self.files_on_dir_value.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.start_recogntion.setText(QCoreApplication.translate(
            "MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
    # retranslateUi
