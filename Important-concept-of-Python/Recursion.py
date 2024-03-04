# Factorial of a number without recursion in python

def factorial_of_A_number(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact
print(factorial_of_A_number(5))

# Recursion Function

def factorial_num(num):
    if num == 1:
        return 1
    else:
        return num * factorial_num(num-1)

print(factorial_num(5))

# Print number n to 1 using normal function.

def print_reverse_number(num):
    while num > 0:
        print(num)
        num -= 1

# print_reverse_number(5)

# Print number n to 1 using Recursion function.

def reverse_numbers(n):
    if n == 0:
        return 
    print(n)
    reverse_numbers(n - 1)


reverse_numbers(5)

# Power of number

def power_number(a,b):
    if b == 0:
        return 1
    return a * power_number(a,b-1)

print(f"the Power of {power_number(2,3)}")
print(f"the Power of {power_number(5,5)}")






