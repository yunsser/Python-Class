#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * 파이썬 인터프리터의 이해
# * Jupyter notebook
# * 주석문의 종류

# In[1]:


print('Hello World')


# ALT + ENTER 실행 후 아랫줄


# In[2]:


a = 5
b = 7
c = a +b
c
# CTRL + EMTER 실행
# SHIFT + ENTER 실행 후 새로운 셀
print('c =',c)


# In[3]:


msg = "Hello"
print(msg)
msg = 'World'
print(msg)
msg = '''This
            id
                String
                    test'''
print(msg)

#문자열로 만듬
""" 
print("a")
print("b"")
print("c")
"""


# In[4]:


# 이런식으로 작성하면 오류
msg = ""Hello"


# In[ ]:


msg = "Hello 'World'"
print(msg)


# In[ ]:


name = "ada lovelace"
name.title()
#print(title)


# In[ ]:


name = "Ada lovelace"
print(name.upper())
print(name.lower())


# In[ ]:


#print(dir(name))
#print(help(str))
dir(name)
help(str)


# In[ ]:


name = "Smith"
age = 29
info = f"{name}{age}"
info


# In[ ]:


name = input('이름을 입력해주세요:')


# In[ ]:


#키보드에서 번호, 이름, 전화번호를 입럭하세요
#화면에 표시해보세요


# In[ ]:


greeting = "Hello"
newGreeting = greeting.rstrip();
newGreeting


# In[ ]:


nums = [1,2,3]
print(nums)
a,b,c = nums
print(a)


# In[ ]:


msg = """
    A
    B
    C"""
print(msg)

msg = '''
    A
    B
    C
'''
print(msg)


# In[ ]:


names = ['smith', 'scott', 'jone']
len(names) # 몇개가 들어있는지 표현해준다
names[1].title() #.title() 이걸 넣어주면 앞에 대문자로 바뀜


# In[ ]:


print(names[0], names[2])


# In[ ]:


names[0], names[2] # 하나의 자료구조 list 아님 # Tuple


# In[ ]:


type(['a'])


# In[ ]:


num = [1,2,3]
num[2] = 5
num.append(4)
num.remove(5) # 값 삭제
del num[1]
num
#dir(num) 쓸수있는 명령어 알려줌
#SHIFT + TAB 상세내용보기


# In[ ]:


# 원소가 한개인 Tuple 선언하고 자료형 확인하기
data = (10,)
type(data)


# In[11]:


data = (1, 2, 3)
data = 1, 2, 3 # () 생략
print(type((data)))


# In[12]:


print(data)
print(data[-1]) # 끝 방


# In[ ]:


# for문
for x in [3,5,7] :
    print(x)


# In[ ]:


for i in range(0,3): # 0 1 2 까지 루프를 돌린다
    print(i)


# In[1]:


# 키보드에서 회원의 정보를 입력받아서 리스트에 저장하는 프로그램 작성 (번호, 이름, 전화)
# 3인의 회원정보를 입력 받아서 리스트에 저장하고 화면에 표시해보세요
num = []
name = []
phone = []

for _ in range(0,3):
    strMem = input('번호 이름 전화:')
    memInfo = strMem.split(' ')
    print(memInfo)
    
    num.append(memInfo[0])
    name.append(memInfo[1])
    phone.append(memInfo[2])
    
for i in range(0,3):
    print(num[i], name[i], phone[i])


# In[ ]:


name


# In[ ]:


# if문
if a==b:
    print(xxx)


# In[4]:


for i in range(0,3):
    print(num[i], name[i], phone[i])
    
newInfo = input('수정할 회원번호 전화: ')

n, newPhone = newInfo.split(' ')
idx = num.index(n) # 값을 사용하여 인덱스를 구함
phone[idx] = newPhone # 전화번호 업데이트

print('\n','수정된 정보')
for i in range(0,3):
    print (num[i], name[i], phone[i])


# In[9]:


for i in range(0,3):
    print(num[i], name[i], phone[i])
    
del_num = input('삭제할 회원번호: ')

try: 
    idx = num.index(del_num)
    del num[idx]
    print('삭제성공')
except ValueError as e:
    print('삭제실패' + str(e)) # 무슨 에러인지 체크가능


# In[10]:


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars


# In[12]:


cars.sort() # 오름차순 정렬 # list에서 가끔 사용
cars


# In[13]:


cars.sort(reverse=True) # 내림차순 정렬
cars


# In[17]:


sorted(cars) # 어떠한 이터러블 객체도 받을 수 있다 # abcd 순


# In[20]:


copy_list = sorted(cars)
print('사본',copy_list)
print('원본',cars)


# In[16]:


cars


# In[22]:


cars.reverse() # 정렬을 반대로 뒤집어준다
cars


# In[24]:


cars
cars.reverse()
cars


# In[26]:


nums = [2,1,3]
nums.reverse()
nums


# In[34]:


import random

rd_num = random.randint(0,10)

# 임의의 종수 한개를 구한다(5~10)
# 위에서 구해진 수의 갯수만큼의 임의의 정수를 구함 # 7이라면 7개의 임의의 정수를 구한다
# 구해진 모든 정수를 화면에 표시해보세요
# 표시 예)
# 1. 6
# 2. 2

