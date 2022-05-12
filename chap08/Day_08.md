# Day_08

소켓 다중 이용자

Python MySQL CRUD

Web Scraping  :  

Socket(서버) : 대기용, 

- accept() : 통신용 소켓 리턴 (이용자 접속), recv(), send()

클라이언트 → 전송 → 서버 → 접속자목록 → 메세지 전송, 메세지 당사자에게는 전송하지 않음

클라이언트 2개 실행

- 아나콘다 프롬프트 2개 실행
- 각각의 프롬프트에서 python Client_Socket.py
    - 실행법
        
        dir > cd 1_Python_Projects (1p 쓰고 탭누르면 자동완성) > dir > python 파일이름
        

퇴장 메세지 → 당사자 외의 다른 이용자에게 전달되도록 

퇴장 > 해당 이용자의 소켓을 서버에서 삭제한다

3인 접속 환경

- 1번 이용자가 3번에게만 전달하고자 하는 메시지가 있다 (귓속말)
- 이용자 소켓을 딕셔너리에 번호화 함께 저장한다
- 메세지 입력 : 3/메세지(3번에게 보내는 메세지)

```python
ChatMsg(mag, to=3)
soc_dict[3].send(msg)
```

첨부파일이 있는 경우

- 3/메시지/test.jpg

1번 이용자 → 3번 이용자에게 첨부파일 보내기

```python
n,msg,fname = '3/msg/fname'.split('/')
with open('test.jpg', 'rb') as fin:
	img_data = fin.read()
	ChatMsg(msg, to=int(n), attach=img_data

print('이미지 로드완료')
```

파일이름 : copy.jpg

```python
with open('copy.jpg', 'wb') as fout:
            fout.write(chatmsg.attach)
            print('파일저장 성공')
```

### sql 설치

mysql 파이썬 커넥터 설치(Anaconda Prompt에서)

python -m pip install mysql-connector-python

pip install PyMySQL

```python
WHERE num=?

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

num=%s
```