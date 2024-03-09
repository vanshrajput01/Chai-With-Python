import requests

def fetch_random_user_details():

    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()


def main():
    pass

if __name__ == "__main__":
    main()


    

    




