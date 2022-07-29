from re import S
import time, random, sys, os, math, datetime, traceback
from bs4 import Tag
import pandas as pd
from PySide6.QtCore import Qt,Signal,Slot,QTimer
from PySide6.QtWidgets import QTreeView,QTreeWidget,QTreeWidgetItem,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont,QBrush
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox
    
#import UI
from UI.UI_PlotPVs_main import Ui_MainWindow
from UI.PV_Monitor_Widget import PVMonitor

class MultiPVmonitor(QMainWindow,Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MultiPVmonitor,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Multi PVnames monitor')
        # monitor name
        self.pvmonitors_dict={}
        self.pvmonitors_count=0
        self.PV_mdi.setBackground(QBrush(Qt.lightGray))
    
    @Slot()
    def on_Add_pv_btn_clicked(self):
        pvname=self.PV_name_txt.text()
        tagname=self.Tag_name_txt.text()
        print(f'get pvname: {pvname}')
        if pvname not in self.pvmonitors_dict:
            self.pvmonitors_count+=1
            self.pvmonitors_dict[pvname]=PVMonitor(PVname=pvname,TagName=tagname)
            self.PV_mdi.addSubWindow(self.pvmonitors_dict[pvname])
            self.pvmonitors_dict[pvname].show()
            self.pvmonitors_dict[pvname].close_sig.connect(self.close_pvmonitor)
        else:
            print(f'already have monitor: {pvname}')

    @Slot(str)
    def close_pvmonitor(self,pvname):
        print(f'will close pvmonitor: {pvname}')
        self.pvmonitors_dict[pvname].close()
        self.pvmonitors_dict.pop(pvname,0)
        self.pvmonitors_count-=1

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