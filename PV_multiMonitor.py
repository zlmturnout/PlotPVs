from re import S
import time, random, sys, os, math, datetime, traceback
from tkinter import N
import pandas as pd
from PySide6.QtCore import Qt,Signal,Slot,QTimer,QThread
from PySide6.QtWidgets import QTreeView,QLabel,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont,QBrush
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox,QSpacerItem,QSizePolicy

# matplotlib
from matplotlib.backends.backend_qtagg import(FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

#import UI
from UI.UI_PlotPVs_main import Ui_MainWindow
from UI.PV_Monitor_Widget import PVMonitor

# tool functions
from Architect.Tools_funcs import SSRFBeamStatus,get_datetime,get_host_ip
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
    
    @Slot()
    def on_actionSSRF_epics_triggered(self):
        pvname="SR-Bl:DCCT:CURRENT"
        tagname="SSRF BeamStatus"
        self.statusBar().showMessage(tagname,3000)
        self.Add_pv_plot(pvname,tagname)
    
    @Slot()
    def on_actionSSRF_internet_triggered(self):
        print(f'start acquiring SSRF beam Status from internet')
        if not self.SSRF_timer_runFlag:
            self.SSRF_timer.start(5000)
        else:
            self.statusLabel.setText(f'SSRF beamstatus already on')
    
    @Slot()
    def get_SSRF_BeamStatus(self):
        self.SSRF_beamstatus_Qthread=RunQThread(SSRFBeamStatus)
        self.SSRF_beamstatus_Qthread.run_sig.connect(self.update_SSRF_BeamStatus)
        self.SSRF_beamstatus_Qthread.start()
    
    @Slot(list)
    def update_SSRF_BeamStatus(self,beamstatus):
        """update SSRF beamstatus in left pannel
        """
        #print(f'beamstatus {beamstatus}')
        curret=beamstatus[0][0]
        
        if curret=='error':
            self.statusLabel.setText(f'can not acquire SSRF beamstatus')
        elif curret.split('mA')[0]:
            Current=round(float(curret.split('mA')[0]),2)
            timestamp=get_datetime()
            self.SSRF_beamCurrent_list.append(Current)
            self.SSRF_timestamps_list.append(timestamp)
            self.SSRF_beam_num+=1
            # update current
            IP_current=f'SSRF beam:{curret}   Host IP:{get_host_ip()}'
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
            self.plot_beam_data(self.SSRF_beam_ax,pd_timestamps,pd_current_list,'Timestamp','Current',"SSRF Beam status")
    
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


    def closeEvent(self, event):
        
        close = QMessageBox.question(self,"QUIT","Are you sure to exit?",
                                                   QMessageBox.Yes | QMessageBox.No)
        if close ==QMessageBox.Yes:
                event.accept()
        else:
                event.ignore() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MultiPVmonitor()
    win.show()
    sys.exit(app.exec())