#!/usr/bin/env python
# coding: utf-8

# # MySQL_CRUD

# In[11]:


import pymysql
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db='mypy', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
sql = "SELECT num, name, phone, email FROM user LIMIT 10"
curs.execute(sql)

# 데이터 Fetch
rows = curs.fetchall()
for (num,name,phone,email) in rows:
    print(num,name,phone,email)
    
curs.close()
# Connection 닫기
conn.close()


# In[ ]:


# Parameter 확인
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db='mypy', charset='utf8')
# Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)
 
# SQL 실행
sql = "SELECT code, name, continent FROM country WHERE code=%s AND continent=%s"
curs.execute(sql, ('KOR','ASIA'))
 
# 데이타 Fetch
rows = curs.fetchall()
for row in rows:
    print(row)
    print(row['code'], row['name'], row['continent'])
    
curs.close()
conn.close()


# In[ ]:


# INSERT
import pymysql
 
# MySQL Connection 생성
conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                       db='test', charset='utf8')
 
# 다수개의 행을 입력하는 경우
vals = (("Smith", "010-5417-3251", "smith@daum.net"), 
        ("Blake", "010-2547-3210", "blake@naver.com"))
sql = "INSERT INTO user(name, phone, email) VALUES (%s,%s,%s)"
# 다수개의 행을 추가하는 경우 executemany() 를 사용한다
with conn.cursor() as cursor:
    n = cursor.executemany(sql, vals )
    # cursor.execute(sql,('a','b','c')) 이와같은 문장을 반복해서 다수행을 입력할 수도 있다
    if n==2:
        print('2개행 입력성공')
        conn.commit()  # commit을 사용하지 않으면 테이블에 반영되지 않음

conn.close()
print('사용자 추가 성공')


# In[ ]:


# updata
import pymysql
 
# MySQL Connection 생성
conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                       db='test', charset='utf8')
 
# Update
sql = "UPDATE user SET phone=%s WHERE num=%s"

with conn.cursor() as cursor:
    n = cursor.execute(sql, ('010-3333-7777', 14) )

    if n==1:
        print('수정 성공')
        conn.commit()

conn.close()
 


# In[ ]:


# Delete
import pymysql
 
# MySQL Connection 생성
conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                       db='test', charset='utf8')
 
# Update
sql = "DELETE FROM user WHERE num=%s"

with conn.cursor() as cursor:
    n = cursor.execute(sql, 15 )

    if n==1:
        print('삭제 성공')
        conn.commit()

conn.close()

