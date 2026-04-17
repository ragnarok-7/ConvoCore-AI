from pydantic import BaseModel

from app.chatbot.llm_client import ask_llm
from app.chatbot.intent_classifier import detect_intent
from app.products.product_search import find_products


# memory
session_memory = {}

class Query(BaseModel):
    message: str
    session_id: str


def chat_api(query: Query):

    user_input = query.message.strip()
    session_id = query.session_id

    if session_id not in session_memory:
        session_memory[session_id] = []

    memory = session_memory[session_id]
    memory.append({"role": "user", "content": user_input})

    lower = user_input.lower()

    if "how are you" in lower:
        return {"type": "ai", "response": "I'm doing great 🙂 How can I help you?"}

    if "my name is" in lower or "i am" in lower:
        name = user_input.split()[-1]
        return {"type": "ai", "response": f"Nice to meet you, {name}! 😊"}

    if "price" in lower or "cost" in lower:
        for item in reversed(memory):
            if "last_products" in item:
                products = find_products(" ".join(item["last_products"]))
                if products:
                    p = products[0]
                    return {
                        "type": "ai",
                        "response": f"{p['name']} costs {p['price']}."
                    }

        return {"type": "ai", "response": "Which product do you want the price for?"}

    products = find_products(user_input)

    if products:
        data = []
        names = []

        for p in products:
            data.append(p)
            names.append(p["name"])

        memory.append({"last_products": names})

        return {
            "type": "product",
            "data": data,
            "follow_up": "Want pricing or specs?"
        }

    intent = detect_intent(user_input).strip().lower()

    if intent == "greeting":
        return {"type": "ai", "response": "Hi 👋 How can I help you?"}

    if intent == "brochure_request":
        return {"type": "brochure"}

    response = ask_llm(user_input)

    return {"type": "ai", "response": response}