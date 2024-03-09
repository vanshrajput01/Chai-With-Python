import requests

def fetch_random_product():

    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        product_details = data["data"]
        products_list = product_details["data"]

        product_category = products_list[0]["id"]
        product_price = products_list[0]["price"]
        product_id = products_list[0]["id"]
        product_name = products_list[0]["title"]

        print(f"Product details is\nProduct name : {product_name}\nProduct id : {product_id}\nProduct Price : {product_price}\nProduct category  : {product_category}")
    




    

    else:
        raise Exception("Failed to fetch User data!!")




def main():
    try:
        fetch_random_product()
        
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()


    

    




