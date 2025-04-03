from flask import Flask, redirect, url_for, session
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
CREDENTIALS_FILE = "credentials.json"

@app.route("/")
def home():
    return '<a href="/authorize">Zaloguj sie do Google Calendar</a>'

@app.route("/authorize")
def authorize():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    credentials = flow.run_local_server(port=5001)
    session["credentials"] = credentials.to_json()
    return redirect(url_for("events"))



if __name__ == "__main__":
    app.run(debug=True, port=5002)