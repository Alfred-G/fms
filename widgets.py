# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:00:30 2016

@author: Alfred
"""
from PyQt5.QtWidgets import QLabel, QApplication, QLineEdit
from PyQt5.QtCore import pyqtSignal, Qt


class Exhibit(QLabel):
    onClicked = pyqtSignal([int, int], [int, str])
    onClickedCtrl = pyqtSignal([int, int], [int, str])
    onClickedShift = pyqtSignal([int, int], [int, str])
    onDblClicked = pyqtSignal([int, int], [int, str])
    onDblClickedCtrl = pyqtSignal([int, int], [int, str])
    onSelected = pyqtSignal([int])

    def __init__(self):
        super(Exhibit, self).__init__()
        self.setFixedWidth(220)
        self.setMinimumHeight(150)

        #self.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.customContextMenuRequested.connect(self.item_menu)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if (QApplication.keyboardModifiers() == Qt.ControlModifier):
                self.onClickedCtrl.emit(event.x(), event.y())
            elif (QApplication.keyboardModifiers() == Qt.ShiftModifier):
                self.onClickedShift.emit(event.x(), event.y())
            else:
                self.onClicked.emit(event.x(), event.y())
            event.accept()
        elif event.button() == Qt.RightButton:
            self.onClicked[int, str].emit(event.x(), str(event.y()))
            event.accept()  
        else:  
            super(Exhibit, self).mousePressEvent(self, event)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:  
            if (QApplication.keyboardModifiers() == Qt.ControlModifier):
                self.onDblClickedCtrl.emit(event.x(), event.y())
            else:
                self.onDblClicked.emit(event.x(), event.y())
            event.accept()  
        elif event.button() == Qt.RightButton:
            self.onDblClicked[int, str].emit(event.x(), str(event.y()))
            event.accept()  
        else:  
            super(Exhibit,self).mouseDoubleClickEvent(self, event)

    """
    def item_menu(self):
        try:
            menu = QMenu()
            rename = QAction('Move', item)
            rename.triggered.connect(self.rename)
            remove = QAction('Delete', item)
            menu.addAction(rename)
            menu.addAction(remove)
            menu.exec_(QCursor.pos())
        except:
            traceback.print_exc()
    """

class InfoEdit(QLineEdit):
    onFocused = pyqtSignal()

    def __init__(self):
        super(InfoEdit, self).__init__()

    def mousePressEvent(self, event):
        self.onFocused.emit()
        event.accept()