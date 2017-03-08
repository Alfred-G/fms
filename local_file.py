# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:00:40 2017

@author: Alfred
"""
import os
from time import strftime, localtime
import threading
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
                    #f.join()
                    
                    """
                    file = {}
                    file['path'] = f.path.replace('\\','/')
                    file['ctime'] = strftime('%Y-%m-%d',
                        localtime(f.stat().st_ctime))
                    size = f.stat().st_size
                    file['size'] = round(size / 1024 / 1024, 2)
                    fobj = open(f.path, 'rb')
                    file['md5'] = get_md5(fobj.read())
                    fobj.close()
                    yield file
                    """

    @staticmethod
    def rename(src, dst):
        try:
            os.rename(src, dst)
            return True
        except:
            traceback.print_exc()
            return False

    @staticmethod
    def open_file(file_path, prefix = ''):
        try:
            full_path = os.path.join(prefix ,file_path)
            if os.path.exists(full_path):
                os.startfile(full_path)
            else:
                print(full_path)
        except:
            traceback.print_exc()
            print(file_path)


class threadsafe_iter:
    """Takes an iterator/generator and makes it thread-safe by
    serializing call to the `next` method of given iterator/generator.
    """
    def __init__(self, it):
        self.it = it
        self.lock = threading.Lock()

    def __iter__(self):
        return self

    def next(self):
        with self.lock:
            return self.it.next()