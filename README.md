# ScautEvent
A library for triggering remote events over the network in Python.
# Example
In this example you'll be making a chat app.

To get started, make a folder, this folder will contain all you project's code.
Once you've done this, download the newest release from the [releases page],  
then open the zip-file, and move the folder called "ScautEvent" into your project folder.
## Server
Create a file called "server.py".

First, you'll have to import the `EventServer`-class;
```python
from ScautEvent.server import EventServer
```

After this, create a server;
```python
server = EventServer("localhost", 5000)
```

Then start the server;
```python
server.start()
```
## Client
Create a file called "client.py".

Now import the `EventClient`-class and the `Event`-class;
```python
from ScautEvent.client import EventClient
from ScautEvent.common import Event
```

Then create a client;
```python
client = EventClient("localhost", 5000)
```

Then bind the `print`-method to the `message`-event;
```python
client.listeners["message"] = print
```

After this, start the client;
```python
client.start()
```

Now you'll just have to create a while-loop to send messages;
```python
while True:
  message = input()
  event = Event("message", message)
  client.push(event)
```

And that's it!  
Just run `server.py`, then start multiple clients, and you have a fully functioning chat app.

[releases page]: https://github.com/Scauting-Burgum/ScautEvent-python/releases
