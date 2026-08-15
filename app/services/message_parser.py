from typing import Any


def extract_message_text(
    message: dict[str, Any],
) -> str:
    message_type = message.get("type", "")

    if message_type == "text":
        return (
            message
            .get("text", {})
            .get("body", "")
            .strip()
        )

    if message_type == "button":
        return (
            message
            .get("button", {})
            .get("text", "")
            .strip()
        )

    if message_type == "interactive":
        interactive = message.get("interactive", {})

        button_reply = interactive.get(
            "button_reply",
            {},
        )
        if button_reply:
            return button_reply.get(
                "title",
                "",
            ).strip()

        list_reply = interactive.get(
            "list_reply",
            {},
        )
        if list_reply:
            return list_reply.get(
                "title",
                "",
            ).strip()

    if message_type in {"image", "document", "video"}:
        return (
            message
            .get(message_type, {})
            .get("caption", "")
            .strip()
        )

    return ""


def extract_messages(
    payload: dict[str, Any],
) -> list[dict[str, str]]:
    extracted_messages: list[dict[str, str]] = []

    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            if change.get("field") != "messages":
                continue

            value = change.get("value", {})

            contacts = {
                contact.get("wa_id", ""): (
                    contact
                    .get("profile", {})
                    .get("name", "")
                )
                for contact in value.get("contacts", [])
            }

            for message in value.get("messages", []):
                phone_number = message.get("from", "")

                extracted_messages.append(
                    {
                        "message_id": message.get(
                            "id",
                            "",
                        ),
                        "phone_number": phone_number,
                        "customer_name": contacts.get(
                            phone_number,
                            "",
                        ),
                        "timestamp": message.get(
                            "timestamp",
                            "",
                        ),
                        "message_type": message.get(
                            "type",
                            "",
                        ),
                        "message_text": (
                            extract_message_text(
                                message
                            )
                        ),
                    }
                )

    return extracted_messages