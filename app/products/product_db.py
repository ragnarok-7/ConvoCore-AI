import json

def load_products():

    with open("database/products.json", "r") as file:
        
        products = json.load(file)

        return products