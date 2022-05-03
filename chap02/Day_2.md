# Day_2

평균값 구하기

```python
 avg = (3+5) /2 
```

List comprehensions

```python
      #for 왼쪽에 종속문 (value), for가 도는 동안 같이돈다 (제곱)
squares = [value**2 for value in range(1, 11)]
print(squares)
```

Slicing a List

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#['charles', 'martina', 'michael']
```

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

#['martina', 'michael', 'florence']
```

```python
# 앞에 시작이 없으면 처음부터라고 생각하면 된다
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

#['charles', 'martina', 'michael', 'florence']
```

```python
# -가 존재하면 뒤에부터 센다
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# ['michael', 'florence', 'eli'
```

&& = and

|| = or

! =not

```python
SELECT * FROM emp WHERE empno IN(10,20,30);

>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

The if-elif-else Chain

```python
age = 12
if age < 4:
price = 0
elif age < 18:
price = 25
else:
price = 40
```