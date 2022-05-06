#!/usr/bin/env python
# coding: utf-8

# ### 오늘의 주제
# * 

# In[1]:


from emp import Emp


# In[2]:


emps = []


# In[3]:


emps.append(Emp(11, name='smith', phone='010-6541-9870'))
emps.append(Emp(12, name='scott', phone='010-3254-2145'))
emps.append(Emp(13, name='ward', phone='010-2697-1220'))
# emps.index()
# dir(emps)


# In[4]:


def is_duplicate_num(num): # 중복되는 객체가 있으면 True, 아니면 False
    nums=[]
    for e in emps:
        nums.append(e.num)
    nums.append(num)
    return len(nums)!=len(set(nums))


# In[5]:


def emp_list():
    print("번호\t이름\t전화")
    for emp in emps:
        print(emp)


# In[6]:


def find_emp_name(name): # 검색성공일 경우 해당 사원정보 리턴, 아니면 None 리턴
    emp = None
    for e in emps:
        if e.name==name:
            emp = e
            print(emp)
    return emp


# In[7]:


def update_emp(num, newPhone):
    updated = False
    if is_duplicate_num(int(num)):
        for emp in emps:
            if emp.num == int(num):
                emp.phone = newPhone
                updated = True
    return updated


# In[8]:


def delete_emp(num):
    deleted = False
    for emp in emps:
        if emp.num == num:
            try:
                emps.remove(emp)
                deleted = True
            except ValueError as ve:
                pass
    return deleted


# In[10]:


while True:
    print("-----------------------------------------------------------")
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ")
    print("---------------------------------------------------------\n")
    
    if menu.upper() == 'A':
        (num,name,phone) = input("사원 번호 이름 전화: ").split()
        if is_duplicate_num(int(num)) != True:
            emps.append(Emp(int(num),name,phone))
            print("사원정보 저장 성공")
        else:
            print("사원정보 중복, 다시 입력해주세요")
        
    elif menu.upper()=='S':
        emp_list()
        
    elif menu.upper()=='F':
        name = input("검색할 사원이름: ")
        if not find_emp_name(name):
            print('입력된 이름으로 검색 실패')
                    
    elif menu.upper()=='U':
        num,phone = input("수정할 사원번호 및 전화번호: ").split()
        if update_emp(num,phone):
            print('수정 성공')
        else:
            print('수정 실패')
            
    elif menu.upper()=='D':
        num = input("삭제할 회원번호: ").strip()
        if delete_emp(int(num)):
            print("삭제 성공")
        else:
            print("삭제 실패")
                
    elif menu.upper() == 'X':
        print('프로그램 종료')
        break
    else:
        print('======== 메뉴 입력오류 ========')


# In[43]:


import random
random.randint(1,10)


# In[7]:


from random import randint
randint(1,10)


# #### 파일 다루기

# In[44]:


fstream = open('emp.py', 'r')
data = fstream.read()
print(data)
fstream.close()


# In[15]:


# open('emp.py','r') # 파일 읽어오기
with open('emp.py','r', encoding='utf-8') as fstream:
    data = fstream.read()
    print(data)


# In[16]:


with open('emp.py','r', encoding='utf-8') as fstream:
    data = fstream.readlines() # list
    print(data)

