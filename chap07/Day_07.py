#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * CountDownThread

# In[4]:


import threading
import time
import datetime

class CountDownThread(threading.Thread):
    def __init__(self,name,num):
        threading.Thread.__init__(self)
        self.name=name
        self.num=num
        print(name, 'instanciated')
        self.daemon=True

    def run(self):
        print(self.name, '쓰레드 시작')
        while True:
            self.num-=1
            print(self.name, '->', self.num)
            if self.num==0:
                print(self.name+'쓰레드 종료')
                break
            time.sleep(1) # 1초 쉼


# In[6]:


num = input('카운트 다운 수 입력: ')
CountDownThread(num, int(num)). start()


# ### Client_Socket

# ### Server_Socket
