import time, random, sys, os, math, datetime, traceback
sys.path.append('.')
import pandas as pd
from PySide6.QtCore import Qt,Signal,Slot,QTimer,QThread
from PySide6.QtWidgets import QTreeView,QLabel,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont,QBrush
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox,QSpacerItem,QSizePolicy

# UI Form
from UI.UI_input_PV_to_XML import Ui_Form
from collections import namedtuple
# input PV_with_XML func
from xml.etree import ElementTree as ET
from resource.PV_with_xml import add_PV_to_xml,read_PV_XML, pretty_xml,PV_info,PVinfo_To_pd,update_PV_Value
# pandas to dataTable
from Architect.Class_Pandas_data_QTable import PandasInQTable
"""
PV info format:

PV_info=namedtuple("PVinfo",field_names=["Beamline","Equipment","PValias","PVname"])

"""


class PVToXML(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super(PVToXML,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f'Interact PV info with XML')
        self.xml_file=None
        self.xml_root=None
        self.pd_PVinfo=None
        self.all_PVinfo=None
        self.pd_data_model=None

# **************************************VerTicaL@zlm**************************************
#  start of pv input part

    @Slot()
    def on_Update_btn_clicked(self):
        """
        1.acquire the input PV info 
        2.update xml file
        3.show PV info in table view
        """
        self.all_PVinfo=read_PV_XML(self.xml_file)
        updated_all_PVinfo=[]
        for pv_info in self.all_PVinfo:
            new_pv_info=update_PV_Value(pv_info)
            updated_all_PVinfo.append(new_pv_info)
        self.all_PVinfo=updated_all_PVinfo
        #print(f'PV_info:\n{self.all_PVinfo}')
        # update in table view
        self.update_pvinfo(self.all_PVinfo)
            
    
    @Slot()
    def on_Add_PV_btn_clicked(self):
        """
        1.acquire the input PV info 
        2.update xml file
        3.show PV info in table view
        """
        has_empty_input,add_PVinfo=self.acquire_PVinfo()
        if not has_empty_input and self.xml_root:
            add_PV_to_xml(self.xml_file,add_PVinfo)
            # read the updated xml file
            self.all_PVinfo=read_PV_XML(self.xml_file) 
            self.update_pvinfo(self.all_PVinfo)
        
    
    @Slot()
    def on_Load_pvxml_btn_clicked(self):
        """Load xml file with PV info
        """
        xml_file,filetype=QFileDialog.getOpenFileName(self, "Open xml file with PV info",os.getcwd(), "xmlfile(*.xml)")
        self.XML_file_txt.setText(xml_file)
        try:
            DOMtree=ET.parse(xml_file)
        except Exception as e:
            print(traceback.format_exc()+e)
        else:
            self.xml_root=DOMtree.getroot()
            self.xml_file=self.XML_file_txt.text()
            # read the xml file to get all PV info
            self.all_PVinfo=read_PV_XML(self.xml_file)
            self.update_pvinfo(self.all_PVinfo)
            

    def update_pvinfo(self,all_PVinfo:list[PV_info]):
        """Update PV info
        """
        if all_PVinfo:
            self.pd_PVinfo=PVinfo_To_pd(all_PVinfo)
            self.pd_data_model = PandasInQTable(self.pd_PVinfo)
            self.TableView.setModel(self.pd_data_model)
            self.TableView.setWindowTitle("all PV info")
            self.TableView.setAlternatingRowColors(True)
        
    
    def acquire_PVinfo(self):
        """acquire all input PV info
        """
        has_empty_input=False
        input_PVinfo=PV_info(None,None,None,None,None)
        input_lineEdit=(self.PV_alias_txt,self.Instrument_txt,self.PV_name_txt)
        for lineEdit in input_lineEdit:
            if not lineEdit.text():
                lineEdit.setStyleSheet("border:1.5px;border-style:dashed;border-color: rgb(255, 0, 0);")
                has_empty_input=True
        # no empty input    
        if not has_empty_input:
            input_PVinfo=PV_info(self.Beamline_cbx.currentText(),self.Instrument_txt.text(),self.PV_alias_txt.text(),self.PV_name_txt.text(),None)
            for lineEdit in input_lineEdit:
                lineEdit.setStyleSheet("")
        print(input_PVinfo)
        return has_empty_input,input_PVinfo
    
    @Slot()
    def on_Add_newbeamline_btn_clicked(self):
        """add new beamline
        """
        all_beamline =[]
        beamlines_num=self.Beamline_cbx.count()
        for i in range(beamlines_num):
            all_beamline.append(self.Beamline_cbx.itemText(i))
        newbeamline =self.New_beamline_txt.text()
        if newbeamline and newbeamline not in all_beamline:
            self.Beamline_cbx.addItem(newbeamline)
#  end of pv input part
# **************************************VerTicaL@zlm**************************************



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PVToXML()
    win.show()
    sys.exit(app.exec())
