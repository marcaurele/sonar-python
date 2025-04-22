from collections import deque
from typing import Deque, List

from flask import Flask, request

class Event:
    def __init__(self):
        self._peeked_events: Deque = deque()

    def store(self, event:str) -> List:
        events = [event]
        self._peeked_events.extend(events)
        print(f"Length: {len(self._peeked_events)}")
        return events


app = Flask(__name__)
events = Event()

@app.route("/")
def main_route() -> dict:
    event_key = request.args.get("event", "")
    return {"events": events.store(event_key)}
