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


# Program 02
    
person_deatils_dict = { 32 : "Alice", 23: "Som",56  : "Bil Mark"}

try:
    print(f"See this Dictionary  : {person_deatils_dict}.")
    age = int(input("Enter age to get name of Person : "))
    print(person_deatils_dict[age])

except Exception as e:
    print(f"ERROR : Invalid Key found.")

finally:
    print("Your program run success Fully.")








    
    


