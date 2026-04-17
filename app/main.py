from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# routers
from app.whatsapp.whatsapp_api import router as whatsapp_router
from app.api import chat_api, Query

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# static
app.mount("/brochures", StaticFiles(directory="database/brochures"), name="brochures")


# 🔥 DIRECT ROUTE (NO IMPORT CONFUSION)
@app.post("/chat")
def chat(query: Query):
    return chat_api(query)


# 🔥 WHATSAPP ROUTE
app.include_router(whatsapp_router)


@app.get("/")
def home():
    return {"message": "Server running"}