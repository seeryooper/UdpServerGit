#!/usr/bin/python
#coding:utf-8

class sqlSentence(object):
    '''
        define the sqlite3 operation sentence
    '''
    def __init__(self):
        pass

    def tableExistSelect(self, tablename):
        return u"SELECT COUNT(*) FROM sqlite_master where type='table' and name='%s';" % tablename

    # create table_DetailSet
    sqlcreate = u"CREATE TABLE 'table_DetailSet' ('ID'  INTEGER NOT NULL, 'FrameID'  INTEGER NOT NULL, 'DTitle'  TEXT NOT NULL, 'DType'  INTEGER NOT NULL, 'mSelection'  INTEGER NOT NULL, 'MSwitchVal'  INTEGER, 'selectName'  TEXT, 'Factor'  REAL NOT NULL, 'Offset'  REAL NOT NULL, 'DDirection'  INTEGER NOT NULL, 'BitStart'  INTEGER NOT NULL, 'BitLen'  INTEGER NOT NULL, 'Minimum'  REAL NOT NULL, 'Maximum'  REAL NOT NULL);"

    def tableInsertPrepare(self, tablename, num):
        str_header = u"insert into %s values(" % tablename
        str_end = u")"
        str_content = ""
        for i in range(num):
            str_content = u"?" if str_content == "" else u"%s,?" % str_content
        return str_header + str_content + str_end

class otherGlobal(object):
    '''
        other global variables define
    '''
    fdir = u'/home/data/sqlitedata'

if __name__ == "__main__":
    sqlS = sqlSentence()
    print(sqlS.tableExistSelect("table_DetailSet"))
    print(sqlS.sqlcreate)
    print(sqlS.tableInsertPrepare("table_DetailSet", 14))
    
