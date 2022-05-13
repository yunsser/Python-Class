# Day_09

### MySQL CRUD 실습

user 테이블 사용

- num, name, phone, email

User 클래스 사용

기능 : 목록 (s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)

수정할 떄는 phone, email 대상

1. 프로그램이 시작되면 위에 제시한 6가지 메뉴가 표시된다
2. 추가(a) 기능을 구현한다
    - 키보드에서 num, name, phone, email을 받아서 User 객체 초기화, user 테이블에 저장
3. 목록(s) 기능 구현
4. 검색(f) 기능 구현 (번호/이름으로 검색)
5. 수정(u)
    - 키보드에서 num, phone, email을 받아서 기존 정보 갱신
6. 삭제(d)
    - 키보드에서 num을 받아서 기존 정보 삭제
7. 종료(x): x누르면 프로그램 종료

각 단계마다 완성 메세지를 채팅창에 올려주세요

- 예시, [추가] 완성

User: VO

UserDAO: DAO

```python
import user
userObj = user.User(11)
```

```python
from user import *
userObj = User(11)
```

```python
udao = dao.UserDAO()
ulist = udao.list_all()
for u in ulist:
	print(u)

from dao import UserDAO
udao = UserDAO()
```

num은 자동증가 필드가 아니므로

user 테이블에 저장되기 전에 동일 번호 중복검사를 수행하여 중복을 방지한다

- 자동증가 번호 생성함수
- 기존 데이터 중에 동일번호가 이미 포함되어 있는지 검사

검색은 번호로 검색, 이름으로 검색 중에 이용자가 선택할 수 있게 해야합니다