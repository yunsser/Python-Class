#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from socket import *
import pickle
import time
from chat import ChatMsg


# In[ ]:


serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind(('', 1122))
serverSock.listen(1) # 동시 접속 클라이언트 1개

while True:
    print('서버 대기 중....')
    com_socket, addr = serverSock.accept() # 클라이언트가 접속시까지 대기함

print(str(addr), '에서 접속됨')
# msg = '서버에 접속됨'
# com_socket.send(msg.encode('utf-8')) # 바이트 단위, 텍스트를 바이트 데이터로 인코딩

msg = ChatMsg('서버에 접속됨')
com_socket.send(pickle.dumps(msg))

msg = com_socket.recv(1024)
chatmsg = pickle.loads(msg)
print(chatmsg)
# print(msg.decode('utf-8'))

time.sleep(1)
print('서버 종료....')


# ================================================================

# In[ ]:


from socket import *
import time
import pickle
import threading

from chat import ChatMsg


# In[ ]:


class ChatThread(threading.Thread):
    
    def __init__(self, soc, addr, soc_list):
        threading.Thread.__init__(self)
        print('ChatThread 시작됨')
        self.soc = soc
        self.addr = addr
        self.soc_list = soc_list

    def run(self):
        msg = ChatMsg('서버 접속 성공')
        self.soc.send(pickle.dumps(msg))
        while True:
            try:
                msg = self.soc.recv(1024) 
                for s in self.soc_list:
                    s.send(msg)
                # if s == self.soc:
                #     contiue
                # print(pickle.loads(msg))
                # self.soc.send(msg)
            except:
                print(str(self.addr)+ ' 퇴장')
                break
        print('ChatThread 종료')


# In[ ]:


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',1122))
serverSock.listen(1)

soc_list = []

while True:
    print('서버 대기중...')
    soc, addr = serverSock.accept() # 클라이언트 접속시까지 대기함
    soc_list.append(soc)
    ChatThread(soc,addr).start()
    
print('서버 종료....')

