from typing import Any

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import PlainTextResponse

from app.core.config import settings
from app.services.google_sheets_service import (
    append_lead,
    message_id_exists,
)
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
    saved_count = 0
    duplicate_count = 0

    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            status_count += len(
                value.get("statuses", [])
            )

    for message in messages:
        message_id = message.get("message_id", "")

        if message_id_exists(message_id):
            duplicate_count += 1
            continue

        phone_number = message.get(
            "phone_number",
            "",
        )

        if (
            phone_number
            and not phone_number.startswith("+")
        ):
            phone_number = f"+{phone_number}"

        append_lead(
            {
                "client_name": message.get(
                    "customer_name",
                    "",
                ),
                "phone_number": phone_number,
                "project": "Other",
                "lead_status": "Information Only",
                "remarks": message.get(
                    "message_text",
                    "",
                ),
                "lead_source": "WhatsApp Chatbot",
                "message_id": message_id,
                "chatbot_stage": "Initial Contact",
            }
        )

        saved_count += 1

    return {
        "status": "received",
        "message_count": len(messages),
        "saved_count": saved_count,
        "duplicate_count": duplicate_count,
        "status_count": status_count,
    }