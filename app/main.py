from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

from app.api.webhook import router as webhook_router


app = FastAPI(
    title="LMAR Lead Assistant API",
    description="API services for LMAR Marketing automation",
    version="1.0.0",
)

# Existing Meta webhook + Google Sheets integration
app.include_router(webhook_router)


@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "LMAR Lead Assistant API is running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/privacy", response_class=HTMLResponse)
def privacy_policy():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LMAR Lead Assistant - Privacy Policy</title>
    </head>
    <body style="max-width:800px;margin:40px auto;padding:0 20px;
                 font-family:Arial,sans-serif;line-height:1.6;color:#333;">
        <h1>LMAR Lead Assistant Privacy Policy</h1>

        <p>
            LMAR Lead Assistant is a customer inquiry and lead-management
            automation service developed by
            <strong>Nasrat Abid — Data & AI Automation</strong>
            for LMAR Marketing.
        </p>

        <h2>Information We Collect</h2>
        <p>
            We may collect customer names, phone numbers, messages,
            property interests, and follow-up information.
        </p>

        <h2>How We Use Information</h2>
        <p>
            Information is used to respond to inquiries, recommend properties,
            arrange site visits, schedule follow-ups, and provide support.
        </p>

        <h2>Data Sharing</h2>
        <p>
            We do not sell customer information. Access is limited to
            authorized personnel and service providers required to operate
            the system.
        </p>

        <h2>Data Retention and Deletion</h2>
        <p>
            Information is retained only as needed for customer service,
            security, and legal obligations. Users may request deletion.
        </p>

        <h2>Contact</h2>
        <p>
            Nasrat Abid — Data & AI Automation<br>
            Email: nasrat02abid@gmail.com
        </p>

        <p><em>Last updated: 18 August 2026</em></p>
    </body>
    </html>
    """


@app.head("/privacy", include_in_schema=False)
def privacy_policy_head():
    return Response(status_code=200, media_type="text/html")
