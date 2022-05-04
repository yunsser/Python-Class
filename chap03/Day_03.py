#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# 1. Collecion(정보처리)
# 2. Arguments

# In[3]:


nums = [1,2,3,4,4,5]
nums


# In[4]:


set(nums)


# In[5]:


len(nums),len(set(nums))


# In[6]:


if len(nums)!=len(set(nums)):
    print('데이터 중복 발견')
else:
    print('데이터 중복 없음')


# In[ ]:


# 프로그램이 시작되면, 아래처럼 메뉴 목록을 제시한다
# “추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x) : “
# 이용자가 ‘a’를 입력한 경우,
# “사원의 번호 이름 전화: ”
# 이용자가 사원정보 3가지를 입력한 경우,
# 한 사원의 정보를 Collection에 저장한다
# 한개의 기능을 수행한 후에는 다시 원래의 메뉴 목록이 표시된다
# 이미 등록된 사원정보 중에서 새로 입력된 사원번호가 중복되지 않아야함 -> set


# In[ ]:


emps = []

while True:
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ")
    if menu.upper() == 'A':
        num,name,phone = input("사원 번호 이름 전화: ").split()
        nums = [user['num'] for user in emps] # 기존 등록된 사원번호
        nums.append(num)                      # 새로 추가할 사원번호
        if len(nums) != len(set(nums)):       # 사원번호 중복검사
            print('사원정보 중복, 다시 입력해주세요')
            continue
        emps.append({'num':num, 'name':name, 'phone':phone})
    elif menu.upper() == 'X':
        print('프로그램 종료')
        break


# In[ ]:


# 목록보기 기능(s)
# 이용자가  "s"를 선택한 경우 화면에 모든 사원정보를 표시하고
# 이어서 화면에 메뉴가 표시된다


# In[ ]:


emps = []


# In[ ]:


while True:
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ")
    if menu.upper() == 'A':
        num,name,phone = input("사원 번호 이름 전화: ").split()
        nums = [user['num'] for user in emps] 
        nums.append(num)                     
        if len(nums) != len(set(nums)):       
            print('사원정보 중복, 다시 입력해주세요')
            continue
        emps.append({'num':num, 'name':name, 'phone':phone})
        
    elif menu.upper()=='S':
        for emp in emps:
            print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
        
    elif menu.upper() == 'X':
        print('프로그램 종료')
        break


# In[ ]:


# 검색기능 (f)
# 이름으로 검색하기, 대소문자 구분없이 검색된 사원정보가 화면에 표시된다


# In[ ]:


emps = []


# In[ ]:


while True:
    print("-----------------------------------------------------------")
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ")
    print("---------------------------------------------------------\n")
    
    if menu.upper() == 'A':
        num,name,phone = input("사원 번호 이름 전화: ").split()
        nums = [user['num'] for user in emps] 
        nums.append(num)                     
        if len(nums) != len(set(nums)):       
            print('사원정보 중복, 다시 입력해주세요')
            continue
        emps.append({'num':num, 'name':name, 'phone':phone})
        
    elif menu.upper()=='S':
        for emp in emps:
            print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
            
    elif menu.upper()=='F':
        ename = input("검색할 이름: ")
        for emp in emps:
            if found == ename:
                print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
                break
            else:
                print("검색 실패")
        
    elif menu.upper() == 'X':
        print('프로그램 종료')
        break
    else:
        print('======== 메뉴 입력오류 ========')


# In[ ]:


emps = []


# In[ ]:


while True:
    print("-----------------------------------------------------------")
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ")
    print("---------------------------------------------------------\n")
    
    if menu.upper() == 'A':
        num,name,phone = input("사원 번호 이름 전화: ").split()
        nums = [user['num'] for user in emps] 
        nums.append(num)                     
        if len(nums) != len(set(nums)):       
            print('사원정보 중복, 다시 입력해주세요')
            continue
        emps.append({'num':num, 'name':name, 'phone':phone})
        
    elif menu.upper()=='S':
        for emp in emps:
            print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
            
    elif menu.upper()=='F':
            ename = input("검색할 이름: ")
            found = False
            for emp in emps:
                if emp['name']==ename:
                    print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
                    found = True
                    break
            if not found:
                    print("검색 실패")
        
    elif menu.upper() == 'X':
        print('프로그램 종료')
        break
    else:
        print('======== 메뉴 입력오류 ========')


