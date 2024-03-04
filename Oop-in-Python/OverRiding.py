# Variable Over riding

a = 90
def print_value(x):
    print(f"Your value is {x}.")

print_value(70)
print(a)
a = 80 # Overriding the variable
print(a)

# function overriding in Python

def random_func():
    pass

def second_func(x,y):
    print(f"Your give value of x is {x} and value of y is {y}.")

second_func(7,6)

def random_func():
    print(f"I am example od random function in Python.")

random_func()