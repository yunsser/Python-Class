#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from socket import *
import pickle
import time
import threading
from chat import ChatMsg


# In[ ]:


class SendThread(threading.Thread):
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc
        
    def run(self):
        while True:
            sMsg = input('입력: ') # 3/hello
            in_list = sMsg.split('/') # ['3', 'hello']
            chatmsg = None
            if len(in_list) == 1: # 모두에게 보내는 메세지
                chatmsg = ChatMsg(sMsg)
            elif len(in_list) ==2:
                n,msg = in_list
                chatmsg = ChatMsg(msg, to=int(n))
            elif len(in_list)==3: # 3/Hello/test.jpg
                n, msg, fname = in_list
                with open(fname, 'rb') as fin:
                    fdata = fin.read()
                    chatmsg = ChatMsg(msg, to=int(n), attach=fdata)
                    print('보내는 파일크기: ', len(chatmsg.attach))
            self.soc.send(pickle.dumps(chatmsg))
            # chatmsg = pickle.dumps(ChatMsg(sMsg))
            # self.soc.send(chatmsg)


# In[ ]:


clientSock = socket(AF_INET,SOCK_STREAM) # 소켓 생성
clientSock.connect(('127.0.0.1', 1122)) # 서버에 접속 (1024 이후 서버)

SendThread(clientSock).start()

while True:
    msg = clientSock.recv(40000)
    chatmsg = pickle.loads(msg)
    print(chatmsg)
    if chatmsg.attach:
        print('수신된 파일크기: ', len(chatmsg.attach))
        # print(pickle.loads(msg))
        
        with open('copy.jpg', 'wb') as fout:
            fout.write(chatmsg.attach)
            print('파일저장 성공')

print('클라이언트 종료...')


# In[ ]:


n,msg,fname = '3/msg/fname'.split('/')
with open('test.jpg', 'rb') as fin:
    img_data = fin.read()
    # print(type(img_data))
    ChatMsg(msg, to=int(n), attach=img_data)
    
print('이미지 로드 완료')

