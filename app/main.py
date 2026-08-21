from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

from app.api.webhook import router as webhook_router


app = FastAPI(
    title="LMAR Lead Assistant API",
    description=(
        "Meta WhatsApp Cloud API chatbot and lead automation "
        "system developed for LMAR Marketing."
    ),
    version="1.0.0",
)

# مهم: اصلي webhook، message parser او Google Sheets integration
app.include_router(webhook_router)


@app.get("/")
def root():
    return {
        "status": "online",
        "message": "LMAR Lead Assistant API is running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "LMAR Lead Assistant",
    }


@app.get("/privacy", response_class=HTMLResponse)
def privacy_policy():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >
        <title>LMAR Lead Assistant Privacy Policy</title>
    </head>

    <body style="
        max-width:800px;
        margin:40px auto;
        padding:0 20px;
        font-family:Arial,sans-serif;
        line-height:1.6;
        color:#222;
    ">
        <h1>LMAR Lead Assistant Privacy Policy</h1>

        <p>
            LMAR Lead Assistant is a customer inquiry and
            lead-management automation service developed by
            <strong>Nasrat Abid — Data & AI Automation</strong>
            for LMAR Marketing.
        </p>

        <h2>Information We Collect</h2>

        <p>
            We may collect customer names, phone numbers, WhatsApp
            messages, property interests, inquiry details, message
            identifiers, and follow-up information.
        </p>

        <h2>How We Use Information</h2>

        <p>
            Information is used to respond to inquiries, recommend
            properties, provide pricing information, arrange site
            visits, schedule follow-ups, assign sales agents, and
            provide customer support.
        </p>

        <h2>Google Sheets and Internal Systems</h2>

        <p>
            Customer inquiry information may be stored in restricted
            Google Sheets or internal lead-management systems that
            are accessible only to authorized personnel.
        </p>

        <h2>Data Sharing</h2>

        <p>
            We do not sell customer information. Access is limited
            to authorized LMAR Marketing personnel and service
            providers required to operate and secure the system.
        </p>

        <h2>Data Security</h2>

        <p>
            Reasonable administrative and technical safeguards are
            used to protect customer information from unauthorized
            access, disclosure, alteration, or loss.
        </p>

        <h2>Data Retention and Deletion</h2>

        <p>
            Information is retained only for as long as necessary
            for customer service, business, security, and legal
            purposes. Customers may request deletion of their data.
        </p>

        <h2>Contact</h2>

        <p>
            Nasrat Abid — Data & AI Automation<br>
            Email:
            <a href="mailto:nasrat02abid@gmail.com">
                nasrat02abid@gmail.com
            </a>
        </p>

        <p><em>Last updated: 21 August 2026</em></p>
    </body>
    </html>
    """


@app.head("/privacy", include_in_schema=False)
def privacy_policy_head():
    return Response(
        status_code=200,
        media_type="text/html",
    )


@app.get("/terms", response_class=HTMLResponse)
def terms_of_service():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >
        <title>LMAR Lead Assistant Terms of Service</title>
    </head>

    <body style="
        max-width:800px;
        margin:40px auto;
        padding:0 20px;
        font-family:Arial,sans-serif;
        line-height:1.6;
        color:#222;
    ">
        <h1>LMAR Lead Assistant Terms of Service</h1>

        <p>
            LMAR Lead Assistant is a customer inquiry and
            lead-management automation service developed by
            <strong>Nasrat Abid — Data & AI Automation</strong>
            for LMAR Marketing.
        </p>

        <h2>Purpose of the Service</h2>

        <p>
            This service helps customers communicate with LMAR
            Marketing about real estate inquiries, available
            properties, pricing, payment plans, site visits, and
            follow-ups.
        </p>

        <h2>User Responsibilities</h2>

        <p>
            Users must provide accurate information and must not
            misuse, disrupt, reverse engineer, or attempt
            unauthorized access to the service.
        </p>

        <h2>Property Information</h2>

        <p>
            Property availability, prices, locations, payment plans,
            possession dates, and other details are subject to final
            confirmation by LMAR Marketing.
        </p>

        <h2>No Investment Guarantee</h2>

        <p>
            Information provided through this service does not
            represent a guarantee of property availability,
            investment returns, or future market performance.
        </p>

        <h2>Service Availability</h2>

        <p>
            We may update, suspend, or discontinue parts of the
            service when required for maintenance, security, legal,
            or operational reasons.
        </p>

        <h2>Contact</h2>

        <p>
            Nasrat Abid — Data & AI Automation<br>
            Email:
            <a href="mailto:nasrat02abid@gmail.com">
                nasrat02abid@gmail.com
            </a>
        </p>

        <p><em>Last updated: 21 August 2026</em></p>
    </body>
    </html>
    """


@app.head("/terms", include_in_schema=False)
def terms_of_service_head():
    return Response(
        status_code=200,
        media_type="text/html",
    )


@app.get("/data-deletion", response_class=HTMLResponse)
def data_deletion():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >
        <title>LMAR Lead Assistant Data Deletion</title>
    </head>

    <body style="
        max-width:800px;
        margin:40px auto;
        padding:0 20px;
        font-family:Arial,sans-serif;
        line-height:1.6;
        color:#222;
    ">
        <h1>LMAR Lead Assistant — User Data Deletion</h1>

        <p>
            LMAR Lead Assistant is developed by
            <strong>Nasrat Abid — Data & AI Automation</strong>
            for LMAR Marketing.
        </p>

        <h2>How to Request Data Deletion</h2>

        <p>
            To request deletion of your personal information,
            send an email to:
        </p>

        <p>
            <strong>
                <a href="mailto:nasrat02abid@gmail.com">
                    nasrat02abid@gmail.com
                </a>
            </strong>
        </p>

        <p>
            Use the email subject:
            <strong>Data Deletion Request</strong>.
        </p>

        <h2>Information to Include</h2>

        <ul>
            <li>Your full name</li>
            <li>Your WhatsApp phone number</li>
            <li>
                A short description of the information you want
                deleted
            </li>
        </ul>

        <h2>Deletion Process</h2>

        <p>
            After identity verification, LMAR Marketing will delete
            the applicable customer, lead, and conversation records,
            except information that must be retained for legal,
            fraud-prevention, security, or regulatory purposes.
        </p>

        <h2>Processing Time</h2>

        <p>
            Valid deletion requests will normally be processed
            within 30 days.
        </p>

        <h2>Contact</h2>

        <p>
            Nasrat Abid — Data & AI Automation<br>
            Email:
            <a href="mailto:nasrat02abid@gmail.com">
                nasrat02abid@gmail.com
            </a>
        </p>

        <p><em>Last updated: 21 August 2026</em></p>
    </body>
    </html>
    """


@app.head("/data-deletion", include_in_schema=False)
def data_deletion_head():
    return Response(
        status_code=200,
        media_type="text/html",
    )