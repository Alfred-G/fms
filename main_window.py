# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:00:30 2016

@author: Alfred
"""
import os
import traceback

from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLabel, QLineEdit, QPushButton, QSlider, QFormLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from widgets import Exhibit


class MainWindow(QMainWindow):
    
    def __init__(self, flds):
        super(MainWindow, self).__init__()
        self.button_zone = ButtonZone()
        self.edit_zone = EditZone(flds)
        self.list_zone = ListZone()
        
        self.init_ui()
        
    def init_ui(self):
        centralWidget = QWidget()
        info_zone = QWidget()
        central_layout = QHBoxLayout()
        info_layout = QVBoxLayout()
        
        central_layout.addWidget(info_zone)
        central_layout.addWidget(self.list_zone)
        central_layout.setStretch(0, 1)
        central_layout.setStretch(1, 5)
        
        info_layout.addWidget(self.button_zone)
        info_layout.addWidget(self.edit_zone)
        info_layout.setStretch(0, 1)
        info_layout.setStretch(1, 15)
        
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(central_layout)
        info_zone.setLayout(info_layout)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowState(Qt.WindowMaximized)
        
class ListZone(QWidget):
    
    def __init__(self):
        super(ListZone, self).__init__()
        grid = QGridLayout()
        grid.setSizeConstraint(3)
        self.setLayout(grid)
        
        self.widget_list = [(QLabel(), Exhibit()) for i in range(42)]
        
        for i in enumerate(self.widget_list):
            idx = i[0]
            label = i[1][0]
            widget = i[1][1]
            grid.addWidget(widget, (idx // 7) * 2, idx % 7)
            label.setFixedWidth(220)
            grid.addWidget(label, (idx // 7) * 2 + 1, idx % 7)
        
    def print_screen(self, info_list):
        for i in zip(info_list, self.widget_list):
            text = i[0][0]
            pic = self.pixmap('D:/Python/fms%s' % i[0][1])
            label = i[1][0]
            widget = i[1][1]
            
            label.setText(text)
            if pic:
                widget.setPixmap(pic)
            else:
                widget.setText('暂无图片')
        if len(info_list) < len(self.widget_list):
            for i in self.widget_list[len(info_list): ]:
                i[0].setText(' ')
                i[1].setText(' ')
    
    @staticmethod
    def pixmap(pic_path):
        pic = ''
        if os.path.isfile(pic_path):
            try:
                pic = QPixmap(pic_path)
                if pic.width() < pic.height():
                    pic = pic.scaledToHeight(220)
                else:
                    pic = pic.scaledToWidth(220)
                return pic
            except:
                pass
        else:
            return pic

class EditZone(QWidget):
    
    def __init__(self, flds):
        super(EditZone, self).__init__()
        
        form = QFormLayout()
        self.setLayout(form)
        
        self.widget_dict = {i: QLineEdit() for i in flds}
        for i in flds:
            label = QLabel(i)
            widget = self.widget_dict[i]
            
            grid = QGridLayout()
            grid.addWidget(label, 0, 0)
            grid.addWidget(widget, 0, 1, 1, 2)
            widget.adjustSize()
            
            form.addRow(grid)

class ButtonZone(QWidget):
    
    def __init__(self):
        super(ButtonZone, self).__init__()
        self.sButton = QPushButton('Search')
        self.oButton = QPushButton('Order')
        self.rButton = QPushButton('Random')
        self.lineEdit = QLineEdit()
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(0)
        
        grid = QGridLayout()
        grid.addWidget(self.sButton, 4, 0)
        grid.addWidget(self.oButton, 4, 1)
        grid.addWidget(self.rButton, 4, 2)
        grid.addWidget(self.lineEdit, 0, 0, 3, 3)
        grid.addWidget(self.slider, 5, 0, 1, 3)
        self.setLayout(grid)