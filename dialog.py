# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:02:37 2017

@author: Alfred
"""

from PyQt5.QtWidgets import QDialog,QLineEdit

s=QDialog()
a=QLineEdit(s)
a.returnPressed.connect(print)
s.show()
