from app.chatbot.llm_client import ask_llm

def identify_product_from_image(image_path):

    prompt = f"""
    A customer uploaded image named {image_path}.

    Guess which product it is from:
    Industrial Ball Valve
    Pipe Flange
    Industrial Gasket

    Return only product name.
    """

    result = ask_llm(prompt)

    return result