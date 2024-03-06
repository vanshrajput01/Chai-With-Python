# File in Python

# Read File using Python

try:
    file_name = input("Enter your file name : ")
    f = open(file_name,"r")
    data = f.read()
    print(f"Your file data is : \n{data}")
    f.close()

except:
    print(f"ERROR  : File is not found.")
finally:
    print("Your Program run success Fully.")

# write the File using Python
# w this mode overwrite the file....
f = open("02_sample_File.txt","w")
f.write("This is Modified File using w mode.")
print("File write Success Fully.")
f.close()

# write the File using Python
# a this mode not overwrite the file....
f = open("02_sample_File.txt","a")
f.write("This file is also text file.")
print("File write success Fully.")
f.close()
print("File close success Fully.")

# r+ mode in file : Read & Write

f = open("03_sample_File.txt","r+")
f.write("abd file") # Over write and add data from begin
print(f.read()) # in this mode complete data is not printed of the file.
f.close()

# w+ mode in file : Read & write

f = open("04_sample_File.txt","w+") # that mode delete all file data.
f.write("Modified file.")
print(f.read()) # not print anything.
f.close()

# a+ mode in python : Read & write

f = open("05_sample_File.txt","a+")
f.write("adc") # not over write file using this mode to add data in end.
print(f.read()) # not print any thing
f.close()



















