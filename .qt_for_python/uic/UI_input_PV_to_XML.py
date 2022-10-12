# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_input_PV_to_XML.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(654, 511)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.XML_file_txt = QLineEdit(Form)
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

        self.Load_pvxml_btn = QPushButton(Form)
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


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(100, 40))
        self.label_5.setMaximumSize(QSize(100, 40))
        palette1 = QPalette()
        brush3 = QBrush(QColor(255, 85, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(0, 170, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush4)
        brush5 = QBrush(QColor(0, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_5.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(100, 40))
        self.label_8.setMaximumSize(QSize(100, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_8.setPalette(palette2)
        self.label_8.setFont(font1)
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setFrameShadow(QFrame.Sunken)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(100, 40))
        self.label_7.setMaximumSize(QSize(100, 40))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_7.setPalette(palette3)
        self.label_7.setFont(font1)
        self.label_7.setFrameShape(QFrame.NoFrame)
        self.label_7.setFrameShadow(QFrame.Sunken)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(100, 40))
        self.label_6.setMaximumSize(QSize(100, 40))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_6.setPalette(palette4)
        self.label_6.setFont(font1)
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setFrameShadow(QFrame.Sunken)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Beamline_cbx = QComboBox(Form)
        self.Beamline_cbx.addItem("")
        self.Beamline_cbx.setObjectName(u"Beamline_cbx")
        self.Beamline_cbx.setMinimumSize(QSize(100, 40))
        self.Beamline_cbx.setMaximumSize(QSize(160, 40))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.Beamline_cbx.setPalette(palette5)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.Beamline_cbx.setFont(font2)

        self.horizontalLayout.addWidget(self.Beamline_cbx)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.New_beamline_txt = QLineEdit(Form)
        self.New_beamline_txt.setObjectName(u"New_beamline_txt")
        self.New_beamline_txt.setMinimumSize(QSize(170, 40))
        self.New_beamline_txt.setMaximumSize(QSize(16777215, 40))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.New_beamline_txt.setPalette(palette6)
        self.New_beamline_txt.setFont(font)
        self.New_beamline_txt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.New_beamline_txt)

        self.Add_newbeamline_btn = QPushButton(Form)
        self.Add_newbeamline_btn.setObjectName(u"Add_newbeamline_btn")
        sizePolicy.setHeightForWidth(self.Add_newbeamline_btn.sizePolicy().hasHeightForWidth())
        self.Add_newbeamline_btn.setSizePolicy(sizePolicy)
        self.Add_newbeamline_btn.setMinimumSize(QSize(130, 40))
        self.Add_newbeamline_btn.setMaximumSize(QSize(100, 40))
        self.Add_newbeamline_btn.setFont(font)
        self.Add_newbeamline_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout.addWidget(self.Add_newbeamline_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.Instrument_txt = QLineEdit(Form)
        self.Instrument_txt.setObjectName(u"Instrument_txt")
        self.Instrument_txt.setMinimumSize(QSize(260, 40))
        self.Instrument_txt.setMaximumSize(QSize(16777215, 40))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.Instrument_txt.setPalette(palette7)
        self.Instrument_txt.setFont(font)
        self.Instrument_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Instrument_txt)

        self.PV_alias_txt = QLineEdit(Form)
        self.PV_alias_txt.setObjectName(u"PV_alias_txt")
        self.PV_alias_txt.setMinimumSize(QSize(260, 40))
        self.PV_alias_txt.setMaximumSize(QSize(16777215, 40))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.PV_alias_txt.setPalette(palette8)
        self.PV_alias_txt.setFont(font)
        self.PV_alias_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.PV_alias_txt)

        self.PV_name_txt = QLineEdit(Form)
        self.PV_name_txt.setObjectName(u"PV_name_txt")
        self.PV_name_txt.setMinimumSize(QSize(260, 40))
        self.PV_name_txt.setMaximumSize(QSize(16777215, 40))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.PV_name_txt.setPalette(palette9)
        self.PV_name_txt.setFont(font)
        self.PV_name_txt.setStyleSheet(u"border:2px;border-style:dashed;border-color: rgb(255, 0, 0);")
        self.PV_name_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.PV_name_txt)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.TableView = QTableView(Form)
        self.TableView.setObjectName(u"TableView")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.TableView.setPalette(palette10)
        self.TableView.setFont(font2)

        self.verticalLayout_4.addWidget(self.TableView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.Add_PV_btn = QPushButton(Form)
        self.Add_PV_btn.setObjectName(u"Add_PV_btn")
        sizePolicy.setHeightForWidth(self.Add_PV_btn.sizePolicy().hasHeightForWidth())
        self.Add_PV_btn.setSizePolicy(sizePolicy)
        self.Add_PV_btn.setMinimumSize(QSize(100, 40))
        self.Add_PV_btn.setMaximumSize(QSize(100, 40))
        self.Add_PV_btn.setFont(font)
        self.Add_PV_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_3.addWidget(self.Add_PV_btn)

        self.Update_btn = QPushButton(Form)
        self.Update_btn.setObjectName(u"Update_btn")
        sizePolicy.setHeightForWidth(self.Update_btn.sizePolicy().hasHeightForWidth())
        self.Update_btn.setSizePolicy(sizePolicy)
        self.Update_btn.setMinimumSize(QSize(100, 40))
        self.Update_btn.setMaximumSize(QSize(100, 40))
        self.Update_btn.setFont(font)
        self.Update_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_3.addWidget(self.Update_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.XML_file_txt.setText("")
        self.XML_file_txt.setPlaceholderText(QCoreApplication.translate("Form", u"XML file with PV names", None))
        self.Load_pvxml_btn.setText(QCoreApplication.translate("Form", u"LoadXML", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Beamline", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Instrument", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"PV alias", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"PV name", None))
        self.Beamline_cbx.setItemText(0, QCoreApplication.translate("Form", u"Eline20U2", None))

        self.New_beamline_txt.setText("")
        self.New_beamline_txt.setPlaceholderText(QCoreApplication.translate("Form", u"add NewBeamline", None))
        self.Add_newbeamline_btn.setText(QCoreApplication.translate("Form", u"Add Beamline", None))
        self.Instrument_txt.setText("")
        self.Instrument_txt.setPlaceholderText(QCoreApplication.translate("Form", u"Instrument name like PGM1", None))
        self.PV_alias_txt.setText("")
        self.PV_alias_txt.setPlaceholderText(QCoreApplication.translate("Form", u"Alias for PV name like GR_SET", None))
        self.PV_name_txt.setText("")
        self.PV_name_txt.setPlaceholderText(QCoreApplication.translate("Form", u"Input PV name", None))
        self.Add_PV_btn.setText(QCoreApplication.translate("Form", u"add PV", None))
        self.Update_btn.setText(QCoreApplication.translate("Form", u"update", None))
    # retranslateUi

