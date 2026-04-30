import requests

def get_ml_products():

    url = "https://api.mercadolivre.com/sites/MLB/search"

    params = {
        "q": "smartphone",
        "limit": 20
    }

    r = requests.get(url, params=params, timeout=10)
    data = r.json()

    products = []

    for item in data.get("results", []):

        products.append({
            "title": item["title"],
            "price": item["price"],
            "sold": item.get("sold_quantity", 0),
            "link": item["permalink"],
            "commission": 5
        })

    return products