from flask import Flask
import requests
from ics import Calendar
from datetime import datetime, timezone

app = Flask(__name__)


ICS_URL = "https://calendar.google.com/calendar/ical/mcichos45%40gmail.com/public/basic.ics"

@app.route("/")
def home():
    return '<a href="/events">Zobacz wydarzenia z kalendarza</a>'

@app.route("/events")
def events():
    try:
        response = requests.get(ICS_URL)

        if response.status_code != 200:
            return "❌ Nie udało się pobrać kalendarza."

        calendar = Calendar(response.text)

        future_events = sorted(
            (event for event in calendar.events if event.begin.datetime >= datetime.now(timezone.utc)),
            key=lambda e: e.begin
        )

        if not future_events:
            return "Brak nadchodzących wydarzeń."

        html = "<h1>📅 Nadchodzące wydarzenia</h1><ul>"
        for event in future_events[:10]:
            html += f"<li>{event.begin.format('YYYY-MM-DD HH:mm')} - {event.name}</li>"
        html += "</ul>"

        return html

    except Exception as e:
        return f"❌ Wystąpił błąd: {e}"

if __name__ == "__main__":
    app.run(debug=True, port=5002)
