from lib.nso.nfvo.vnfd.main import Vnfd
from lib.nso.nfvo.vnfi.main import Vnfi


class Nfvo(Vnfd, Vnfi):
    def __init__(self):
        Vnfd.__init__(self)
        Vnfi.__init__(self)
