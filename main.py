from apis.shopee import get_shopee_products
from apis.mercadolivre import get_ml_products
from apis.amazon import get_amazon_products
from engine.ranker import rank_products
from telegram import send_telegram

def run():

    products = []

    try:
        products += get_shopee_products()
    except:
        print("Shopee offline")

    try:
        products += get_ml_products()
    except:
        print("Mercado Livre offline")

    try:
        products += get_amazon_products()
    except:
        print("Amazon offline")

    if not products:
        print("Sem produtos disponíveis")
        return

    ranked = rank_products(products)

    for p in ranked[:5]:
        msg = f"""🔥 OFERTA TOP

📦 {p['title']}
💰 R$ {p['price']}
📊 Score: {p['score']}
👉 {p['link']}
"""
        send_telegram(msg)

if __name__ == "__main__":
    run()