#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * 파일 다루기
# * 객체 직렬화 (Serialization)

# # 파일 다루기
# * 파일 열기 : open()
# * CRUD : read, write, readlines
# * 파일 닫기 : close()

# In[1]:


fobj = open('emp.py', 'r')
type(fobj) # _io.TextIOWrapper
dir(fobj)  # Iterator, __next__(), 반복문에 적용 가능
fobj.close()


# In[2]:


fobj = open('emp.py', 'r')
for data in fobj:
    # print(data, end='') # 프린트의 디폴트(\n) 개행을 하지마라 # Keyword Arguments
    print(data.rstrip()) # 오른쪽 끝에 있는 공백제거
fobj.close()


# In[3]:


from collections.abc import Iterable, Iterator
nums = [1,2,3]
dir(nums)
isinstance(nums, Iterable) # True, isinstance (Java : intance of 메소드와 동일), __getitem__()이 존재한다
# nums.__iter__() # for of 안에서 사용가능
isinstance(nums, Iterator) # False


# In[4]:


nums.__getitem__(0)
nums[0]


# In[5]:


itr = nums.__iter__() # next만 호출, 인스턴스 안에 있는 메소드

isinstance(itr, Iterator) # True


# In[6]:


# nums.__iter__()
iter(nums) # 함수(클래스 밖)


# In[7]:


isinstance(fobj, Iterable) # True
isinstance(fobj, Iterator) # True


# In[8]:


fobj = open('emp.py', 'r')
fdata = fobj.read()
# print(fdata)
type(fdata) # str (문자열 한개), 한방에 출력을 할때


# In[9]:


fobj = open('emp.py', 'r')
datalist = fobj.readlines() # 한행 한행을 가져오기 때문에, 한행 한행 분석할때 쓰기 좋다
type(datalist) # list

for line in datalist:
    print(line.rstrip())
    
fobj.close()


# In[10]:


fobj = open('emp.py', 'r')
print(fobj.__next__().rstrip()) # 한 행
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
fobj.close()


# In[11]:


fobj = open('emp.py', 'r')
# fobj.__next__()
print(next(fobj).rstrip()) # 위에와 동일한 한 행
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
fobj.close()


# In[12]:


with open('emp.py', 'r') as fobj: # 자동 close()
    for line in fobj :
        print(line.rstrip())


# In[23]:


# Emp 클래스가 포함된 모듈을 임포트한다
from emp import Emp

# with 절을 이용하여 emps.txt를 읽기모드로 열고 객체를 fobj에 저장
with open('emps.txt', 'r') as fobj:
    # 한 행을 읽어서 공백 기준으로 쪼갠다
    for line in fobj:
        (num,name,phone) = line.strip().split()
        print(Emp(num,name,phone)) 


# In[24]:


from emp import Emp

with open('emps.txt', 'r') as fobj:
    for line in fobj:
        tup = line.strip().split()
        emp = Emp(tup[0], tup[1], tup[2])
        print(emp)


# In[25]:


def show_list(emps):
    for emp in emps:
        print(emp)


# In[26]:


from emp import Emp

emps = []
with open('emps.txt', 'r') as fobj:
    for line in fobj:
        num,name,phone = line.strip().split()
        emps.append(Emp(num,name,phone))

# 목록을 받아서 화면에 표시한다
show_list(emps)


# In[27]:


# 파일에 한 행 추가
# open, append mode, write
fobj = open('filename', 'a')
fobj.write('line\n')
fobj.close()


# In[28]:


from emp import Emp

def load_emps():
    emps = []
    with open('emps.txt', 'r') as fobj:
        for line in fobj:
            num,name,phone = line.strip().split()
            emps.append(Emp(num,name,phone))
    return emps


# In[29]:


def save_emp(emp):
    line = "{} {} {}".format(emp.num, emp.name, emp.phone)
    with open('emps.txt', 'a') as fobj:
        fobj.write(line + '\n')


# In[50]:


show_list(load_emps())


# In[51]:


# 키보드에서 num,name,phone을 입력받아서 emps.txt에 한 행으로 추가
# 목록보기 기능을 실행하면 추가된 정보가 표시되어야 함

num, name, phone = input('번호 이름 전화: ').strip().split() # 키보드에서 한 사원정보를 입력 받는다
save_emp(Emp(num,name,phone)) # 사원정보를 파일에저장
show_list(load_emps()) # 저장된 데이터 확인, 목록을 화면에 표시한다


# In[40]:


# 키보드에서 입력된 사원번호를 키워드로 emps.txt 에서 검색하여
# 검색된 사원정보를 화면에 표시한다
# find_emp(emp) : Emp객체 리턴
# [Emp, Emp, ....]

nums = [3,4,5]
5 in nums
10 in nums # 10==3, 10==4, 10==5

emp in emps # emp==emps[0], emp==emps[1], .... 


# In[35]:


# 파일 데이터를 로드
emplist = load_emps()
# 위에서 로드된 리스트로부터 키보드에서 입력된 사원번호의 Emp객체의 포함여부 확인
sNum = input('검색하려는 사원의 번호: ')
emp = Emp(sNum.strip())

found = None
if emp in emplist:
    found = emplist[emplist.index(emp)]
    
if found:
    print(found)
else:
    print('검색실패')


# In[36]:


def find_emp(emp):
    found = None
    
    if emp in load_emps():
        found = emplist[emplist.index(emp)]
    return found


# In[37]:


sNum = input('검색하려는 사원의 번호: ')
emp = Emp(sNum.strip())
found = find_emp(emp)
if found:
    print(found)
else:
    print('검색실패')


# In[41]:


# 키보드에서 사번, 전화번호를 받아서 해당 사원의 정보를 갱신한다
# update_emp(emp) : True/False


# In[46]:


num, phone = input('사원번호 전화: ').strip().split()
key = Emp(num, phone = phone)
print(key)


# In[71]:


def overwrite(emplist):
    try:
        with open('emps.txt', 'w') as fobj:
            for emp in emplist:
                line = "{} {} {}".format(emp.num, emp.name, emp.phone)
                fobj.write(line + '\n')
        return True
    except:
        return False


# In[72]:


def update_emp(key):
    updated = False
    emplist = load_emps()
    if key in emplist:
        emplist[emplist.index(key)].phone = key.phone
        updated = overwrite(emplist)
    return updated


# In[75]:


# 사원정보 로드
if update_emp(key):
    print('수정성공')
else:
    print('수정실패')
    
show_list(load_emps())


# In[77]:


def delete_emp(key):
    deleted = False
    emplist = load_emps()
    if key in emplist:
        emplist.remove(key)
        deleted = overwrite(emplist)
    return deleted


# In[84]:


# 로드, 리스트에서 삭제대상 찾아서 삭제, 수정된 리스트로 파일 덮어쓰기
sNum = input('삭제할 사원의 번호: ')
key = Emp(sNum.strip())


# In[85]:


if delete_emp(key):
    print('삭제성공')
else:
    print('삭제실패')
    
show_list(load_emps())


# # 객체 직렬화(Serialization)
# * 메모리상에 저장된 객체를 파일이나 네트워크로 전송할 때 필요함

# In[98]:


emp = Emp(15, 'Scott', '000-1111-2222')
with open('empObj.pickle', 'wb') as fw: # Binary Data(이진 데이터), 텍스트가 아닌걸로 쓰겠다
    pickle.dump(emp, fw) # fw 파일에 저장해버리기

