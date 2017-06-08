# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:35:41 2017

@author: paul
"""

import sys
use_pyqt = None

#==============================================================================
# try if PyQt4 is already loaded
#==============================================================================
if 'PyQt4' in sys.modules:
    use_pyqt = 4

else:
    try:
        import PyQt5
        use_pyqt = 5
    except ImportError:
        import PyQt4
        use_pyqt = 4

#==============================================================================
# PyQt4       
#==============================================================================
if use_pyqt == 4:
    from PyQt4.QtGui import QAction, QApplication, QDialog, QFileDialog, \
        QGraphicsItem, QGraphicsPathItem, QGraphicsScene, QGraphicsTextItem, \
        QGraphicsView, QGridLayout, QHBoxLayout, QLabel, QLineEdit, \
        QListWidget, QMainWindow, QMenu, QMessageBox, QPushButton, \
        QSpinBox, QTabWidget, QVBoxLayout, QWidget

    from PyQt4.QtGui import QPrinter, QPrintDialog

    from PyQt4.QtGui import QDrag, QIcon, QImage, QPainter, QPainterPath, \
        QPen, QTransform
        
    from PyQt4 import QtCore
        

#==============================================================================
# PyQt5       
#==============================================================================
elif use_pyqt == 5:
    from PyQt5.QtWidgets import QAction, QApplication, QDialog, QFileDialog, \
        QGraphicsItem, QGraphicsPathItem, QGraphicsScene, QGraphicsTextItem, \
        QGraphicsView, QGridLayout, QHBoxLayout, QLabel, QLineEdit, \
        QListWidget, QMainWindow, QMenu, QMessageBox, QPushButton, \
        QSpinBox, QTabWidget, QVBoxLayout, QWidget

    from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

    from PyQt5.QtGui import QDrag, QIcon, QImage, QPainter, QPainterPath, \
        QPen, QTransform

    from PyQt5 import QtCore
        
#==============================================================================
# no PyQt found
#==============================================================================
else:
    raise Exception('No PyQt4 or PyQt5 found')