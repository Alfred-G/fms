# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 18:45:57 2016

@author: Alfred
"""
import sqlite3
import traceback


class sqlite_database():
    
    def __init__(self,db):
        self.db=db
        
    def _cnx(self):
        cnx=sqlite3.connect(self.db['path'])
        return cnx
    
    def execute(self,sql_state):
        cnx=self._cnx()
        cursor=cnx.cursor()
        rst=[]
        try:
            cursor.execute(sql_state)
            if sql_state[:6]=='select':
                rst=cursor.fetchall()
            else:
                cnx.commit() 
        except:
            traceback.print_exc()
            print(sql_state)
        cursor.close()
        cnx.close()
        return rst
        
    def execute_many(self,sql_state,data_list):
        cnx=self._cnx()
        cursor=cnx.cursor()

        try:
            cursor.executemany(sql_state,data_list)
            cnx.commit()
            print('DB Operated')
        except:
            traceback.print_exc()
            print(sql_state)

        cursor.close()
        cnx.close()
        return []
    
    def insert(self,tbl,data_list):
        flds, pk = self.db['tbs'][tbl]

        exist_rst = self.execute('select %s from %s'%(pk,tbl))
        exist_rst = set([i[0] for i in exist_rst])
        
        insert_set = []
        update_set = []
        for i in data_list:
            i_pk = i.get(pk,'')
            if not i_pk:
                continue
            if i_pk in exist_rst:
                update_set.append(i)
            else:
                insert_set.append(i)
                
        sql_state = 'insert into %s(%s) values(%s)'\
            %(tbl,','.join(flds),','.join(['?']*len(flds)))
        pool=[]
        for i in insert_set:
            pool.append([i.get(i2,'') for i2 in flds])
            if pool and len(pool)%200==0:
                self.execute_many(sql_state,pool)
        if pool:
            self.execute_many(sql_state,pool)
        
        sql_state='update %s set %s=? where %s=?'\
            %(tbl,'=?,'.join(flds),pk)
        pool=[]
        for i in update_set:
            pool.append([i.get(i2,'') for i2 in flds])
            if pool and len(pool)%200==0:
                self.execute_many(sql_state,pool)
        if pool:
            self.execute_many(sql_state,pool)