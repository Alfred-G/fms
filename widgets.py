# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:00:30 2016

@author: Alfred
"""
from PyQt5.QtWidgets import QLabel, QApplication, QMenu
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QCursor


class Exhibit(QLabel):
    OnClicked = pyqtSignal([int, int], [int, str])
    OnClickedCtrl = pyqtSignal([int, int], [int, str])
    OnClickedShift = pyqtSignal([int, int], [int, str])
    OnDblClicked = pyqtSignal([int, int], [int, str])
    OnDblClickedCtrl = pyqtSignal([int, int], [int, str])
    
    def __init__(self, menu=None):
        super(Exhibit, self).__init__()
        self.setFixedWidth(220)
        self.setMinimumHeight(150)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if (QApplication.keyboardModifiers() == Qt.ControlModifier):
                self.OnClickedCtrl.emit(event.x(), event.y())
            elif (QApplication.keyboardModifiers() == Qt.ShiftModifier):
                self.OnClickedShift.emit(event.x(), event.y())
            else:
                self.OnClicked.emit(event.x(), event.y())
            event.accept()
        elif event.button() == Qt.RightButton:
            self.OnClicked[int, str].emit(event.x(), str(event.y()))
            event.accept()  
        else:  
            super(Exhibit, self).mousePressEvent(self, event)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:  
            if (QApplication.keyboardModifiers() == Qt.ControlModifier):
                self.OnDblClickedCtrl.emit(event.x(), event.y())
            else:
                self.OnDblClicked.emit(event.x(), event.y())
            event.accept()  
        elif event.button() == Qt.RightButton:
            self.OnDblClicked[int, str].emit(event.x(), str(event.y()))
            event.accept()  
        else:  
            super(Exhibit,self).mouseDoubleClickEvent(self, event)
