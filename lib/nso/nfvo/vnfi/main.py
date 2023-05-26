from lib.nso.nfvo.vnfi.create import VnfiCreate
from lib.nso.nfvo.vnfi.delete import VnfiDelete
from lib.nso.nfvo.vnfi.get import VnfiGet
from lib.nso.nfvo.vnfi.output import VnfiOutput


class Vnfi(VnfiCreate, VnfiDelete, VnfiGet, VnfiOutput):
    def __init__(self):
        VnfiCreate.__init__(self)
        VnfiDelete.__init__(self)
        VnfiGet.__init__(self)
        VnfiOutput.__init__(self)
