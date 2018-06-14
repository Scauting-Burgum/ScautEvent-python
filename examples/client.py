from ScautEvent.client import EventClient
from ScautEvent.common import Event

client = EventClient("localhost", 5000)

client.listeners["message"] = print

client.start()

while True:
  message = input()
  event = Event("message", message)
  client.push(event)
