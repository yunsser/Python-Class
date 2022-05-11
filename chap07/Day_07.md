# Day_07

이용자가 숫자를 입력하면 그 수부터 0까지 1초에 한번씩 숫자를 표시하고 0이 되면 종료

이용자는 기존 카운트다운이 진행되고 있는 도중에라도

얼마든지 다시 새로운 숫자를 입력할 수 있다

100 → 0, 100초 소요

다른 숫자입력 n → 0

현재 CPU가 어떤 루프에 매달리고 있다면 이용자가 숫자를 입력하더라도 그 수의 카운트 다운을 할 수 없다

```python
class CountDownThread(threading.Thread):
	def __init__(self, name, num):
		#....
		self.name = name
		self.num = num

	def run(self):
		while True:
			self.num -= 1
			print(self.num)
			if self.num == 0;
				print(self.name, '쓰레드 종료')
				break
			time.sleep(1)
```

숫자 입력 → Thread 객체에 숫자를 전달 → Thread.start()

```python
num = input(’카운트 다운 수 입력: ’)
cdt = CountDownThread(num, int(num))
cdt.start()
```

Socket

- 전구 소켓
- 소켓
- 접속구

인터넷에 연결된 다른 컴퓨터에 접속하기 위한 접속구 역활

tcp/ip protocol을 사용하여 다른 시스템과 통신하려고 할 때

tcp/ip socket

클라이언트, 서버 간의 통신에 ChatMsg 객체 활용

전달된 메세지를 화면에 표시

클래스

```python
ChatMsg

msg = ChatMsg('안녕하세요?')
chatmsg = pickle.dumps(msg) # 바이트 단위
clientSock.send(chatmsg)
```

이용자가 서버에 접속하면,

채팅기능은 별도의 쓰레드에 의해서 실행되도록 하고

메인 쓰레드는 이용자 접속대기 기능만 수행하도록 한다

한 클라이언트가 전송한 데이터가 자신에 되돌아오면 성공!

서버측에서 데이터를 클라이언트에게 보내려면 뭐가 필요하죠?

- 소켓

1번 이용자 → 모든 이용자에게 전송

```python
msg = soc.recv(1024)
soc1.send(msg)
soc2.send(msg)
soc3.send(msg)
soc4.send(msg)
```