# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:00:30 2016

@author: Alfred
"""
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, Qt


class Exhibit(QLabel):
    OnClicked = pyqtSignal([int, int], [int, str])
    OnDblClicked = pyqtSignal([int, int], [int, str])
    
    def __init__(self):
        super(Exhibit, self).__init__()
        self.setFixedWidth(220)
        self.setMinimumHeight(150)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  
            self.OnClicked.emit(event.x(), event.y())  
            event.accept()  
        elif event.button() == Qt.RightButton:  
            self.OnClicked[int, str].emit(event.x(), str(event.y()))
            event.accept()  
        else:  
            super(Exhibit, self).mousePressEvent(self, event)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:  
            self.OnDblClicked.emit(event.x(), event.y())  
            event.accept()  
        elif event.button() == Qt.RightButton:  
            self.OnDblClicked[int, str].emit(event.x(), str(event.y()))
            event.accept()  
        else:  
            super(Exhibit,self).mouseDoubleClickEvent(self, event)