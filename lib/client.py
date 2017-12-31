import sys

from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.utils import iswrapper

class Wrapper(EWrapper):
    pass

class Client(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

class ClientApp(Wrapper, Client):
    def __init__(self):
        Wrapper.__init__(self)
        Client.__init__(self, wrapper=self)
        self.started = False

    @iswrapper
    def connectAck(self):
        if self.async:
            self.startApi()

    @iswrapper
    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)

        self.nextValidOrderId = orderId
        self.start()

    @iswrapper
    def start(self):
        if self.started:
            return

        self.started = True
        sys.stderr.write("Client is connected. Executing requests.\n")
        self.reqGlobalCancel()

    @iswrapper
    def keyboardInterrupt(self):
        self.done = True

