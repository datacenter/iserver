from lib.nso.nfvo.vnfd.create import VnfdCreate
from lib.nso.nfvo.vnfd.delete import VnfdDelete
from lib.nso.nfvo.vnfd.get import VnfdGet
from lib.nso.nfvo.vnfd.output import VnfdOutput


class Vnfd(VnfdCreate, VnfdDelete, VnfdGet, VnfdOutput):
    def __init__(self):
        VnfdCreate.__init__(self)
        VnfdDelete.__init__(self)
        VnfdGet.__init__(self)
        VnfdOutput.__init__(self)
