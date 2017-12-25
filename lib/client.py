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
