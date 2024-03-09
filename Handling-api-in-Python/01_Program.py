import requests

def fetch_random_user_details():

    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    print(data)


def main():
    try:
        fetch_random_user_details()
    except Exception as e:
        print("Error : {e}")


if __name__ == "__main__":
    main()


    

    




