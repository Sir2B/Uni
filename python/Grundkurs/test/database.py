#!/usr/bin/env python
 
 
import MySQLdb
from _mysql_exceptions import *
 
 
class DataBase:
 
 
    def __init__(self,host,user,db,db_table,passwd=''):
       
        try:
            self.conn=MySQLdb.connect(host=host,
                                      user=user,
                                      db=db,
                                      passwd=passwd)
   
             
        except OperationalError, msg:
            print msg[1]
 
        self.db_table_cols=self.get_data("show columns from %s"%db_table)
 
   
    def get_data(self,action):
 
        cursor=self.conn.cursor()
        cursor.execute(action)
        result=cursor.fetchall()
        cursor.close()
        return result
 
 
    def set_data(self,action):
 
        cursor=self.conn.cursor()
        cursor.execute(action)
        cursor.close()
 
 
    def close(self):
        self.conn.close()
 
