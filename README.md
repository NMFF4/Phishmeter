# PhishMeter

PhishMeter is a simple web app that analyzes email text and scores its phishing risk. It detects suspicious keywords, urgent language, links, and excessive ALL CAPS words.

## Live Demo

Check it out live: [https://phishmeter.onrender.com](https://phishmeter.onrender.com)

## Features

- Detects mentions of passwords (credential theft)
- Flags verification requests
- Identifies urgent language
- Detects suspicious links
- Highlights excessive ALL CAPS words
- Shows a risk score, level, and visual meter

## How to Use

1. Open the live demo link or run locally.
2. Paste the email text into the textarea.
3. Click **Scan Email** to see the results.

## Email Example

Subject: URGENT: Account Verification Required

Dear User,

We detected unusual activity on your account. To avoid being locked out, please VERIFY your password immediately by clicking the link below:

http://fakebank-login.com

FAILURE TO ACT WITHIN 24 HOURS WILL RESULT IN ACCOUNT SUSPENSION.

THANK YOU,
The Security Team


## Installation (for local testing)

```bash
git clone https://github.com/YOUR_USERNAME/phishmeter.git
cd phishmeter
python -m pip install -r requirements.txt
python app.py
