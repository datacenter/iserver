from lib.nso.nfvo.vnfi.create import NfvoVnfiCreate
from lib.nso.nfvo.vnfi.delete import NfvoVnfiDelete
from lib.nso.nfvo.vnfi.get import NfvoVnfiGet
from lib.nso.nfvo.vnfi.output import NfvoVnfiOutput


class NfvoVnfi(NfvoVnfiCreate, NfvoVnfiDelete, NfvoVnfiGet, NfvoVnfiOutput):
    def __init__(self):
        NfvoVnfiCreate.__init__(self)
        NfvoVnfiDelete.__init__(self)
        NfvoVnfiGet.__init__(self)
        NfvoVnfiOutput.__init__(self)