# In[ ]:


# 수정기능 (u)
# 이용자가 'u'를 선택한 경우,
# "수정할 사원번호 전화번호" 
# 입력된 사원번호로 검색하여 해당 사원의 전화번호를 갱신한 후
# "수정성공" "수정실패" 메세지 출력


# In[ ]:


emps = []


# In[ ]:


while True:
    print("-----------------------------------------------------------")
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ")
    print("---------------------------------------------------------\n")
    
    if menu.upper() == 'A':
        num,name,phone = input("사원 번호 이름 전화: ").split()
        nums = [user['num'] for user in emps] 
        nums.append(num)                     
        if len(nums) != len(set(nums)):       
            print('사원정보 중복, 다시 입력해주세요')
            continue
        emps.append({'num':num, 'name':name, 'phone':phone})
        
    elif menu.upper()=='S':
        for emp in emps:
            print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
            
    elif menu.upper()=='F':
            ename = input("검색할 이름: ")
            found = False
            for emp in emps:
                if emp['name']==ename:
                    print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
                    found = True
                    break
            if not found:
                    print("검색 실패")
                    
    elif menu.upper()=='U':
        num,phone=input("수정할 사원번호 및 전화번호: ").split()
        updated = False
        for emp in emps:
            if emp['num']==num:
                emp['phone']=phone
                updated = True
                print("수정성공")
                break
        if not updated:
            print("수정실패")
                
    elif menu.upper() == 'X':
        print('프로그램 종료')
        break
    else:
        print('======== 메뉴 입력오류 ========')


# In[ ]:


# 삭제기능(d)
# 이용자가 'd'를 선택한 경우,
# "삭제할 사원번호:"
# 삭제 후 "삭제 성공/실패"


# In[ ]:


emps = []


# In[ ]:


while True:
    print("-----------------------------------------------------------")
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ")
    print("---------------------------------------------------------\n")
    
    if menu.upper() == 'A':
        num,name,phone = input("사원 번호 이름 전화: ").split() # 여러개 split
        nums = [user['num'] for user in emps] 
        nums.append(num)                     
        if len(nums) != len(set(nums)):       
            print('사원정보 중복, 다시 입력해주세요')
            continue
        emps.append({'num':num, 'name':name, 'phone':phone})
        
    elif menu.upper()=='S':
        for emp in emps:
            print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
            
    elif menu.upper()=='F':
            ename = input("검색할 이름: ")
            found = False
            for emp in emps:
                if emp['name']==ename:
                    print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
                    found = True
                    break
            if not found:
                    print("검색 실패")
                    
    elif menu.upper()=='U':
        num,phone=input("수정할 사원번호 및 전화번호: ").split()
        updated = False
        for emp in emps:
            if emp['num']==num:
                emp['phone']=phone
                updated = True
                print("수정성공")
                break
        if not updated:
            print("수정실패")
            
    elif menu.upper()=='D':
        num=input("삭제할 회원번호: ").strip() # 한개 strip
        deleted = False
        for emp in emps:
            if emp['num']==num:
                emps.remove(emp)
                deleted = True
                print("삭제성공")
        if not deleted:
            print("삭제실패")
                
    elif menu.upper() == 'X':
        print('프로그램 종료')
        break
    else:
        print('======== 메뉴 입력오류 ========')


# In[ ]:


emps = []


# In[ ]:


# 중복인지 아닌지를 검사해서 그 결과를 리턴하는 함수 작성
# is_duplicate True: 중복됨, False: 중복아님

