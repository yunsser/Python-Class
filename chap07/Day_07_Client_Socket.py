#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 서버에 접속, 데이터 송수신
# 서버는 클라이언트 접속 대기 상태로 존재해야 함
# 서버는 특정 클라이언트 간의 통신 중개 역활


# In[ ]:


from socket import *
import pickle
import time
from chat import ChatMsg


# In[ ]:


clientSock = socket(AF_INET,SOCK_STREAM) # 소켓 생성
clientSock.connect(('127.0.0.1', 1122)) # 서버에 접속 (1024 이후 서버)

msg = clientSock.recv(1024) # 서버 데이터 수신 대기 (데이터가 안와서 block)
print(pickle.loads(msg))
# print(msg.decode('utf-8')) # 서버로부터 수신된 데이터를 화면에 표시

# clientSock.send('클라이언트 메세지'.encode('utf-8'))
# clientSock.send('클라이언트에서 전하는 말')
chatmsg = ChatMsg('클라이언트에서 전하는 말')
clientSock.send(pickle.dumps(chatmsg))

time.sleep(1)
clientSock.close()
print('클라이언트 종료...')


# In[ ]:


# 서버에서 수신되는 메시지는 루프를 사용하여 대기한다
# 클라이언트는 임의의 시기에 메시지를 서버로 전달가능해야 한다

