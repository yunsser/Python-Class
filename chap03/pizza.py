def make_pizza(size, *toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
def add(a,b):
    c = a+b
    print(f"{a}+{b}={c}")
    
def test():
    print("Hello module")