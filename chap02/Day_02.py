#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# 1. Ramdom
# 2. List comprehensions

# In[1]:


#임의의 정수 10개 추출하고
#내림차순으로 정렬하고,
#화면에 표시
#오름차순으로 정렬
#맨 마지막에 있는 정수 1개 삭제
#중간에 위치한 수를 추출하여 화면에 표시
#중간에 수가 없다면 중간 양쪽에 있는 수의 평균값


# In[2]:


import random

ran_num = [random.randint(1, 100)for r in range(10)]
ran_num.sort()
print(ran_num)
ran_num.sort(reverse=True)
print(ran_num)


# In[3]:


import random # 모듈을 사용하겠다
# import random as rd # 랜덤을 rd 라는 언어로 쓰겠다


# In[4]:


num_list = []
for _ in range(10):
    num_list.append(random.randint(0,10))


# In[5]:


num_list


# In[6]:


num_list.sort(reverse=True)
num_list


# In[7]:


num_list.sort()
num_list


# In[8]:


num_list.pop()
num_list


# In[9]:


num_list[int(len(num_list)/2)]


# In[10]:


# 1 ~10 사이의 정수중에서 짝수만 선택하여 
# 리스트의 원소에 저장하고 홀수는 0으로 변경하여
# 저장한 후 리스트의 모든 원소를 화면에 표시해보세요


# In[11]:


# list = []
# for i in range(1, 11):
#     if i % 2 ==0:
#         list.append(i)
#     else:
#         list.append(0)
# print(list)


# In[12]:


# 조건값
nums = [v if v % 2 == 0 else 0 for v in range(1,11)]


# In[13]:


print(nums)


# In[14]:


nums = list(range(1,11))
nums


# In[15]:


nums2 = nums[4:7]
nums2


# In[16]:


nums2[0] = 100
nums2[0]


# In[17]:


nums


# In[18]:


nums3 = nums # Shallow Copy 얕은 복사


# In[19]:


nums3


# In[20]:


nums3[0] = 100


# In[21]:


nums3


# In[22]:


nums


# In[23]:


nums4 = nums[:] # Deep Copy 원본 통째로 복사


# In[24]:


nums4


# In[25]:


nums4[0] = 200
nums4


# In[26]:


nums


# ==============================================================================

# In[27]:


nums.append(-5)
print(nums)


# In[28]:


nums4


# In[29]:


num_list = [4,5,6]
num_list


# In[30]:


a,b,c = num_list


# In[31]:


a,b,c


# In[32]:


a


# In[33]:


# 무작위 정수 10개를 준비하고
# 처음 3개를 추출하여 튜플(tuple)에 저장하고
# 튜플의 내용을 화면에 표시
# list comprehension 활용 

nums = [random. randint(0,11) for i in range(1,11)]
nums


# In[34]:


a,b,c = nums[:3]
a,b,c


# In[35]:


tp = (a,b,c)
tp


# ===========================================================================================================================

# In[118]:


uid_list = ['SMITH', 'WARD', 'LORA']
pwd_list = ['0000', '1111', '2222']


# In[122]:


# 키보드에서 아이디, 암호를 입력 받아서
# 로그인 하는 기능 구현
# 미리 uid, pwd 리스트를 생성해놓고 몇개의 정보를 준비함
# uid, pwd에는 아이디는 모두 대문자로 준비함
# 로그인에 성공할 때까지느 반복해서 시도할 수 있도록 함
# 결국 호그인에 성공하면 '로그인 성공', 아니면 '로그인 실패' 표시

for _ in range(3):
    uid, pwd = input('아이디 암호: ').split()
    try:
        idx = uid_list.index(uid.upper())
        
        if uid_list[idx] == uid.upper():
            if pwd_list[idx] == pwd:
                print('로그인성공')
                break
    except ValueError as e:
        print('로그인실패: ' + str(e))


# In[39]:


1 < 2 #True


# In[40]:


1 < 2 and 3 > 2


# In[42]:


'd' in ['a','b','c']


# In[46]:


# 파이썬 날짜 다루기
# import datetime
from datetime import date


# In[49]:


# today = datetime.date.today()
today = date.today()


# In[55]:


today.year # 년도
today.month # 월
today.day #일
today.weekday() # 요일 # 월(0), 화(1), 수(2), 목(3), 금(4), 토(5), 일(6)
today.isoweekday() # iso에서 정한 표준요일 # 월(1), 화(2), 수(3), 목(4), 금(5), 토(6), 일(7)


