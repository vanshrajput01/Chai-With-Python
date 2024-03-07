# insert and delete data on user Choice

print("User chioce is : \n1.insert data\n2.show All data")

def insert_data(data):
    with open("data_File.txt","a") as f:
        f.write(data)
        print("Data Inserted Success Fully.")

def show_data():
    with open("data_File.txt","r") as f:
        file_data = f.read()
        print(file_data)
    
def main(c = 1):
    match c:
        case 1:
            name = input("Enter youtube vedio name : ")
            time = input("Enter vedio time : ")
            data = f"{name} : {time}"
            insert_data(data)
        case 2:
            show_data()
        case _ :
            print("Enter a valid choice")

choice = int(input("Enter Your chioce : "))
main(choice)



