#Example of normal function 

def sum_of_value(value1,value2):
    sum = value1  + value2
    print(f"Sum of {value1} and {value2} is {sum}.")

sum_of_value(10,20)
# sum_of_value() that is give An Error.

# Over loding Function in Pyhton


def add(*args):
    sum = 0
    for element in args:
        sum = sum  + element
    print(f"Sum of your given value is {sum}.")

add(1,2,3,4)  # Over loded function
add(2,3)
add()


# Method over loding in python.

class A:
    def __init__(self,name = None):
        if name != None:
            print(f"Hello ! {name}")
        else:
            print("Hello ! ")

a = A()
