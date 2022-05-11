#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * pickle모듈을 사용한 직렬화/역직렬화 응용 CRUD

# ### Serialization_Ex

# In[ ]:


from emp import Emp


# In[ ]:


import pickle


# In[ ]:


emp = Emp(11, 'Smith', '010-2394-5410')


# ### 객체 직렬화(Object Serialization)
# * 메모리상에 저장된 객체를 파일이나 네트워크로 전송할 때 필요함

# In[ ]:


# 객체 직렬화 (Serialization)
fw = open('empObj.pickle', 'wb')
pickle.dump(emp,fw)
fw.close()
print('객체 직렬화 성공')


# ### 역직렬화(De-Serialization)

# In[ ]:


fr = open('empObj.pickle', 'rb')
emp2 = pickle.load(fr)
fr.close()
print(emp2)
print(emp2.name)


# In[ ]:


emp == emp2 # emp.__eq__(emp2)


# In[ ]:


emplist = [Emp(11), Emp(12), Emp(13)]


# In[ ]:


fw = open('emplist.pickle', 'wb')
pickle.dump(emplist, fw)
fw.close()

print('리스트 직렬화 완료')


# In[ ]:


fr = open('emplist.pickle', 'rb')
emps = pickle.load(fr)
fr.close()

print(emps[0])
print('리스트 역직렬화 성공')


# In[ ]:


# 객체 > 텍스트 파일, 텍스트 > 객체 매핑
# 객체 > 객체, 객체 > 객체


# In[ ]:


# 프로그램이 시작되면 메뉴 6개가 표시된다
# 목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)
# 추가(a)하고 목록보기가 되도록 기능을 작성해보세요


# In[ ]:


import pickle
from emp import Emp


# In[ ]:


emplist = []


# In[ ]:


def save_emplist():
    saved = False
    try:
        with open('crud_list.pickle','wb') as fout:
            pickle.dump(emplist, fout)
            saved = True
    except:
        pass
    return saved


# In[ ]:


def add_emp(emp):
    emplist.append(emp)
    return save_emplist()


# In[ ]:


def show_list():
    with open('crud_list.pickle','rb') as fin:
        elist = pickle.load(fin)
        # elist.sort(key=lambda e:e.num)
        elist.sort(key=lambda e:int(e.num))
        for e in elist:
            print(e)


# In[ ]:


def find_emp(emp):
    found = None
    with open('crud_list.pickle','rb') as fin:
        elist = pickle.load(fin)
        if emp in elist:
            found = elist[elist.index(emp)]
    return found


# In[ ]:


def update_emp(emp):
    updated = None
    global emplist # 현재 함수 외부에 선언된 변수(global)
    with open('crud_list.pickle', 'rb') as fin:
        emplist = pickle.load(fin)
        if emp in emplist:
            emplist[emplist.index(emp)].phone = emp.phone
            updated = save_emplist()
    return updated


# In[ ]:


def delete_emp(emp):
    global emplist
    deleted = False
    with open('crud_list.pickle', 'rb') as fin:
        emplist = pickle.load(fin)
        if emp in emplist:
            emplist.remove(emp)
            deleted = save_emplist()
    return deleted


# In[ ]:


def is_duplicate(emp):
    with open('crud_list.pickle','rb') as fin:
        emplist = pickle.load(fin)
        if emp in emplist:
            return True
    return False


# In[ ]:


while True:
    menu = input('목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)')
    
    if menu.upper()=='A':
        num, name, phone = input('사원번호 이름 전화번호').strip().split()
        emp = Emp(num, name, phone)
        if is_duplicate(emp):
            print('번호중복, 추가실패!')
            continue
        if add_emp(emp):
            print('사원정보 추가 성공')
        else:
            print('사원정보 추가 실패')
    elif menu.upper()=="S":
        show_list()
    elif menu.upper()=="F":
        sNum = input('검색할 사원번호: ').strip()
        found = find_emp(Emp(sNum))
        if found:
            print(found)
        else:
            print('검색 실패')
    elif menu.upper()=="U":
        num,phone = input('변경할 사원번호 전화번호').strip().split()
        if update_emp(Emp(num, phone=phone)):
            print('수정 성공')
        else:
            print('수정 성공')
    elif menu.upper()=="D":
        sNum = input('삭제할 사원번호').strip()
        if delete_emp(Emp(sNum)):
            print('삭제 성공')
        else:
            print('삭제 실패')
    elif menu.upper()=="X":
        break;
    else:
        print('메뉴입력 오류')

print('프로그램 종료....')


# In[ ]:


with open('crud_list.pickle','rb') as fin:
        elist = pickle.load(fin)
elist
for e in elist:
    print(e)


# In[ ]:


elist
byte_arr = pickle.dumps(elist)
print(byte_arr)


# In[ ]:


elist2 = pickle.loads(byte_arr)
for e in elist2:
    print(e)


# In[ ]:


# elist.sort() # 객체를 정렬해라는 오류남 # 객체의 어떤 값을 지정해서 정렬하라고 해야 오류안남
elist.sort(key=lambda e:e.num) # 람다식
for e in elist:
    print(e)


# In[ ]:


nums = [3,5,1,4,2]
sorted(nums)
nums.sort()
nums


# In[ ]:


outer_num = 100


# In[ ]:


def value_use():
    print(outer_num + 10)


# In[ ]:


value_use()


# In[ ]:


def value_change():
    global outer_num
    outer_num = 10 # 지역변수 > 전역변수, global로 선언
    print(outer_num)  # 10


# In[ ]:


value_change()


# In[ ]:


outer_num


# In[ ]:


def value_use2():
    num = outer_num + 100
    print(num)


# In[ ]:


value_use2()


# In[ ]:


# dumps(), loads()
emplist


# ### Thread_Ex

# In[ ]:


# Thread, Runnable, run()
# Process : 현재 실행중인 프로그램
# Process 안에서 동시에 실행 가능한 소규모 Process


# In[ ]:


# 함수, 메소드, run()


# In[ ]:


import threading
import time
import datetime


# In[ ]:


def t1(name):
    while True:
        print(name, datetime.datetime.now())
        time.sleep(1)


# In[ ]:


# t1('Date Thread')


# In[ ]:


def t2(name):
    i = 0
    while True:
        i += 1
        print(name, i)
        time.sleep(1)


# In[ ]:


# t2('Num Thread')


# In[ ]:


th1 = threading.Thread(target=t1, args=('Date Thread',))
th1.daemon = True
th1.start()

th2 = threading.Thread(target=t2, args=('Num Thread',))
th2.daemon = True
th2.start()


# In[ ]:


# 객체의 멤버 메소드를 쓰레드의 타켓으로 설정하는 예
# threading. Thread(target=obj.method), args=('Date Thread',))


# In[ ]:


import threading
import datetime
import time

# 가상의 CPU역활을 하는 클래스 정의
class MyGame(threading.Thread): # Thread 클래스 상속
    def __init__(self, name):
        threading.Thread.__init__(self)
        print(name, 'instanciated')
        self.daemon = True
    
    def run(self):
        while True:
            print(datetime.datetime.now())
            time.sleep(1) # 1초 쉼
    
my_thread = MyGame('game thread')
# my_thread.daemon = True
my_thread.start()

