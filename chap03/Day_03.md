# Day_03

Collection ( 정보처리 )

- list, tuple, dictionary, set
    - list : 순서유지, 중복허용
    - tuple : list와 동일특성, 수정/삭제 안됨
    - dictionary : key, value가 쌍으로 저장
    - set : 중복불허

```python
def greet_user(username) → 가인자
print(f"Hello, {username.title()}!")
greet_user('jesse') → 실인자
```

Default Values (Arguments)

```python
def describe_pet(pet_name, animal_type='dog'): # 고정값 dog
describe_pet(pet_name='willie')
```

Argument Optional

```python
											 #디폴드값 없는거 앞, 있는건 뒤쪽으로 (마지막껀 값 전달 안함)
def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

```python
function_name(list_name[:]) 
#사본이 조작되게 하고싶을때 deep copy
```

인스턴스 메소드

```python
class Dog:

def __init__(self, name, age):
self.name = name
 self.age = age

def sit(self):
 print(f"{self.name} is now sitting.")
 
def roll_over(self):
 print(f"{self.name} rolled over!")
```