#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from socket import *
import time
import pickle
import threading

from chat import ChatMsg


# In[ ]:


class ChatThread(threading.Thread):
    
    def __init__(self, soc, addr, num, soc_dict):
        threading.Thread.__init__(self)
        print('ChatThread 시작됨')
        self.soc = soc
        self.addr = addr
        self.num = num
        self.soc_dict = soc_dict
        # self.soc_list = soc_list

    def run(self):
        msg = ChatMsg('서버 접속 성공')
        self.soc.send(pickle.dumps(msg))
        rem_idx = -1
        
        while True:
            try:
                msg = self.soc.recv(40000) # 오류가 생기면 except 오류 발생
                chatmsg = pickle.loads(msg)
                if chatmsg.to:
                    soc_dict[chatmsg.to].send(msg)
                else:
                    for i,s in self.soc_dict.items():
                        if s is self.soc:
                            rem_idx = i
                            continue
                        s.send(msg)
            except:
                print(str(self.addr)+ ' 퇴장') # 소켓 끊김
                del self.soc_dict[self.num]
                for i,s in self.soc_dict.items():
                # self.soc_list.remove(self.soc)
                # for s in self.soc_list:
                    # if s is self.soc:
                        # continue
                    s.send(pickle.dumps(ChatMsg(str(self.addr)+'님 퇴장')))
                break # while 문장을 벗어남
        print('ChatThread 종료')


# In[ ]:


serverSock = socket(AF_INET, SOCK_STREAM) # 소켓 생성
serverSock.bind(('',1122))  # ip주소/포트번호
serverSock.listen(1) # 동시접속자를 1명으로 제한

# soc_list = []
soc_dict= {}
num = 0

while True:
    print('서버 대기중...')
    soc, addr = serverSock.accept() # 클라이언트 접속시까지 대기함
    # soc_list.append(soc)
    # ChatThread(soc,addr, soc_list).start()
    num += 1 # 고유번호 지정
    soc_dict[num] = soc # [num] = key , soc = value
    ChatThread(soc, addr, num, soc_dict).start()
    
print('서버 종료....')

