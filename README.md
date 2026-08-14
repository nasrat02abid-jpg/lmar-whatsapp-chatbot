# LMAR WhatsApp Chatbot

A professional WhatsApp lead qualification and automation system for LMAR Marketing Real Estate Company.

The system uses Meta's official WhatsApp Cloud API to respond to customers, collect property requirements, qualify leads, send project information, schedule follow-ups, and automatically store leads in the LMAR Multi-Agent Lead Management System.

## Project Status

Currently under active development.

## Main Objectives

* Respond to WhatsApp customers within seconds
* Operate 24 hours a day, 7 days a week
* Collect and qualify real estate leads automatically
* Send project details and brochures
* Route leads to the appropriate sales agent
* Store WhatsApp leads in Google Sheets
* Integrate with the LASOS Real Estate CRM
* Reduce missed leads and delayed follow-ups

## Core Features

* Multilingual chatbot: Pashto, Urdu, and English
* Customer name and phone-number capture
* Buyer, seller, rent, and investment inquiry flows
* Project and property-type selection
* Budget and buying-timeline collection
* Hot, warm, and information-only lead classification
* Automatic agent assignment
* PDF brochure and property-media delivery
* Site-visit request and scheduling
* Human sales-agent handover
* Follow-up reminders
* Duplicate-message protection
* Conversation-history recording
* Google Sheets lead synchronization
* LASOS CRM integration

## Technology Stack

* Python 3
* FastAPI
* Uvicorn
* Meta WhatsApp Cloud API
* Meta Graph API
* Google Sheets API
* Google Service Account
* gspread
* HTTPX
* Pydantic
* python-dotenv
* Render or Railway for deployment
* GitHub for version control

## System Workflow

1. A customer sends a message to the LMAR WhatsApp number.
2. Meta sends the message to the FastAPI webhook.
3. The chatbot identifies the customer's current conversation stage.
4. The chatbot asks qualification questions.
5. The customer's answers are validated and stored.
6. The lead is classified and assigned to a sales agent.
7. The completed lead is added to the WhatsApp Chatbot Leads Sheet.
8. The lead is synchronized with the LMAR Master Sheet and LASOS CRM.
9. The assigned agent receives the lead for follow-up.

## Lead Information Collected

* Date added
* Client name
* Phone number
* Project
* Property type
* Budget
* Lead status
* Assigned agent
* Last contact date
* Next follow-up date
* Conversation summary
* Lead source
* WhatsApp message ID
* Chatbot stage

## Planned Project Structure

```text
lmar-whatsapp-chatbot/
├── app/
│   ├── api/
│   │   └── webhook.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── services/
│   │   ├── whatsapp_service.py
│   │   ├── chatbot_service.py
│   │   ├── google_sheets_service.py
│   │   └── agent_routing_service.py
│   ├── models/
│   ├── schemas/
│   └── main.py
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Environment Variables

The application requires the following environment variables:

```text
WHATSAPP_ACCESS_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_BUSINESS_ACCOUNT_ID=
META_APP_SECRET=
WEBHOOK_VERIFY_TOKEN=
GOOGLE_SHEET_ID=
GOOGLE_SERVICE_ACCOUNT_JSON=
```

Actual credentials must never be uploaded to GitHub.

## Security

* The repository must remain private during development.
* Access tokens and passwords are stored only in environment variables.
* The `.env` file is excluded from Git.
* Meta webhook requests will be verified.
* Customer data will not be stored in the GitHub repository.
* Sensitive actions will require authorized access.
* AI will not delete leads, confirm payments, or send sensitive messages without human approval.

## Development Phases

### Phase 1: Foundation

* Repository setup
* FastAPI project structure
* Environment configuration
* Meta webhook verification

### Phase 2: WhatsApp Messaging

* Receive incoming messages
* Send text and interactive replies
* Track conversation stages

### Phase 3: Lead Qualification

* Collect customer information
* Select project and property type
* Collect budget and buying timeline
* Classify leads

### Phase 4: Google Sheets Integration

* Store WhatsApp leads
* Prevent duplicate records
* Synchronize with the LMAR Master Sheet

### Phase 5: LASOS CRM Integration

* Create CRM client records
* Assign sales agents
* Create follow-up tasks
* Store conversation summaries

### Phase 6: Testing and Deployment

* Webhook testing
* Message-flow testing
* Security testing
* Production deployment
* Staff training

## Future AI Assistant

The future AI Assistant will:

* Summarize customer conversations
* Recommend the next best action
* Suggest suitable properties
* Draft follow-up messages
* Identify overdue leads
* Generate sales and lead reports

All important AI actions will require human confirmation.

## Developed By

**Nasrat Abid**
Data Analyst and Meta Ads Specialist
LMAR Marketing Real Estate Company
Deep Data Lab — AI and Automation

