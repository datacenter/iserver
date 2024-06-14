from lib.nso.nfvo.vnfd.create import NfvoVnfdCreate
from lib.nso.nfvo.vnfd.delete import NfvoVnfdDelete
from lib.nso.nfvo.vnfd.get import NfvoVnfdGet
from lib.nso.nfvo.vnfd.output import NfvoVnfdOutput


class NfvoVnfd(NfvoVnfdCreate, NfvoVnfdDelete, NfvoVnfdGet, NfvoVnfdOutput):
    def __init__(self):
        NfvoVnfdCreate.__init__(self)
        NfvoVnfdDelete.__init__(self)
        NfvoVnfdGet.__init__(self)
        NfvoVnfdOutput.__init__(self)
