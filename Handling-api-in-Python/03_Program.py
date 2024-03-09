import requests

def fetch_books_details():
    url = "https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        all_book_details = data["data"]
        book_details = all_book_details["data"]
        for book in range(0,len(book_details)):
            print("Book id is",book_details[book]["id"])
            print("Book Author is", book_details[book]["volumeInfo"]["authors"][0])
            print("Book Description is", book_details[book]["volumeInfo"]["description"])


    else:
        raise Exception("Failed to fetch data")
    



def main():
    try:
        fetch_books_details()
    except Exception as e:
        print("ERROR :",e)
if __name__ == "__main__":
    main() 