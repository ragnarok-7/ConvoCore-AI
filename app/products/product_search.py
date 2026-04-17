products = [
    {
        "name": "Industrial Ball Valve",
        "price": "Rs. 2500",
        "category": "Valves",
        "description": "High pressure stainless steel valve",
        "stock": "Available"
    }
]


def find_products(query):

    query_words = query.lower().split()
    results = []

    for p in products:
        name_words = p["name"].lower().split()

        if any(word in name_words for word in query_words):
            results.append(p)

    return results


def find_unknown_products(query):
    return []