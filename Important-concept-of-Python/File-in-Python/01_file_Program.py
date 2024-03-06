# File in Python

# Read File using Python

try:
    file_name = input("Enter your file name : ")
    f = open(file_name,"r")
    data = f.read()
    print(f"Your file data is : \n{data}")

except:
    print(f"ERROR  : File is not found.")
finally:
    print("Your Program run success Fully.")

