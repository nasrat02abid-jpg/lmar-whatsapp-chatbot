from fastapi.responses import HTMLResponse, Response


@app.get("/privacy", response_class=HTMLResponse)
def privacy_policy():
    return """
    <html>
    <body style="max-width:800px;margin:40px auto;font-family:Arial;line-height:1.6">
        <h1>LMAR Lead Assistant Privacy Policy</h1>

        <p>LMAR Lead Assistant is a customer inquiry and lead-management
        automation service developed by <strong>Nasrat Abid — Data & AI
        Automation</strong> for LMAR Marketing.</p>

        <h2>Information We Collect</h2>
        <p>We may collect customer names, phone numbers, WhatsApp messages,
        property interests, and follow-up information.</p>

        <h2>How We Use Information</h2>
        <p>Information is used to respond to inquiries, recommend properties,
        arrange site visits, schedule follow-ups, and provide customer support.</p>

        <h2>Data Sharing</h2>
        <p>We do not sell customer information. Access is limited to authorized
        LMAR Marketing personnel and service providers needed to operate the system.</p>

        <h2>Data Retention and Deletion</h2>
        <p>Information is retained only as required for customer service,
        security, and legal obligations. Users may request deletion through
        our data-deletion page.</p>

        <h2>Contact</h2>
        <p>Nasrat Abid — Data & AI Automation<br>
        Email: nasrat02abid@gmail.com</p>

        <p>Last updated: 18 August 2026</p>
    </body>
    </html>
    """


@app.head("/privacy", include_in_schema=False)
def privacy_policy_head():
    return Response(status_code=200, media_type="text/html")