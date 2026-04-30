import requests

def get_shopee_products():

    # placeholder API (você pode trocar pela oficial de afiliados)
    url = "https://shopee-api-placeholder/search"

    r = requests.get(url, timeout=10)
    data = r.json()

    return [
        {
            "title": i["name"],
            "price": i["price"],
            "sold": i["sold"],
            "link": i["url"],
            "commission": 10
        }
        for i in data.get("items", [])
    ]