# In[60]:


# 오늘 날짜 출력
# 2022년 05월 03일 화요일

from datetime import date
today = date.today()


# In[97]:


from datetime import date

d = date.today()
t = ['월', '화', '수', '목', '금', '토', '일']
r = d.weekday()
print (str(d.year)+'년', str(d.month)+'월', str(d.day)+'일', t[r]+'요일')


# In[91]:


year = today.year
month = today.month
day = today.day
wday = today.weekday()

strday = ''

if wday==0:
    strday='월'
elif wday==1:
    strday='화'
elif wday==2:
    strday='수'
elif wday==3:
    strday='목'
elif wday==4:
    strday='금'
elif wday==5:
    strday='토'
elif wday==6:
    strday='일'


# In[98]:


days = list('월화수목금토일')
days[0]
days[wday]


# In[94]:


strday = list('월화수목금토일')[wday]


# In[95]:


print(f"{year}년 {month}월 {day}일, {strday}요일")


# In[125]:


# try ~ except 리스트에 포함되지 않는 아이템을 검사
# - list.index('value')
# try ~ except 없이 로그인 기능 구현

uid_list = ['SMITH', 'WARD', 'LORA']
pwd_list = ['0000', '1111', '2222']

for _ in range(3):
   uid,pwd = input('아이디 암호: ').split()
   if uid.upper() in uid_list:
        idx = uid_list.index(uid.upper())
        if uid_list[idx] == uid.upper() and pwd_list[idx]==pwd:
            print('로그인 성공')
            break
   else:
    print('로그인실패')


# In[123]:


users = [{}, {}, {}]
type(users[0])


# In[160]:


# 키보드에서 3인의 회원정보를 입력받는다
# (번호, 이름, 전화)
# 입력을 마치면, 입력된 모든 정보를 리스트로 화면에 표시
# user = {}
# user['num'] = 11

users = []
for _ in range(3):
    (num,name,phone) = input('번호 이름 전화: ').split()
    users.append({'num':num, 'name':name, 'phone':phone})
users


# In[161]:


for user in users:
    s = f"{user['num']}\t{user['name']}\t{user['phone']}"
    print(s)


# In[162]:


# 한사람의 전화번호를 수정 후 화면에 표시
users[1]['phone'] = '3333'


# In[163]:


for user in users:
    s = f"{user['num']}\t{user['name']}\t{user['phone']}"
    print(s)


# In[164]:


# 리스트에 저장된 마지막 회원정보 중에서 phone 정보 삭제
# 삭제된 상태로 리스트 출력
# phone 정보가 없는 경우 '전화기 분실' 표시

del users[2]['phone']


# In[165]:


users


# In[169]:


for user in users:
    s = f"{user['num']}\t{user['name']}\t{user.get('phone','전화기 분실')}"
    print(s)


# In[173]:


# [{}, {} ......]
# 위의 리스트에 몇 사람 정보를 저장한다
# 키보드에서 회원번호를 입력하여 해당 회원을 검색하고
# 그 결과를 화면에 표시한다

num = input('검색할 회원정보: ').strip()


# In[176]:


for user in users:
    if user['num']==num:
        s = f"{user['num']}\t{user['name']}\t{user.get('phone','전화기 분실')}"
        print(s)
        break


# In[175]:


users = []
for i in range(3):
    num, name, phone = input("번호, 이름, 전화를 입력하세요: ").split()
    users.append({'num':num, 'name':name, 'phone':phone})

num = input('검색할 회원번호: ').strip()    
for user in users:
    if num==user['num']:
        s = f"{user['num']}\t{user['name']}\t{user['phone']}"
        print(s)
        break


# In[ ]:


# list, set, dictionary
# list : 순서유지, 중복활용
# set : 순서없음, 중복불허
# dict : key, value 같이 저장


# In[179]:


set1 = set([1,1,1,1,2])


# In[180]:


len(set1)


# In[182]:


# 1~10 사이의 정수 중에서 임의로 한개를 추출하여 중복되지 않도록 7개를 추출하려고 한다
# 추출된 원소를 정렬하여 화면에 표시한다
# 무한루프
# while True :
#    xxxxxxx
#    break

import random as rd
set2 = set()

while True:
    rd_num = rd.randint(1, 11)
    set2.add(rd_num)
    if len(set2)==7:
        break
        
sorted(set2)

