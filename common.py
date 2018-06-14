from .ScautNet import ConversionFilter
import json

class Event:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def event_from_json(_json):
    return Event(**json.loads(_json))

def event_to_json(event):
    return json.dumps({"name":event.name, "value":event.value})

class EventFilter(ConversionFilter):
    def __init__(self):
        super().__init__(event_from_json, event_to_json)
