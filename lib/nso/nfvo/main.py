from lib import log_helper

from lib.nso.nfvo.api.main import NfvoApi
from lib.nso.nfvo.vnfd.main import NfvoVnfd
from lib.nso.nfvo.vnfi.main import NfvoVnfi


class Nfvo(NfvoApi, NfvoVnfd, NfvoVnfi):
    def __init__(
            self,
            rest_handler,
            nfvo_etsi=False,
            nfvo_version='3.x',
            log_id=None
            ):

        self.log = log_helper.Log(log_id=log_id)
        self.rest_handler = rest_handler

        NfvoApi.__init__(
            self,
            nfvo_etsi=nfvo_etsi,
            nfvo_version=nfvo_version
        )
        NfvoVnfd.__init__(self)
        NfvoVnfi.__init__(self)
