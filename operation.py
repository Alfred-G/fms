# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:21:17 2017

@author: Alfred
"""

def remove():
    db.execute('delete')
    opr.remove()
    
def rename():
    db.update()
    opr.rename()
    
def scan():
    db.insert(opr.scan)

def f_open():
    opr.open_file()
    
def crawl():
    db.insert(spd.crawl)
    
def modify():
    db.update()
    
def delete():
    db.execute('delte')
    
def tag():
    tag.modify()