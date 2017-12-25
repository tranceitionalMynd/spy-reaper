import sys

from ibapi.wrapper import EWrapper
from ibapi.client import EClient

class Wrapper(EWrapper):
    pass

class Client(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

class App(Wrapper, Client):
    def __init__(self):
        Wrapper.__init__(self)
        Client.__init__(self, wrapper=self)
        self.started = False

    def connectAck(self):
        if self.async:
            self.startApi()

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)

        self.nextValidOrderId = orderId
        self.start()

    def start(self):
        if self.started:
            return

        self.started = True
        sys.stderr.write("Client is connected. Executing requests.\n")
        self.reqGlobalCancel()
