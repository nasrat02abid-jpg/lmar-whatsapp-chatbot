from fastapi import FastAPI

from app.api.webhook import router as webhook_router


app = FastAPI(
    title="LMAR WhatsApp Chatbot API",
    description=(
        "Meta WhatsApp Cloud API chatbot and "
        "lead automation system for LMAR Marketing."
    ),
    version="1.0.0",
)

app.include_router(webhook_router)


@app.get("/")
def root():
    return {
        "message": "LMAR WhatsApp Chatbot API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }