from genericpath import isfile
import time, random, sys, os, math, datetime, traceback
import pandas as pd
from PySide6.QtCore import Qt,Signal,Slot,QTimer,QThread
from PySide6.QtWidgets import QTreeView,QLabel,QHBoxLayout,QHeaderView,QWidget,QMenu
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont,QBrush
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox,QSpacerItem,QSizePolicy

# matplotlib
from matplotlib.backends.backend_qtagg import(FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

# xml read
from resource.PV_with_xml import PV_info, read_PV_XML,PVinfo_To_pd,load_xml_pvinfo
#import UI
from UI.UI_PlotPVs_main import Ui_MainWindow
from UI.PV_Monitor_Widget import PVMonitor

# tool functions
from Architect.Tools_funcs import SSRFBeamStatus,get_datetime,get_host_ip,createPath
from Architect.Dict_DataFrame_Sqlite import dict_to_csv,dict_to_excel,dict_to_json,dict_to_SQLTable
# save path
DATA_PATH = os.getcwd()
save_path = os.path.join(DATA_PATH, 'save_data')
createPath(save_path)
# data base
SQLiteDB_path=createPath(os.path.join(save_path,'database'))

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

class MultiPVmonitor(QMainWindow,Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MultiPVmonitor,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Multi PVnames monitor')
        # monitor name
        self.pvmonitors_dict={}
        self.pvmonitors_count=0
        #self.PV_mdi.setBackground(QBrush(QColor(162, 178, 199)))
        
        self.__init__menu()
        self.__init__beam_status()
        self.__init_pv_xml()
    
    def __init__menu(self):
        self.statusLabel=QLabel(self)
        self.statusBar().addWidget(self.statusLabel)
        self.statusLabel.setStyleSheet("background-color: rgba(197, 255, 253, 20);font-size:15px;color:rgb(29, 187, 255)")
        self.statusLabel.setText('Welcome to PV monitor')
        self.IP_label.setText(f'Host IP:{get_host_ip()}')
        

# **************************************VerTicaL@zlm**************************************
#  start of pv monitor part    
        
    @Slot()
    def on_Add_pv_btn_clicked(self):
        pvname=self.PV_name_txt.text()
        tagname=self.Tag_name_txt.text()
        self.statusBar().showMessage(tagname,3000)
        self.Add_pv_plot(pvname,tagname)
    
    def Add_pv_plot(self,pvname,tag=None):
        print(f'get pvname: {pvname}')
        if pvname not in self.pvmonitors_dict:
            self.pvmonitors_count+=1
            self.pvmonitors_dict[pvname]=PVMonitor(PVname=pvname,TagName=tag)
            self.PV_mdi.addSubWindow(self.pvmonitors_dict[pvname])
            self.pvmonitors_dict[pvname].show()
            self.pvmonitors_dict[pvname].close_sig.connect(self.close_pvmonitor)
        else:
            print(f'already have monitor: {pvname}')
            self.statusLabel.setText(f'already have monitor: {pvname}')
            self.pvmonitors_dict[pvname].showMaximized()

    @Slot(str)
    def close_pvmonitor(self,pvname):
        print(f'will close pvmonitor: {pvname}')
        self.pvmonitors_dict[pvname].close()
        self.pvmonitors_dict.pop(pvname,0)
        self.pvmonitors_count-=1

#  end of pv monitor part    
# **************************************VerTicaL@zlm**************************************

# **************************************VerTicaL@zlm**************************************
#  start of beam status part    

    def __init__beam_status(self):
        self.SSRF_timer=QTimer()
        self.SSRF_timer_runFlag=False
        self.SSRF_timer.timeout.connect(self.get_SSRF_BeamStatus)
        # figure part
        Figure_Canvas=FigureCanvas(Figure(figsize=(10,3)))
        self.BeamStatus_VLayout.addWidget(Figure_Canvas)
        self.BeamStatus_VLayout.addWidget(NavigationToolbar(Figure_Canvas,self))
        self.SSRF_beam_ax=Figure_Canvas.figure.subplots()
        #data part
        self.SSRF_beamCurrent_list=[]
        self.SSRF_timestamps_list=[]
        self.SSRF_beam_num=0
        self.SSRF_epics_runflag=False
    
    @Slot()
    def on_actionSSRF_epics_triggered(self):
        pvname="SR-Bl:DCCT:CURRENT"
        tagname="SSRF BeamStatus"
        #self.statusBar().showMessage(tagname,3000)
        #self.Add_pv_plot(pvname,tagname)
        if not self.SSRF_epics_runflag:
            self.SSRF_epics_beamMonitor=PVMonitor(PVname=pvname,TagName=tagname)
            self.SSRF_epics_beamMonitor.show()
            self.BeamStatus_VLayout.addWidget(self.SSRF_epics_beamMonitor)
            self.SSRF_epics_runflag=True
        else:
            self.statusLabel.setText(f'SSRF epics beamstatus already on')

    
    @Slot()
    def on_actionSSRF_internet_triggered(self):
        print(f'start acquiring SSRF beam Status from internet')
        if not self.SSRF_timer_runFlag:
            self.SSRF_timer.start(5000)
            self.SSRF_timer_runFlag=True
        else:
            self.statusLabel.setText(f'SSRF beamstatus already on')
    
    @Slot()
    def get_SSRF_BeamStatus(self):
        try:
            self.SSRF_beamstatus_Qthread=RunQThread(SSRFBeamStatus)
            self.SSRF_beamstatus_Qthread.run_sig.connect(self.update_SSRF_BeamStatus)
            self.SSRF_beamstatus_Qthread.start()
        except Exception as e:
            print(traceback.format_exc()+e)
    
    @Slot(list)
    def update_SSRF_BeamStatus(self,beamstatus):
        """update SSRF beamstatus in left pannel
        """
        #print(f'beamstatus {beamstatus}')
        current=beamstatus[0][0]
        Current=round(current,2)
        timestamp=get_datetime()
        self.SSRF_beamCurrent_list.append(Current)
        self.SSRF_timestamps_list.append(timestamp)
        self.SSRF_beam_num+=1
        # update current
        IP_current=f'SSRF beam:{current}mA   Host IP:{get_host_ip()}'
        self.IP_label.setText(IP_current)
        # plot
        if self.SSRF_beam_num>100:
            current_list=self.SSRF_beamCurrent_list[-100:]
            timestamps=self.SSRF_timestamps_list[-100:]
        else:
            current_list=self.SSRF_beamCurrent_list
            timestamps=self.SSRF_timestamps_list
        temp_timestamps=pd.Series(timestamps)
        pd_timestamps=pd.to_datetime(temp_timestamps)
        pd_current_list=pd.Series(current_list)
        self.plot_beam_data(self.SSRF_beam_ax,pd_timestamps,pd_current_list,'Timestamp','Current(mA)',"SSRF Beam status")
    
    def plot_beam_data(self,axis, x_list: list, y_list: list, x_name: str, y_name: str,title:str=None):
        """ plot the beam current data
        
        Args:
            axis: matplotlib plot axis
            x_list: 
            y_list:
            x_name:
            y_name:
        
        """
        axis.cla()
        axis.fill_between(x_list, y_list, color="skyblue", alpha=0.5)
        axis.plot(x_list, y_list, marker='o', markersize=1, markerfacecolor='orchid',
                                   markeredgecolor='orchid', linestyle='-', color='skyblue')
        axis.set_xlabel(x_name, fontsize=12, color='m')
        axis.set_ylabel(y_name, fontsize=12, color='m')
        axis.set_title(title,color='#ff5500')
        axis.figure.autofmt_xdate(rotation=25)
        axis.figure.canvas.draw()           
            
        
#  end of beam status part    
# **************************************VerTicaL@zlm**************************************


# **************************************VerTicaL@zlm**************************************
#  start of xml file part 
    def __init_pv_xml(self):
        self.pd_pvdata=pd.DataFrame()
        self.all_pv_info=[]
        self.all_beamlines={}
        self.add_beamlinePVs()
        self.actionLoadBeamline.triggered.connect(self.load_pvxml_file)
        
    def load_pvxml_file(self):
        xml_file, filetype = QFileDialog.getOpenFileName(self, "read xml file(xml)", './', '*.xml')
        if os.path.isfile(xml_file):
            self.add_beamlinePVs(xml_file)
                                                        
    
    def add_beamlinePVs(self,usr_xml_file:str=None):
        """add pv menu into PVtree
        PV_info=namedtuple("PVinfo",field_names=["Beamline","Equipment","PValias","PVname","PVvalue"])
        menu Beamline-Equiment-PValias
        Args:
            usr_xml_file (str, optional): _description_. Defaults to None.
        """
        xml_file= usr_xml_file if usr_xml_file and os.path.isfile(usr_xml_file) else "./resource/SSRF-Eline.xml"
        self.all_pv_info,self.pd_pvdata=load_xml_pvinfo(xml_file)
        beamline_list=[]
        #create menu Beamline-Equiment for all Beamline
        if not self.pd_pvdata.empty:
            for i in range(len(self.pd_pvdata)):
                beamline_list.append(self.pd_pvdata.loc[i,"Beamline"])
        beamline_set=set(beamline_list)
        print(beamline_set,beamline_list)
        for beamline in beamline_set:
            # create a menu for each beamline
            Beamline_menu = QMenu(f'{beamline}',self)
            self.menuPVTree.addAction(Beamline_menu.menuAction())
            self.all_beamlines[beamline]=Beamline_menu
        # add all pv info
        for pv_info in self.all_pv_info:
            self.add_pv_action(pv_info)
            
        
    def add_pv_action(self,pvinfo:PV_info):
        """add pv info to Ui action
        PV_info=namedtuple("PVinfo",field_names=["Beamline","Equipment","PValias","PVname","PVvalue"])
        Args:
            pvinfo (PV_info): _description_

        Returns:
            _type_: _description_
        """
        #create menu Beamline-Equiment-PValias action
        alias_pvname=f'{pvinfo.Equipment}-{pvinfo.PValias}'
        Equipment_alias_action=QAction(alias_pvname,self)
        
        Equipment_alias_action.objectName()
        #add menu and action
        self.all_beamlines[pvinfo.Beamline].addAction(Equipment_alias_action)
        # add trigger
        Equipment_alias_action.triggered.connect(lambda:self.Add_pv_plot(pvinfo.PVname,pvinfo.PValias))


#  end of xml file part 
# **************************************VerTicaL@zlm**************************************


# **************************************VerTicaL@zlm**************************************
    #  start of data save part 

    def routine_data_save(self,save_header:str='SSRFBeamStatus'):
         all_valid_data = self.get_full_data()
         cur_datetime=time.strftime("%Y-%m-%d-%H-%M", time.localtime())
         filename=f'{save_header}-{cur_datetime}N'
         today_folder=createPath(os.path.join(save_path,time.strftime('%Y-%m-%d', time.localtime())))
         self.save_all_data(all_valid_data,today_folder,filename)
        
    def get_full_data(self):
        """
        get all the data whcih is not empty
        """
        valid_full_data=dict()
        pv_data={"BeamCurrent":self.SSRF_beamCurrent_list,"timestamp":self.SSRF_timestamps_list}
        # get the valid scan data (not empty)
        for key, value in pv_data.items():
            if value:
                valid_full_data[key] = value
        return valid_full_data


    def save_all_data(self,full_data:dict,path,filename):
        """save all sensor data
        save to excel xlsx,json,csv and sqlite database
        Args:
            full_data[dict]: full data in dict
            path: save path
            filename: filename
        """
        if full_data and os.path.isdir(path):
            dict_to_csv(full_data, path, filename + '.csv')
            dict_to_excel(full_data, path, filename + '.xlsx')
            dict_to_json(full_data, path, filename + '.json')
            dict_to_SQLTable(full_data,filename, SQLiteDB_path, 'PVMonitorData.db')
            details=f'save to excel/csv/json files.\nFilename:{path+filename}\nSqlite database:{SQLiteDB_path}/SensorData.db\ntablename:{filename}'
            print(details)

#  end of data save part 
# **************************************VerTicaL@zlm**************************************
    
    def closeEvent(self, event):
        
        close = QMessageBox.question(self,"QUIT","Are you sure to exit?",
                                                   QMessageBox.Yes | QMessageBox.No)
        if close ==QMessageBox.Yes:
            self.routine_data_save(save_header="SSRFBeamStatus")
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MultiPVmonitor()
    win.show()
    sys.exit(app.exec())