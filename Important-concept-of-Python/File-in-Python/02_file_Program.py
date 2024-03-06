# Another syntax using to perform operation on file in Python.

# with open("demo.txt","r") as f:
#     print(f.read())

# How to delete exist file in python
    
import os

# os.remove("demo.py") # delete file

# rename function use to rename exits file name.

# os.rename("demo.txt","06_sample_File.txt")

# Create A new file

# Replace data of file

with open("demo.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","Python")
print(new_data)

with open("demo.txt","w") as f:
    f.write(new_data)

# searching data in existing file.

with open("demo.txt","r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print("Yes, learning is found !")
    else:
        print("No, learning is not found")







   






    
