# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:00:30 2016

@author: Alfred
"""
import os
import traceback

from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout,\
    QVBoxLayout, QGridLayout, QLabel, QSlider,QFormLayout, QStatusBar,\
    QTabWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from fms.widgets import Exhibit, InfoEdit



class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.button_zone = QWidget()
        self.edit_zone = EditZone()
        self.tab_zone = QTabWidget()

        self.init_ui()

    def init_ui(self):
        centralWidget = QWidget()
        info_zone = QWidget()
        central_layout = QHBoxLayout()
        info_layout = QVBoxLayout()
        
        # central layout
        central_layout.addWidget(info_zone)
        central_layout.addWidget(self.tab_zone)
        central_layout.setStretch(0, 1)
        central_layout.setStretch(1, 5)
        
        # info layout
        info_layout.addWidget(self.button_zone)
        info_layout.addWidget(self.edit_zone)
        info_layout.setStretch(0, 1)
        info_layout.setStretch(1, 15)
        
        # end
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(central_layout)
        info_zone.setLayout(info_layout)

        self.setStatusBar(QStatusBar())

        self.setGeometry(300, 300, 300, 150)
        self.setWindowState(Qt.WindowMaximized)



class ListZone(QWidget):
    """
    idx for info_list
    pos for widget_list
    page_num for slider
    
    prefix
    get 
    set
    """
    def __init__(self, name):
        super(ListZone, self).__init__()

        self.name = name
        self.info_list = []
        self.selected = [set(),None]

        self.widget_list = [(QLabel(), Exhibit()) for i in range(42)]
        grid = QGridLayout()
        grid.setSizeConstraint(3)
        self.setLayout(grid)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(0)
        self.slider.valueChanged.connect(self.changePage)

        for i in enumerate(self.widget_list):
            idx = i[0]
            label = i[1][0]
            widget = i[1][1]
            grid.addWidget(widget, (idx // 7) * 2, idx % 7)
            label.setFixedWidth(220)
            grid.addWidget(label, (idx // 7) * 2 + 1, idx % 7)
        grid.addWidget(self.slider, 12, 0, 1, 7)

    def get_info_list_selected(self, idx):
        return [self.info_list[i] for i in self.selected[0]]
    
    # screen display
    def print_screen(self, info_list):
        """
        list of tuple
        (f.id,b.id,p.id,text, pic)
        """
        # NORMAL PRINT
        for i in zip(info_list, self.widget_list):
            fid, bid, pid, text, pic = i[0]
            pic = self.pixmap('D:/Python/fms%s' % pic)
            label, widget = i[1]
            
            label.setText(text)
            if pic:
                widget.setPixmap(pic)
            else:
                widget.setText('暂无图片')

        # SET BLANK
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

    def info_list_slice(self, page_num):
        start = page_num * 42
        end = min((page_num + 1) * 42, len(self.info_list))
        return self.info_list[start: end]

    def changePage(self, event):
        try: 
            self.print_screen(self.info_list_slice(event.real))
            return 'Items: %s, Page: %s' \
                % (len(self.info_list), event.real + 1)
        except:
            traceback.print_exc()

    def get_current_page_num(self):
        return self.slider.value()


    # selection
    def set_label_color(self, pos, color, single):
        try:
            if single:
                for i in self.widget_list:
                    i[0].setStyleSheet('QLabel {color: black}')
            self.widget_list[pos][0]\
                .setStyleSheet('QLabel {color: %s}' % color)
        except:
            traceback.print_exc()
            print(pos)

    def get_current_widget_pos(self):
        widget = self.layout().indexOf(self.sender())
        r, c, w, h = self.layout().getItemPosition(widget)
        return int(r / 2 * 7) + c

    def basic_select(self, single):
        try:
            pos = self.get_current_widget_pos()
            self.set_label_color(pos, 'blue', single)

            idx = pos + self.get_current_page_num() * 42
            self.widget_list[pos][1].onSelected.emit(idx)
            return idx
        except:
            traceback.print_exc()

    def select(self):
        try:
            idx = self.basic_select(True)
            self.selected = [set([idx]), idx]
        except:
            traceback.print_exc()

    def select_ctrl(self):
        idx = self.basic_select(False)
        
        # widget has already been selected
        if idx in self.selected[0]:
            self.selected[0].remove(idx)
            if idx == self.selected[1]:
                self.selected[1] = max(self.selected[0])
            self.set_label_color(idx % 42, 'black', False)
        # widget yet not been selected
        else:
            self.selected[0].add(idx)
            self.selected[1] = idx

    def select_shift(self):
        idx = self.basic_select(False)
        # if no first item do nothing
        if not self.selected[1]:
            return

        # set label color
        start = min(self.selected[1] % 42, idx % 42) + 1
        end = max(self.selected[1] % 42, idx % 42) + 1
        if start == end:
            return
        for i in range(start, end):
            self.set_label_color(i, 'blue', False)
        
        # add to selected
        start = min(self.selected[1], idx) + 1
        end = max(self.selected[1], idx) + 1
        self.selected[0] = self.selected[0].union(range(start, end))
        self.selected[1] = idx


class EditZone(QWidget):
    """
    1
    """
    def __init__(self):
        super(EditZone, self).__init__()
        self.widget_dict = {}
        
        form = QFormLayout()
        self.setLayout(form)

    def add_widget(self, fld):
        if fld in self.widget_dict.keys():
            return
        
        self.widget_dict[fld] = InfoEdit()
        
        widget = self.widget_dict[fld]
        self.layout().addRow(fld, widget)

    def remove_widget(self, fld):
        if fld in self.widget_dict.keys():
            idx = self.layout().indexOf(self.widget_dict[fld])
            label = self.layout().itemAt(idx - 1)
            widget = self.layout().itemAt(idx)
            self.layout().removeItem(label)
            self.layout().removeItem(widget)
            label.widget().setParent(None)
            widget.widget().setParent(None)
            del self.widget_dict[fld]

    def print_text(self, fld, text):
        """
        list of tuple
        (fld, text)
        """
        if fld in self.widget_dict.keys():
            self.widget_dict[fld].setText(text)
            self.widget_dict[fld].setCursorPosition(0)
