# Variable Over riding

a = 90
def print_value(x):
    print(f"Your value is {x}.")

print_value(70)
print(a)
a = 80 # Overriding the variable
print(a)
