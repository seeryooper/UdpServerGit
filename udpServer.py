#!/usr/bin/python
#-*- coding:utf-8 –*-
# support utf-8 coding

from socket import *;
from time import ctime;
from time import sleep;
#import sys
#type = sys.getfilesystemencoding('utf-8')
# 使得 sys.getdefaultencoding() 的值为 'utf-8'  
#reload(sys)                      # reload 才能调用 setdefaultencoding 方法  
#sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

HOST = '';
PORT = 8000;
BUFSIZ = 1024;
ADDR = (HOST, PORT);

udpServer = socket(AF_INET, SOCK_DGRAM);
udpServer.bind(ADDR);
#sdata = "CREATE TABLE 'table_DetailSet' ('ID'  INTEGER NOT NULL, 'FrameID'  INTEGER NOT NULL,  'DTitle'  TEXT NOT NULL, 'DType'  INTEGER NOT NULL, 'mSelection'  INTEGER NOT NULL,  'MSwitchVal'  INTEGER, 'selectName'  TEXT, 'Factor'  REAL NOT NULL, 'Offset'  REAL  NOT NULL, 'DDirection'  INTEGER NOT NULL, 'BitStart'  INTEGER NOT NULL, 'BitLen'   INTEGER NOT NULL, 'Minimum'  REAL NOT NULL, 'Maximum'  REAL NOT NULL);";
sdata = "<<<<<<<<=====================================================>>>>>>>>";

SendCount = 1000;
ReceiveCount = 0;
SleepTime = 0.01;

'''
while True:
    print '等待信息...';
    data, addr = udpServer.recvfrom(BUFSIZ);
    udpServer.sendto('[%s] %s' % (ctime(), data), addr);
    print '...收到并发送[%s]: %s：' % (addr, data);
    if data == 'quit':
        print '收到退出命令，服务结束！';
        break;
'''

while True:
    print '等待接收开始命令...';
    data, addr = udpServer.recvfrom(BUFSIZ);
    if data == 'quit':
        print '收到退出命令，服务结束！';
        break;
    elif data == 'start':
        tSendCount = SendCount;
        print "=====================开始发%s条数据=======================" % (SendCount,);
        while tSendCount > 0:
            udpServer.sendto(sdata.decode('utf-8'), addr);
            tSendCount = tSendCount - 1;
            sleep(SleepTime);
        print "=====================%s条数据发送结束=======================" % (SendCount,);
        #break;
    else:
        #udpServer.sendto('[%s] %s' % (ctime(), data), addr);
        #udpServer.sendto('[%s] %s' % (ctime(), data.decode('utf-8').encode(type)), addr);
        #print '...收到并发送[%s]: %s：' % (addr, data);
        ReceiveCount = ReceiveCount + 1
        print '收到%s条UDP信息....' % ReceiveCount;
    #print '此轮没有收到数据...';

udpServer.close();
