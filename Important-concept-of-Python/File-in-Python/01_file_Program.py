# File in Python

# Read File using Python

# try:
#     file_name = input("Enter your file name : ")
#     f = open(file_name,"r")
#     data = f.read()
#     print(f"Your file data is : \n{data}")
#     f.close()

# except:
#     print(f"ERROR  : File is not found.")
# finally:
#     print("Your Program run success Fully.")

# write the File using Python
# w this mode overwrite the file....
f = open("02_sample_File.txt","w")
f.write("This is Modified File using w mode.")
print("File write Success Fully.")
f.close()



