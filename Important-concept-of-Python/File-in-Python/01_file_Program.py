# File in Python

# Read File using Python

try:
    file_name = input("Enter your file name : ")
    f = open(file_name,"r")
    data = f.read()
    print(f"Your file data is {data}")

except Exception as e:
    print(f"ERROR : {e}")
finally:
    print("Your Program run success Fully.")

