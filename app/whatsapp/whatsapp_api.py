from fastapi import APIRouter, Request
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse

from app.api import chat_api, Query

router = APIRouter()


@router.post("/whatsapp")
async def whatsapp_reply(request: Request):

    try:
        # 🔹 Read incoming data from Twilio
        form = await request.form()

        user_msg = form.get("Body", "")
        sender = form.get("From", "unknown")

        print("\n📩 Incoming WhatsApp Message:")
        print("User:", user_msg)
        print("Sender:", sender)

        # 🔹 Send to chatbot logic
        query = Query(message=user_msg, session_id=sender)
        result = chat_api(query)

        reply = ""

        # 🔹 Handle different response types
        if result["type"] == "product":
            for p in result["data"]:
                reply += f"{p['name']} - {p['price']}\n"

            if result.get("follow_up"):
                reply += "\n" + result["follow_up"]

        elif result["type"] == "ai":
            reply = result["response"]

        elif result["type"] == "brochure":
            reply = "📄 Brochure available. Reply with Email / WhatsApp / Download."

        elif result["type"] == "escalation":
            reply = result["message"]

        else:
            reply = "Sorry, I couldn't understand that."

        print("🤖 Bot Reply:", reply)

        # 🔹 Create Twilio XML response
        twilio_response = MessagingResponse()
        twilio_response.message(reply)

        # 🔥 IMPORTANT: Return XML response (NOT string)
        return Response(
            content=str(twilio_response),
            media_type="application/xml"
        )

    except Exception as e:
        print("❌ WhatsApp Error:", e)

        twilio_response = MessagingResponse()
        twilio_response.message("Server error. Please try again.")

        return Response(
            content=str(twilio_response),
            media_type="application/xml"
        )