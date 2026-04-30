import requests

def get_amazon_products():

    url = "https://api.amazon-paapi.com/search"

    # exemplo estrutural (você conecta depois com sua chave afiliado)
    return [
        {
            "title": "Produto Amazon exemplo",
            "price": 199,
            "sold": 1000,
            "link": "https://amazon.com",
            "commission": 8
        }
    ]