from collections import deque
from typing import Deque, List

from flask import Flask, request


class Event:
    def __init__(self):
        self._peeked_events: Deque = deque()
        self._events: List = []

    def store(self, event: str) -> List:
        events = [event]
        self._peeked_events.extend(events)
        self._events.append(event)
        print(f"Length: {len(self._peeked_events)}")
        print(f"Length: {len(self._events)}")
        return events


app = Flask(__name__)
events = Event()


@app.route("/", methods=("GET",))
def main_route() -> dict:
    event_key = request.args.get("event", "")
    return {"events": events.store(event_key)}
