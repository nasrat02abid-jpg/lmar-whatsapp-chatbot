from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import gspread

from app.core.config import settings


def get_worksheet() -> gspread.Worksheet:
    credentials_path = Path(
        settings.google_service_account_file
    )

    if not credentials_path.is_absolute():
        credentials_path = Path.cwd() / credentials_path

    if not credentials_path.exists():
        raise FileNotFoundError(
            f"Service-account file not found: {credentials_path}"
        )

    client = gspread.service_account(
        filename=str(credentials_path)
    )

    spreadsheet = client.open_by_key(
        settings.google_sheet_id
    )

    return spreadsheet.worksheet(
        settings.google_worksheet_name
    )


def test_google_sheets_connection() -> dict[str, Any]:
    worksheet = get_worksheet()

    return {
        "connected": True,
        "spreadsheet": worksheet.spreadsheet.title,
        "worksheet": worksheet.title,
        "rows": worksheet.row_count,
        "columns": worksheet.col_count,
    }


def append_lead(
    lead: dict[str, Any],
) -> dict[str, Any]:
    worksheet = get_worksheet()

    serial_number = len(
        worksheet.col_values(1)
    )

    date_added = datetime.now(
        ZoneInfo("Asia/Karachi")
    ).strftime("%Y-%m-%d %H:%M:%S")

    row = [
        serial_number,
        date_added,
        lead.get("client_name", ""),
        lead.get("phone_number", ""),
        lead.get("project", "Other"),
        lead.get("lead_status", "Information Only"),
        lead.get("assigned_agent", ""),
        lead.get("last_contact_date", ""),
        lead.get("next_follow_up_date", ""),
        lead.get("remarks", ""),
        lead.get("lead_source", "WhatsApp"),
        lead.get("message_id", ""),
        lead.get("chatbot_stage", "New Lead"),
    ]

    worksheet.append_row(
        row,
        value_input_option="USER_ENTERED",
        table_range="A:M",
    )

    return {
        "saved": True,
        "serial_number": serial_number,
        "phone_number": lead.get(
            "phone_number",
            "",
        ),
    }


def message_id_exists(
    message_id: str,
) -> bool:
    if not message_id:
        return False

    worksheet = get_worksheet()

    existing_cell = worksheet.find(
        message_id,
        in_column=12,
    )

    return existing_cell is not None