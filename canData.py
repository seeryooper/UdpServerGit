#!/usr/bin/python
# -*- coding:utf-8 -*- 

import os, logging
import sqlite3
from sqlsentence import sqlSentence,otherGlobal

class canDataDefine(object):
    '''
    the class to save receive CAN information
    '''
    
    #fdir = u'/home/data/sqlitedata'
    #ogbl = otherGlobal()
    fdir = otherGlobal.fdir
    isdbok = False
    fpath = ''
    errmsg = ''

    def __init__(self, sn, proname, cdata):
        self.sn = sn
        self.proname = proname
        self.cdata = cdata

    def openDb(self):
        '''
            1. folder operation, get folder path, if not exists, create it
            2. get sqlite file path
            3. open sqlite file
        '''

        sdir = os.path.join(self.fdir, self.proname)
        if not os.path.exists(sdir):
            os.makedirs(sdir)
            logging.info('Create dir:%s successed!' % sdir)
        filename = self.sn + ".db"
        self.fpath = os.path.join(sdir, filename)
        try:
            self.conn = sqlite3.connect(self.fpath)
            self.isdbok = True
            logging.info('open sqlite file:%s successed!' % self.fpath)
            return self.prepareDb()
        except:
            logging.error('open sqlite file:%s failed!' % (self.fpath))
            return False
    
    def prepareDb(self):
        if self.isdbok:
            '''
            sqlstr = u"SELECT COUNT(*) FROM sqlite_master where type='table' and name='table_DetailSet';"
            sqlcreate = u"CREATE TABLE 'table_DetailSet' ('ID'  INTEGER NOT NULL, 'FrameID'  INTEGER NOT NULL, 'DTitle'  TEXT NOT NULL, 'DType'  INTEGER NOT NULL, 'mSelection'  INTEGER NOT NULL, 'MSwitchVal'  INTEGER, 'selectName'  TEXT, 'Factor'  REAL NOT NULL, 'Offset'  REAL NOT NULL, 'DDirection'  INTEGER NOT NULL, 'BitStart'  INTEGER NOT NULL, 'BitLen'  INTEGER NOT NULL, 'Minimum'  REAL NOT NULL, 'Maximum'  REAL NOT NULL);"
            sqlsave = u"insert into table_DetailSet values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            '''
            sqlSen = sqlSentence()
            sqlstr = sqlSen.tableExistSelect('table_DetailSet')
            sqlcreate = sqlSen.sqlcreate
            sqlsave = sqlSen.tableInsertPrepare('table_DetailSet', 14)
            cur = self.conn.cursor()
            cur.execute(sqlstr)
            self.conn.commit()
            rval = cur.fetchone()
            if len(rval) == 1:
                if rval[0] == 1:
                    logging.info('table_DetailSet exists!')
                else:
                    cur.execute(sqlcreate)
                    for data in self.cdata:
                        cur.execute(sqlsave, data)
                    self.conn.commit()
                    logging.info('table_DetailSet create successed!')
                logging.info('prapare sqlite db finished!')
                return True
            else:
                logging.error('operation db failed!')
                return False
                    
        else:
            return False

    def selectAll(self, tablename):
        sqlselect = 'select * from %s;' % tablename
        cur = self.conn.cursor()
        cur.execute(sqlselect)
        self.conn.commit()
        rval = cur.fetchall()
        for el in rval:
            for ee in el:
                if isinstance(ee, str):
                    print ee.encode("utf-8"),
                else:
                    print ee,
            print ''

    def closeDb(self):
        if self.isdbok:
            self.conn.close()
            self.isdbok = False
            logging.info('close sqlite file:%s successed!' % self.fpath)
            self.fpath = ''
            self.cdata = []
            
if __name__ == '__main__':
    cdata = [(1, 273, u'总电压', 1, 0, 0, '', 0.01, 0, 0, 0, 16, 0, 600),
             (2, 273, u'工作模式', 0, 0, 0, '', 1, 0, 0, 32, 8, 0, 0)] 
    cd = canDataDefine('171130002', '540_LMU', cdata)
    cd.openDb()
    cd.selectAll('table_DetailSet')
    cd.closeDb()
