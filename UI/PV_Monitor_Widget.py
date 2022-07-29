from calendar import c
from epics import ca, caget, cainfo, camonitor, caput, PV, camonitor_clear, get_pv
import time, random, sys, os, math, datetime, traceback
import pandas as pd
from PySide6.QtCore import Qt,Signal,Slot,QTimer
from PySide6.QtWidgets import QTreeView,QTreeWidget,QTreeWidgetItem,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox
# matplotlib
from matplotlib.backends.backend_qtagg import(FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

# UI import
from UI_PV_monitor import Ui_Form

def get_timestamp():
    """ get current date time, as accurate as milliseconds

        Args: None

        Returns:
            str type
            eg: "2018-10-01 00:32:39.993176"
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

class PVMonitor(QWidget,Ui_Form):
    """Monitor a EPICS PV name
    should provide a PVname
    example: PVMonitor(pvname='example')
    """
    close_sig=Signal(str)
    
    def __init__(self,parent=None,PVname=None,TagName=None,):
        super(PVMonitor,self).__init__()
        self.pvname=PVname
        self.tagname=TagName if TagName else PVname
        self.setupUi(self)
        self.setWindowTitle(f'Monitoring {PVname}')
        self.monitoring_flag=False
        self._pv=''
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_time)
        # for data list
        self.pv_changed_Num:int=0
        self.pv_value_list=list()
        self.pv_num_list=list()
        self.pv_timestamps=list()
        self.__init__matplotlib()
        self.timer.start(500)

    @Slot()
    def update_time(self):
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.Time_stamp_label.setText(timestamp)
# **************************************VerTicaL@zlm**************************************
#  start of pv value part

    @Slot()
    def on_Start_monitor_btn_clicked(self):
        if not self.monitoring_flag:
            self._pv=PV(self.pvname,callback=self.pv_value_changed,connection_timeout=5)
            try:
                if self._pv.connect(timeout=5):
                    value=self._pv.get()
                    if value:
                        # self.pv_value_list.append(float(value))
                        # self.pv_changed_Num+=1
                        # self.pv_num_list.append(self.pv_changed_Num)
                        # self.pv_timestamps.append(get_timestamp())
                        self.PV_value_input.setText(str(value))
                else:
                    self.PV_name_label.setText(f'{self.pvname} not found')
            except Exception as e:
                print(traceback.format_exc() + str(e))
            else:
                self.monitoring_flag=True
                self.PV_name_label.setText(f'{self.pvname} Monitor')
            finally:
                print(f'end PV:{self.pvname} set')

    def pv_value_changed(self,pvname=None,value=None,**kw):
        """
        read PV value back
        update and plot
        """
        if value:
            self.PV_value_input.setText(str(value))
            timestamp=get_timestamp()
            self.pv_changed_Num+=1
            self.pv_value_list.append(float(value))
            self.pv_num_list.append(self.pv_changed_Num)
            self.pv_timestamps.append(get_timestamp())
            if self.pv_changed_Num>100:
                num_list=self.pv_num_list[-100:]
                value_list=self.pv_value_list[-100:]
                timestamps=self.pv_timestamps[-100:]
            else:
                num_list=self.pv_num_list
                value_list=self.pv_value_list
                timestamps=self.pv_timestamps
            # plot the changes
            if self.Y_change_cbx.currentIndex()==0:
                self.plot_PV_data(num_list,value_list,self.pvname,'ChangeNum')
            else:
                temp_timestamps=pd.Series(timestamps)
                pd_timestamps=pd.to_datetime(temp_timestamps)
                pd_value_list=pd.Series(value_list)
                self.plot_PV_data(pd_timestamps,pd_value_list,self.pvname,'timestamp')

    @Slot()
    def on_Stop_monitor_btn_clicked(self):
        if self.monitoring_flag:
            self.monitoring_flag=False
            self._pv.remove_callback(0)

   #  end of pv value part
# **************************************VerTicaL@zlm**************************************

# **************************************VerTicaL@zlm**************************************
    #  start of pv plot part by matplotlib
    def __init__matplotlib(self):
        """Initialize matplotlib plot part
        """
        Figure_Canvas=FigureCanvas(Figure(figsize=(4,3)))
        self.verticalLayout_plot.addWidget(Figure_Canvas)
        self.verticalLayout_plot.addWidget(NavigationToolbar(Figure_Canvas,self))
        self.data_fig_ax=Figure_Canvas.figure.subplots()
        
    def plot_PV_data(self, x_list: list, y_list: list, x_name: str, y_name: str):
        """
        plot any x_list and y_list data,and set the Axis name x_name,y_name
        :param x_list:
        :param y_list:
        :param x_name:
        :param y_name:
        :return:
        """
        # plot
        self.data_fig_ax.cla()
        self.data_fig_ax.plot(x_list, y_list, marker='o', markersize=2, markerfacecolor='orchid',
                                   markeredgecolor='orchid', linestyle='-', color='c')
        self.data_fig_ax.set_xlabel(x_name, fontsize=12, color='m')
        self.data_fig_ax.set_ylabel(y_name, fontsize=12, color='m')
        self.data_fig_ax.set_title(self.tagname,color='#ff5500')
        self.data_fig_ax.figure.autofmt_xdate(rotation=25)
        self.data_fig_ax.figure.canvas.draw()

#  end of pv plot part by matplotlib
# **************************************VerTicaL@zlm**************************************
    

# **************************************VerTicaL@zlm**************************************
    #  start of closeEvent
    
    def closeEvent(self, event):
        if self.monitoring_flag:
            self.monitoring_flag=False
            self._pv.remove_callback(0)
            #event.accept()
            self.close_sig.emit(self.pvname)
        elif not self.monitoring_flag:
            #event.accept()
            self.close_sig.emit(self.pvname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PVMonitor(PVname='LiminZhou:ai1',TagName='LiminZhou:ai1')
    win.show()
    sys.exit(app.exec())





