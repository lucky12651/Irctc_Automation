# IRCTC booking helper

Python helper that fills the public IRCTC booking forms in Chrome. You still solve captcha and complete payment in the browser.

This project uses the **Page Object Model**: locators and page actions live in `irctc/pages/`, the booking steps live in `irctc/flows/`, and `main.py` is the only entry point you run.

## Project structure

```text
Irctc_Automation/
├── main.py                 # run this
├── .env.example            # copy to .env and fill in
├── irctc/
│   ├── config.py           # settings from environment
│   ├── driver.py           # Chrome WebDriver setup
│   ├── flows/
│   │   └── booking_flow.py # login → search → passenger → payment
│   └── pages/
│       ├── base_page.py    # shared waits and clicks
│       ├── login_page.py
│       ├── search_page.py
│       ├── train_list_page.py
│       └── passenger_page.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.8+
- Google Chrome

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your values:

```powershell
copy .env.example .env
```

```env
IRCTC_USERNAME=your_username
IRCTC_PASSWORD=your_password
IRCTC_FROM_STATION=GHAZIABAD - GZB
IRCTC_TO_STATION=LUCKNOW NR - LKO
IRCTC_JOURNEY_DATE=04/05/2026
```

## Run

```bash
python main.py
```

The script opens IRCTC, fills login fields, then pauses. Solve captcha and sign in, press Enter in the terminal, and it continues through search and passenger details. It pauses again if captcha appears before payment.

## Important note

Use this only on your own IRCTC account and follow IRCTC's terms. Automated access can violate those terms. This project is a personal form-filling helper, not a captcha bypass.
