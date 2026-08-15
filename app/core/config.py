from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    webhook_verify_token: str

    google_service_account_file: str
    google_worksheet_name: str = "Leads"
    google_sheet_id: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()