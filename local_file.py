# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:00:40 2017

@author: Alfred
"""
import os
from time import strftime, localtime
import traceback


class LocalFile():
    """
    1
    """
    @staticmethod
    def scan(path):
        for p, ds, fs in os.walk(path):
            for f in os.scandir(p):
                if f.is_file():
                    file = {}
                    file['path'] = f.path.replace('\\','/')
                    file['ctime'] = strftime('%Y-%m-%d',
                        localtime(f.stat().st_ctime))
                    size = f.stat().st_size
                    file['size'] = round(size / 1024 / 1024, 2)
                    yield file

    @staticmethod
    def rename(src, dst):
        if not os.path.isfile(src):
            print('ERROR: SRC FILE not exist\nsrc: %s' % src)
            return False
        elif os.path.isfile(dst):
            print('ERROR: DST FILE already exist\ndst: %s' % dst)
            return False
        elif not os.path.isdir(os.path.dirname(dst)):
            print('ERROR: DST DIR not exist\ndst: %s' % dst)
            return False
            
        try:
            os.rename(src, dst)
            return True
        except:
            traceback.print_exc()
            return False

    @staticmethod
    def open_file(path):
        try:
            if os.path.exists(path):
                os.startfile(path)
                return True
            else:
                print('ERROR: PATH not exist\npath: %s' % path)
                return False
        except:
            traceback.print_exc()
            print('path: %s' % path)
            return False
