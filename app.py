from flask import Flask, render_template
import requests
from ics import Calendar
from datetime import datetime, timezone

app = Flask(__name__)


ICS_URL = "https://calendar.google.com/calendar/ical/mcichos45%40gmail.com/public/basic.ics"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/events")
def events():
    try:
        response = requests.get(ICS_URL)
        if response.status_code != 200:
            return render_template("events.html", events=[], error="Nie udało się pobrać kalendarza.")

        calendar = Calendar(response.text)
        future_events = sorted(
            (event for event in calendar.events if event.begin.datetime >= datetime.now(timezone.utc)),
            key=lambda e: e.begin
        )

        return render_template("events.html", events=future_events[:10], error=None)

    except Exception as e:
        return render_template("events.html", events=[], error=str(e))
    
    
if __name__ == "__main__":
    app.run(debug=True)
