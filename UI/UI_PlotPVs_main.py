# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_PlotPVs_main.ui'
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
    QLabel, QLineEdit, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 602)
        self.actionSSRF_epics = QAction(MainWindow)
        self.actionSSRF_epics.setObjectName(u"actionSSRF_epics")
        self.actionSSRF_internet = QAction(MainWindow)
        self.actionSSRF_internet.setObjectName(u"actionSSRF_internet")
        self.action20U = QAction(MainWindow)
        self.action20U.setObjectName(u"action20U")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.action20U.setFont(font)
        self.actionViewPVs = QAction(MainWindow)
        self.actionViewPVs.setObjectName(u"actionViewPVs")
        self.actionadd_PV_name = QAction(MainWindow)
        self.actionadd_PV_name.setObjectName(u"actionadd_PV_name")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(100, 40))
        self.label_5.setMaximumSize(QSize(100, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.label_5.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.PV_name_txt = QLineEdit(self.centralwidget)
        self.PV_name_txt.setObjectName(u"PV_name_txt")
        self.PV_name_txt.setMinimumSize(QSize(260, 40))
        self.PV_name_txt.setMaximumSize(QSize(16777215, 40))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        self.PV_name_txt.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.PV_name_txt.setFont(font2)
        self.PV_name_txt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.PV_name_txt)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(100, 40))
        self.label_6.setMaximumSize(QSize(100, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.label_6.setPalette(palette2)
        self.label_6.setFont(font1)
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setFrameShadow(QFrame.Sunken)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.Tag_name_txt = QLineEdit(self.centralwidget)
        self.Tag_name_txt.setObjectName(u"Tag_name_txt")
        self.Tag_name_txt.setMinimumSize(QSize(150, 40))
        self.Tag_name_txt.setMaximumSize(QSize(16777215, 40))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        self.Tag_name_txt.setPalette(palette3)
        self.Tag_name_txt.setFont(font2)
        self.Tag_name_txt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Tag_name_txt)

        self.Add_pv_btn = QPushButton(self.centralwidget)
        self.Add_pv_btn.setObjectName(u"Add_pv_btn")
        sizePolicy.setHeightForWidth(self.Add_pv_btn.sizePolicy().hasHeightForWidth())
        self.Add_pv_btn.setSizePolicy(sizePolicy)
        self.Add_pv_btn.setMinimumSize(QSize(100, 40))
        self.Add_pv_btn.setMaximumSize(QSize(100, 40))
        self.Add_pv_btn.setFont(font2)
        self.Add_pv_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout.addWidget(self.Add_pv_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.PV_mdi = QMdiArea(self.splitter)
        self.PV_mdi.setObjectName(u"PV_mdi")
        self.PV_mdi.setStyleSheet(u"")
        self.splitter.addWidget(self.PV_mdi)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.BeamStatus_VLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.BeamStatus_VLayout.setObjectName(u"BeamStatus_VLayout")
        self.BeamStatus_VLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.verticalLayoutWidget)

        self.verticalLayout.addWidget(self.splitter)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.IP_label = QLabel(self.centralwidget)
        self.IP_label.setObjectName(u"IP_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.IP_label.sizePolicy().hasHeightForWidth())
        self.IP_label.setSizePolicy(sizePolicy1)
        self.IP_label.setMinimumSize(QSize(100, 12))
        self.IP_label.setMaximumSize(QSize(16777215, 12))
        palette4 = QPalette()
        brush5 = QBrush(QColor(255, 77, 23, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.IP_label.setPalette(palette4)
        font3 = QFont()
        font3.setFamilies([u"Cambria"])
        font3.setPointSize(12)
        font3.setItalic(True)
        self.IP_label.setFont(font3)
        self.IP_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.IP_label)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 894, 28))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush6 = QBrush(QColor(22, 22, 22, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        brush7 = QBrush(QColor(160, 160, 160, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.menubar.setPalette(palette5)
        self.menubar.setFont(font2)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        palette6 = QPalette()
        brush8 = QBrush(QColor(47, 198, 198, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        brush9 = QBrush(QColor(109, 109, 109, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        self.menuMenu.setPalette(palette6)
        self.menuMenu.setFont(font)
        self.menuPVTree = QMenu(self.menubar)
        self.menuPVTree.setObjectName(u"menuPVTree")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        self.menuPVTree.setPalette(palette7)
        self.menuPVTree.setFont(font)
        self.menuBeamStatus = QMenu(self.menubar)
        self.menuBeamStatus.setObjectName(u"menuBeamStatus")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        self.menuBeamStatus.setPalette(palette8)
        self.menuBeamStatus.setFont(font)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuPVTree.menuAction())
        self.menubar.addAction(self.menuBeamStatus.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMenu.addAction(self.actionViewPVs)
        self.menuMenu.addAction(self.actionadd_PV_name)
        self.menuPVTree.addAction(self.action20U)
        self.menuBeamStatus.addAction(self.actionSSRF_epics)
        self.menuBeamStatus.addAction(self.actionSSRF_internet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSSRF_epics.setText(QCoreApplication.translate("MainWindow", u"SSRF-epics", None))
        self.actionSSRF_internet.setText(QCoreApplication.translate("MainWindow", u"SSRF-internet", None))
        self.action20U.setText(QCoreApplication.translate("MainWindow", u"20U", None))
        self.actionViewPVs.setText(QCoreApplication.translate("MainWindow", u"ViewPVs", None))
        self.actionadd_PV_name.setText(QCoreApplication.translate("MainWindow", u"add PV name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PV name:", None))
        self.PV_name_txt.setText(QCoreApplication.translate("MainWindow", u"LiminZhou:ai1", None))
        self.PV_name_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PV name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tag:", None))
        self.Tag_name_txt.setText(QCoreApplication.translate("MainWindow", u"LiminZhou:ai1", None))
        self.Tag_name_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PV name", None))
        self.Add_pv_btn.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.IP_label.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuPVTree.setTitle(QCoreApplication.translate("MainWindow", u"PVTree", None))
        self.menuBeamStatus.setTitle(QCoreApplication.translate("MainWindow", u"BeamStatus", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

