from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


def load_events():
    with open('../calendar/data/data.json', 'r') as file:
        events = json.load(file)
    return events


def save_events(events):
    with open('../calendar/data/data.json', 'w') as file:
        json.dump(events, file, indent=4)


@app.route('/calendar')
def calendar():
    events = load_events()
    return render_template('calendar.html', events=events)

@app.route('/get_events')
def get_events():
    events = load_events()
    return jsonify(events)


@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    events = load_events()
    events.append(data)
    save_events(events)
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)
