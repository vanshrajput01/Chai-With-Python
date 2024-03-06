# Exception handing in Python
try:
    a = int(input("Enter the value of a : "))
    b = int(input("Enter value of b : "))
    result = a / b
    print(f"Your result is {result}.")

except Exception as e:
    print(f"Error : {e}")

finally:
    print("Your Program run successfully")




    
    


