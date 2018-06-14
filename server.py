from .ScautNet import Server
from .common import get_pipeline
from threading import Thread

class EventServerHandler(Thread):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def run(self):
        while self.server.alive:
            with self.server.pipelines_lock:
                for pipeline in self.server.pipelines:
                    try:
                        event = pipeline.pull(timeout=0.2)
                    except Empty:
                        pass
                    else:
                        for pipeline_ in self.server.pipelines:
                            pipeline_.push(event)

class EventServer(Server):
    def __init__(self, hostname, port):
        super().__init__(hostname, port)
        self.handler = EventServerHandler(self)
    
    def get_pipeline(self, socket):
        return get_pipeline(socket)

    def start(self):
        super().start()
        self.handler.start()
