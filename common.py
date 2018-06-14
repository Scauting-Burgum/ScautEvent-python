from .ScautNet import ConversionFilter, Connection, TextFilter, Pipeline
import json

class Event:
    def __init__(self, name, data):
        self.name = name
        self.data = data

def event_from_json(_json):
    return Event(**json.loads(_json))

def event_to_json(event):
    return json.dumps({"name":event.name, "data":event.data})

class EventFilter(ConversionFilter):
    def __init__(self):
        super().__init__(event_from_json, event_to_json)

def get_pipeline(socket):
    connection = Connection(socket)
    text_filter = TextFilter()
    event_filter = EventFilter()
    return Pipeline(connection, text_filter, event_filter)
