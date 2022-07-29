import PySide6,sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
    
from PV_multiMonitor import *

"""Main entrance  

Start Project program
"""

"""
for bat file:

@echo off
E:
cd {current directory}
start python main.py
pause

"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MultiPVmonitor()
    win.show()
    sys.exit(app.exec())