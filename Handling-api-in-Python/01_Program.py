import requests

def fetch_random_user_details():

    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_details = data["data"]
        user_name = user_details["login"]["username"]
        user_password = user_details["login"]["password"]
        user_email = user_details["email"]

        print(f"User details\nUser Name : {user_name}\nUser Password : {user_password}\nUser Email : {user_email} ")

    else:
        raise Exception("Failed to fetch User data!!")




def main():
    try:
        fetch_random_user_details()
    except Exception as e:
        print("Error : {e}")


if __name__ == "__main__":
    main()


    

    




