# 🤖 ConvoCore AI

**ConvoCore AI** is an intelligent, multi-channel customer support agent designed to handle real-time conversations across **Web and WhatsApp**.  
It combines **AI-driven responses**, **product intelligence**, and **automation** to deliver seamless customer interactions.

---

## 🚀 Features

- 💬 AI-powered conversational chatbot
- 📲 WhatsApp integration using Twilio
- 🌐 Web-based chat interface
- 📦 Smart product search & recommendations
- 💰 Context-aware pricing responses
- 📄 Brochure request handling
- 🧠 Session-based conversational memory
- 🔁 Intent detection (greeting, product, pricing, etc.)
- ⚡ Real-time responses via FastAPI

---

## 🏗️ Tech Stack

| Layer       | Technology               |
| ----------- | ------------------------ |
| Backend     | FastAPI (Python)         |
| AI Engine   | LLM (Gemini / API-based) |
| Frontend    | HTML, CSS, JavaScript    |
| Messaging   | Twilio WhatsApp API      |
| Tunneling   | ngrok                    |
| Environment | Python 3.10+             |

---

## 📁 Project Structure

app/
├── main.py # FastAPI entry point
├── api.py # Core chatbot logic
├── chatbot/
│ ├── llm_client.py
│ └── intent_classifier.py
├── products/
│ └── product_search.py
├── whatsapp/
│ └── whatsapp_api.py
├── crm/
│ └── crm_manager.py
├── escalation/
│ └── human_handoff.py

database/
└── brochures/

frontend/
└── index.html

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/convocore-ai-agent.git
cd convocore-ai-agent
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run FastAPI Server
uvicorn app.main:app --reload --port 8000
5️⃣ Start ngrok
ngrok http 8000
6️⃣ Configure Twilio WhatsApp Sandbox
Go to Twilio Sandbox
Set webhook:
https://your-ngrok-url.ngrok.io/whatsapp
Join sandbox by sending code on WhatsApp
🧪 Usage
💻 Web Chat

Open:

frontend/index.html
📱 WhatsApp Chat

Send messages like:

hello
industrial valve
price
send brochure
🔥 Example Interaction

User: industrial valve
Bot:
Industrial Ball Valve - Rs. 2500
Want pricing or specs?

🧠 How It Works
User sends message (Web / WhatsApp)
Request hits FastAPI backend
Intent detection + product matching
AI fallback for general queries
Response formatted
Delivered via Web UI or WhatsApp
⚠️ Current Limitations
In-memory session storage (not persistent)
Basic intent classification
Limited product dataset
No analytics dashboard yet
🚀 Future Enhancements
🗄️ MongoDB for persistent chat memory
📊 Admin dashboard for analytics
📩 Email & WhatsApp brochure delivery automation
🎨 Advanced UI with animations & personalization
🧠 Improved contextual AI responses
🌍 Multi-language support
👨‍💻 Author

Ankush Patra
B.Tech CSE | AI & Full Stack Developer

📜 License

This project is licensed under the MIT License.


---
```
