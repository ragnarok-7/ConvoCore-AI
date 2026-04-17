from app.chatbot.llm_client import ask_llm


def detect_intent(user_input):

    prompt = f"""
    Classify the user query into ONE of these categories:

    greeting
    product_query
    brochure_request
    escalation
    general_query

    ONLY return one word.

    Query: {user_input}
    """

    intent = ask_llm(prompt).strip().lower()

    return intent