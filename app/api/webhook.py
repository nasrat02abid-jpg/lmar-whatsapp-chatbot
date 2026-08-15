from typing import Any

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import PlainTextResponse

from app.core.config import settings
from app.services.message_parser import extract_messages


router = APIRouter(
    prefix="/webhook",
    tags=["Meta WhatsApp Webhook"],
)


@router.get("", response_class=PlainTextResponse)
def verify_webhook(
    mode: str = Query(alias="hub.mode"),
    verify_token: str = Query(alias="hub.verify_token"),
    challenge: str = Query(alias="hub.challenge"),
):
    if (
        mode == "subscribe"
        and verify_token == settings.webhook_verify_token
    ):
        return challenge

    raise HTTPException(
        status_code=403,
        detail="Webhook verification failed.",
    )


@router.post("")
async def receive_webhook(
    payload: dict[str, Any],
):
    messages = extract_messages(payload)

    status_count = 0

    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            status_count += len(
                value.get("statuses", [])
            )

    return {
        "status": "received",
        "message_count": len(messages),
        "status_count": status_count,
        "messages": messages,
    }