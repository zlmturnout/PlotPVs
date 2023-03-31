# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_PV_saveRecord.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.XML_file_txt = QLineEdit(self.centralwidget)
        self.XML_file_txt.setObjectName(u"XML_file_txt")
        self.XML_file_txt.setMinimumSize(QSize(260, 40))
        self.XML_file_txt.setMaximumSize(QSize(16777215, 40))
        palette = QPalette()
        brush = QBrush(QColor(8, 177, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.XML_file_txt.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(14)
        font.setBold(True)
        self.XML_file_txt.setFont(font)
        self.XML_file_txt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.XML_file_txt)

        self.Load_pvxml_btn = QPushButton(self.centralwidget)
        self.Load_pvxml_btn.setObjectName(u"Load_pvxml_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Load_pvxml_btn.sizePolicy().hasHeightForWidth())
        self.Load_pvxml_btn.setSizePolicy(sizePolicy)
        self.Load_pvxml_btn.setMinimumSize(QSize(100, 40))
        self.Load_pvxml_btn.setMaximumSize(QSize(100, 40))
        self.Load_pvxml_btn.setFont(font)
        self.Load_pvxml_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_2.addWidget(self.Load_pvxml_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.TableView = QTableView(self.centralwidget)
        self.TableView.setObjectName(u"TableView")
        palette1 = QPalette()
        brush3 = QBrush(QColor(0, 170, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.TableView.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.TableView.setFont(font1)

        self.verticalLayout.addWidget(self.TableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(100, 40))
        self.label_7.setMaximumSize(QSize(100, 40))
        palette2 = QPalette()
        brush4 = QBrush(QColor(255, 85, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush5 = QBrush(QColor(0, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_7.setPalette(palette2)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_7.setFont(font2)
        self.label_7.setFrameShape(QFrame.NoFrame)
        self.label_7.setFrameShadow(QFrame.Sunken)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.Status_txt = QLineEdit(self.centralwidget)
        self.Status_txt.setObjectName(u"Status_txt")
        self.Status_txt.setMinimumSize(QSize(400, 40))
        self.Status_txt.setMaximumSize(QSize(16777215, 40))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.Status_txt.setPalette(palette3)
        self.Status_txt.setFont(font)
        self.Status_txt.setStyleSheet(u"border:2px;border-style:dashed;border-color: rgb(0, 170, 255);")
        self.Status_txt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Status_txt)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.Add_record_btn = QPushButton(self.centralwidget)
        self.Add_record_btn.setObjectName(u"Add_record_btn")
        sizePolicy.setHeightForWidth(self.Add_record_btn.sizePolicy().hasHeightForWidth())
        self.Add_record_btn.setSizePolicy(sizePolicy)
        self.Add_record_btn.setMinimumSize(QSize(130, 40))
        self.Add_record_btn.setMaximumSize(QSize(100, 40))
        self.Add_record_btn.setFont(font)
        self.Add_record_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout.addWidget(self.Add_record_btn)

        self.Save_tofile_btn = QPushButton(self.centralwidget)
        self.Save_tofile_btn.setObjectName(u"Save_tofile_btn")
        sizePolicy.setHeightForWidth(self.Save_tofile_btn.sizePolicy().hasHeightForWidth())
        self.Save_tofile_btn.setSizePolicy(sizePolicy)
        self.Save_tofile_btn.setMinimumSize(QSize(100, 40))
        self.Save_tofile_btn.setMaximumSize(QSize(120, 40))
        self.Save_tofile_btn.setFont(font)
        self.Save_tofile_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout.addWidget(self.Save_tofile_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 877, 31))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.menubar.setFont(font3)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.XML_file_txt.setText("")
        self.XML_file_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XML file with PV names", None))
        self.Load_pvxml_btn.setText(QCoreApplication.translate("MainWindow", u"LoadXML", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"StatusText", None))
        self.Status_txt.setText("")
        self.Status_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input Current Status", None))
        self.Add_record_btn.setText(QCoreApplication.translate("MainWindow", u"add record", None))
        self.Save_tofile_btn.setText(QCoreApplication.translate("MainWindow", u"Save to File", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

