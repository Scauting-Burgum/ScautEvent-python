from threading import Thread, Lock
from queue import Empty
from .ScautNet import Client
from .common import get_pipeline

class EventClientHandler(Thread):
    def __init__(self, client):
        super().__init__()
        self.client = client

    def run(self):
        while self.client.alive:
            try:
                event = self.client.pull(timeout=0.2)
            except Empty:
                pass
            else:
                with self.client.listener_lock:
                    if event.name in self.client.listeners:
                        self.client.listeners[event.name](event.data)

class EventClient(Client):
    def __init__(self, hostname, port):
        super().__init__(hostname, port)
        self.listener_lock = Lock()
        self.listeners = dict()
        self.handler = EventClientHandler(self)

    def get_pipeline(self):
        return get_pipeline(self.socket)

    def start(self):
        super().start()
        self.handler.start()
