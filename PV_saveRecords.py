import time, random, sys, os, math, datetime, traceback

from numpy import save
sys.path.append('.')
import pandas as pd
from epics import ca, caget, cainfo, camonitor, caput, PV, camonitor_clear, get_pv
from PySide6.QtCore import Qt,Signal,Slot,QTimer,QThread
from PySide6.QtWidgets import QTreeView,QLabel,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont,QBrush
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox,QSpacerItem,QSizePolicy

# UI Form
from UI.UI_PV_saveRecord import Ui_MainWindow
from collections import namedtuple
# input PV_with_XML func
from xml.etree import ElementTree as ET
from resource.PV_with_xml import add_PV_to_xml,read_PV_XML, pretty_xml,PV_info,PVinfo_To_pd,update_PV_Value,get_PVs_Value
# pandas to dataTable
from Architect.Class_Pandas_data_QTable import PandasInQTable
from Architect.Tools_funcs import SSRFBeamStatus,get_datetime,get_host_ip,createPath
# save path
DATA_PATH = os.getcwd()
save_path = os.path.join(DATA_PATH, 'save_data')
createPath(save_path)
today_folder=createPath(os.path.join(save_path,time.strftime('%Y-%m-%d', time.localtime())))
"""
PV info format:

PV_info=namedtuple("PVinfo",field_names=["Beamline","Equipment","PValias","PVname"])

"""

class RunQThread(QThread):
    """
    run any time consuming operation of func(*args,**kwargs)
    :argument can provide keyword args <timeout:float=1000.0>ms
    :return the signal will send function's return value in list form (return=funcs())
    Notice: if run exception occurs,will emit the <Exception info>
    """
    run_sig = Signal(list)

    def __init__(self, func, *args, timeout: float = 1000.0, **kwargs):
        super(RunQThread, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.run_flag = True
        self.run_time = timeout
        self.func = func
        self.result = None

    def run(self):
        t0 = time.time()
        #print('QThread start')
        while self.run_flag and time.time() - t0 < self.run_time:
            try:
                self.result = self.func(*self.args, **self.kwargs)
            except Exception as e:
                # print(e)
                error_info = traceback.format_exc() + str(e) + '\n'
                self.run_sig.emit([error_info])
            else:
                self.run_flag = False
                self.run_sig.emit([self.result])

    def __del__(self):
        self.run_time = False

class SavePVRecords(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(SavePVRecords,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f'save PV info into records')
        self.xml_file=None
        self.xml_root=None
        self.pd_PVinfo=pd.DataFrame()
        self.all_PVinfo=None
        self.pvname_list=[]
        self.pvalias_list=[]
        self.pd_data_model=None
        self.record_id=0


# **************************************VerTicaL@zlm**************************************  
#  start of pv record part

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
            self.create_pvRecord(self.all_PVinfo)

    
    def create_pvRecord(self,all_PVinfo:list[PV_info]):
        """create a new record based on all the PV_info from input
        Records form
        id  PValias1  PValias2 ....savetime
        0   value1       value2     timestamp

        Args:
            all_PVinfo (list[PV_info]): all the PV_info
        """
        if all_PVinfo:
            for idx,pv_info in enumerate(all_PVinfo):
                self.pvname_list.append(pv_info.PVname)
                self.pvalias_list.append(pv_info.PValias)
            self.pd_PVinfo=pd.DataFrame(columns=['id','status',*self.pvalias_list,'savetime'])
            self.get_new_record(self.pvname_list)
    
    def get_new_record(self,pvname_list:list):
        """get current values of all pv name in a Qthread
        Args:
            pvname_list (list): pv names
        """
        self.pvValue_Qthread=RunQThread(get_PVs_Value,pvname_list)
        self.pvValue_Qthread.run_sig.connect(self.update_pvRecords)
        self.pvValue_Qthread.start()
    
    @Slot(list)
    def update_pvRecords(self,record:list):
        pv_values=record[0]
        status_text=self.Status_txt.text()
        timestamp= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.pd_PVinfo.loc[self.record_id]=[self.record_id,status_text,*pv_values,timestamp]
        self.record_id+=1
        # set the model
        if not self.pd_PVinfo.empty:
            self.pd_data_model = PandasInQTable(self.pd_PVinfo)
            self.TableView.setModel(self.pd_data_model)
            self.TableView.setWindowTitle("all PV info")
            self.TableView.setAlternatingRowColors(True)

    @Slot()
    def on_Add_record_btn_clicked(self):
        """add a new record
        """
        if not self.pd_PVinfo.empty and self.pvname_list:
            self.get_new_record(self.pvname_list)

    @Slot()
    def on_Save_tofile_btn_clicked(self):
        """save pd data to excel file
        """
        file_in_path,filetype=QFileDialog.getSaveFileName(self, "save all records to excel file",today_folder, "excel file(*.xlsx)")
        usr_path = os.path.dirname(file_in_path)
        usr_file = os.path.basename(file_in_path)
        filename = usr_file.split('.')[0]
        self.save_pd_data(self.pd_PVinfo,usr_path,filename)
    
    @staticmethod
    def save_pd_data(pd_data: pd.DataFrame, path, filename: str):
        """
        save pandas DataForm data to excel/csv/json file by path/filename
        :param pd_data: pandas dataFrame
        :param path:
        :param filename:
        :return:
        """
        save_path = path
        if not os.path.isdir(path):
            save_path = os.getcwd()
        excel_file_path = os.path.join(save_path, filename + '.xlsx')
        # excel writer
        excel_writer = pd.ExcelWriter(excel_file_path)
        pd_data.to_excel(excel_writer)
        excel_writer.save()
        print(f'save to excel xlsx file {excel_file_path} successfully')
        # # csv file
        # csv_file_path = os.path.join(save_path, filename + '.csv')
        # pd_data.to_csv(csv_file_path)
        # print(f'save to csv file {csv_file_path} successfully')
        # # json file
        # json_file_path = os.path.join(save_path, filename + '.json')
        # pd_data.to_json(json_file_path)
        # print(f'save to json file {json_file_path} successfully')

#  end of pv record part
# **************************************VerTicaL@zlm**************************************  

# **************************************VerTicaL@zlm**************************************  
# close event handler
    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                            "QUIT",
                                            "Are you sure to exit?",
                                            QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            if not self.pd_PVinfo.empty:
                timestamp= time.strftime("%Y-%m-%d-%H", time.localtime())
                autosave_filename=f'autosave_{timestamp}_{self.record_id}'
                self.save_pd_data(self.pd_PVinfo,today_folder,autosave_filename)
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SavePVRecords()
    win.show()
    sys.exit(app.exec())