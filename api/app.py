from http.client import BAD_REQUEST, OK
from flask import Flask, abort, request
from flask_cors import CORS

events = {
    # Here is an example event:
    0: {
        "name": "OSAI Social",
        "category": "food",
        "location": "CIF 1038",
        "date": "Oct 6th 2022 7PM",
    },
    1: {
        "name": "OSAI Event",
        "category": "stuff",
        "location": "CIF 1038",
        "date": "Oct 13th 2022 7PM",
    }
}

app = Flask(__name__)
CORS(app)


@ app.get("/")
def get_default():
    return {"message": "why am i here???????"}


@ app.get("/events")
def get_all():
    """
    Returns a map of all events to their event ID
    """
    return events


@ app.get("/events/<event_id>")
def get_event(event_id: int):
    """
    Returns the event object for the given event_id
    """
    event_id = int(event_id)
    # Your code goes here
    return events[event_id]
    # Since this function is not yet implemented, return Status 501
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501
    # abort(501)


@ app.post("/events")
def new():
    """
    Stores a new event object in the database
    """
    # HINT: You can access the object to be created using request.json
    # Your code goes here
    new_event = request.json
    events.update({len(events) + 1 : new_event})
    return "added event no way this is the correct way"
    # abort(501)


@ app.patch("/events/<event_id>")
def update(event_id: int):
    """
    Updates the event object for the given event_id
    """
    event_id = int(event_id)
    # HINT: You can access the object to be updated using request.json
    # Your code goes here
    events[event_id] = request.json
    return "updated event"

@ app.delete("/events/<event_id>")
def delete(event_id: int):  # no error handling
    """
    Deletes the event object for the given event_id
    """
    event_id = int(event_id)
    # Your code goes here
    
    events.pop(event_id)
    return "deleted event"


if __name__ == '__main__':
    app.run()
