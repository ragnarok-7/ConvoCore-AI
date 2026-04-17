from app.chatbot.llm_client import ask_llm
from app.products.product_search import find_products, find_unknown_products
from app.escalation.human_handoff import escalate_query
from app.image_ai.image_identifier import identify_product_from_image
from app.brochure.brochure_sender import get_download_links
from app.brochure.contact_capture import save_lead
from app.crm.crm_manager import log_customer_interaction


SYSTEM_PROMPT = """
You are a professional customer support AI for Panchal Enterprises.

Be polite.
Be helpful.
Be concise.

Company sells:
Industrial valves
Pipe fittings
Flanges
Gaskets
Pumps

Answer like a real support executive.
"""


# =========================
# INTENT DETECTION
# =========================

def detect_intent(user_input):

    text = user_input.lower()

    if "brochure" in text:
        return "brochure"

    if text.startswith("image:"):
        return "image"

    if "what products" in text:
        return "general_products"

    if "what do you sell" in text:
        return "general_products"

    if "catalog" in text:
        return "general_products"

    if "hello" in text or "hi" in text:
        return "greeting"

    return "query"



# =========================
# MAIN CHAT LOOP
# =========================

def chat():

    print("\nPanchal Enterprises Support AI Ready")
    print("Type 'exit' to quit\n")

    while True:

        user_input = input("Customer: ")

        if user_input.lower() == "exit":

            print("\nAI: Thank you for contacting Panchal Enterprises!")

            break


        intent = detect_intent(user_input)


        # =========================
        # GREETING
        # =========================

        if intent == "greeting":

            response = ask_llm("Greet customer professionally")

            print("\nAI:",response)

            log_customer_interaction(user_input,None)

            continue


        # =========================
        # GENERAL PRODUCT QUESTIONS
        # =========================

        if intent == "general_products":

            response = ask_llm(
                "Explain what products Panchal Enterprises sells in a short list"
            )

            print("\nAI:",response)

            log_customer_interaction(user_input,None)

            continue


        # =========================
        # BROCHURE SYSTEM
        # =========================

        if intent == "brochure":

            print("\nAI: I can share our brochures with you.")

            print("Options:")
            print("Email")
            print("WhatsApp")
            print("Direct download")

            choice = input("\nEnter email/phone or type skip: ")

            if "@" in choice:

                save_lead(email=choice)

                print("\nAI: Thank you. Brochure will be sent to your email.")

                log_customer_interaction(user_input,None)

                continue


            elif choice.isdigit():

                save_lead(phone=choice)

                print("\nAI: Thank you. Brochure will be shared via WhatsApp.")

                log_customer_interaction(user_input,None)

                continue


            else:

                links = get_download_links()

                print("\nAI: Here are download links:\n")

                for link in links:

                    print(link)

                log_customer_interaction(user_input,None)

                continue


        # =========================
        # IMAGE DETECTION
        # =========================

        if intent == "image":

            image_path = user_input.replace("image:","").strip()

            product_name = identify_product_from_image(image_path)

            products = find_products(product_name)

            if products:

                print("\nAI: Product identified:\n")

                for product in products:

                    print("-------------------")

                    print("Name:",product["name"])
                    print("Price:",product["price"])
                    print("Stock:",product["stock"])

            else:

                print("\nAI: Could not identify product.")

            log_customer_interaction(user_input,None)

            continue


        # =========================
        # PRODUCT SEARCH
        # =========================

        products = find_products(user_input)

        product_names = []

        if products:

            print("\nAI: Product Details:\n")

            for product in products:

                print("-------------------")

                print("Name:",product["name"])
                print("Category:",product["category"])
                print("Price:",product["price"])
                print("Description:",product["description"])
                print("Applications:",product["applications"])
                print("Stock:",product["stock"])

                product_names.append(product["name"])


            log_customer_interaction(user_input,product_names)


            if len(product_names) >= 2:

                print("\nAI: Our sales team has been notified for bulk inquiry.")

            continue


        # =========================
        # UNKNOWN PRODUCT ESCALATION
        # =========================

        unknown = find_unknown_products(user_input)

        if unknown:

            escalate_query(user_input)

            print("\nAI: I couldn't find this product.")

            print("Our sales team will contact you.")

            log_customer_interaction(user_input,None)

            continue


        # =========================
        # AI FALLBACK
        # =========================

        prompt = f"""
        {SYSTEM_PROMPT}

        Customer question:
        {user_input}

        Respond professionally.
        """

        response = ask_llm(prompt)

        print("\nAI:",response)

        log_customer_interaction(user_input,None)