def is_duplicate(num):
    nums = [emp['num'] for emp in emps]
    nums.append(num)
    if len(nums) != len(set(nums)):
        return True
    else:
        return False


# In[ ]:


# 목록보기 기능 -> emp_list()

def emp_list():
    for emp in emps:
        print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")


# In[ ]:


# 검색기능 : 이름을 파라미터로 받아서 해당 사원의 정보를 검색하고 리턴한다
# - 검색결과가 없는 경우에는 None을 리턴
# - find_emp(name):

def find_emp(name):
    for emp in emps:
        if emp['name']==name:
            return emp
    return None


# In[ ]:


# 수정기능 : (num, phone)을 받아서 목록을 수정하고 성공시 True,
# 실패시 False 리턴
# - update_emp(tuple)

def update_emp(new_phone):
    num, phone = new_phone
    updated = False
    for emp in emps:
        if emp['num']==num:
            emp['phone'] = phone
            updated = True
    return updated # 함수안에 리턴은 한번만 쓰는게 좋다


# In[ ]:


# 삭제기능 : 사원번호를 받아서 해당 사원정보를 삭제하고 True, 실패시 False 리턴
# - delete_emp(num):

def delete_emp(num):
    deleted = False
    for emp in emps:
        if emp['num']==num:
            emps.remove(emp)
            deleted = True
    return deleted


# In[ ]:


while True:
    print("-----------------------------------------------------------")
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ")
    print("---------------------------------------------------------\n")
    
    if menu.upper() == 'A':
        num,name,phone = input("사원 번호 이름 전화: ").split()
        if is_duplicate(num):                   
            print('사원정보 중복, 다시 입력해주세요')
            continue
        emps.append({'num':num, 'name':name, 'phone':phone})
        print("사원정보 저장 성공")
        
    elif menu.upper()=='S':
        emp_list()
        
    elif menu.upper()=='F':
        ename = input("검색할 사원이름: ")
        emp = find_emp(ename)
        if emp:
            print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
        else:
            print("해당 이름의 사원정보는 없음")
                    
    elif menu.upper()=='U':
        num,phone = input("수정할 사원번호 및 전화번호: ").split()
        if update_emp((num,phone)):
            print("수정성공")
        else:
            print("수정실패")
            
    elif menu.upper()=='D':
        num=input("삭제할 회원번호: ").strip()
        if delete_emp(num):
            print('삭제 성공')
        else:
            print('삭제 실패')
                
    elif menu.upper() == 'X':
        print('프로그램 종료')
        break
    else:
        print('======== 메뉴 입력오류 ========')


# In[ ]:


# import 종류 3가지


# In[ ]:


import pizza


# In[ ]:


pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# In[ ]:


pizza.add(3,5)


# In[ ]:


from pizza import add
add(3,5)


# In[ ]:


import pizza as p
p.add(3,5)


# In[ ]:


import mymodule as mm


# In[ ]:


mm.show('Smith', 'Ward', 'King')


# In[ ]:


from mymodule import show as s
s('Smith', 'Ward', 'King')


# In[5]:


from pizza import *
test()
add(3,5)


# # 클래스 실습
# * 클래스와 인스턴스
# * 초기자, __init__()
# * 인스턴스 메소드 : 인스턴스에 포함된 메소드

# In[20]:


class Emp:
    
    def __init__(self, num, name, phone):
        self.num = num
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return(f"{self.num}\t{self.name}\t{self.phone}")
    
    def __eq__(self, other):
        return self.num==other.num


# In[21]:


e1 = Emp(11, 'Smith', '010-3547-6510')
print(e1)


# In[39]:


e2 = Emp(12, 'Blake', '010-3271-1290')
print(e2)


# In[23]:


e1.__eq__(e2)


# In[35]:


e3 = Emp(12, '', '')

e2.__eq__(e3)


# In[36]:


e2==e3


# In[37]:


e1==e2


# In[40]:


emp_list = [e1, e2]
for e in emp_list:
    print(e)

