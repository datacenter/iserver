from lib import log_helper

from lib.nso.cnfm.main import NsoCnfm
from lib.nso.common import NsoCommon
from lib.nso.device.main import NsoDevice
from lib.nso.api import rest
from lib.nso.nfvo import main as nfvo_library


class Nso(NsoCnfm, NsoCommon, NsoDevice):
    def __init__(
            self,
            protocol,
            ip_address,
            port,
            username=None,
            password=None,
            restconf_enabled=True,
            nfvo=None,
            log_id=None
            ):

        self.log = log_helper.Log(log_id=log_id)

        self.rest_handler = rest.Rest(
            protocol,
            ip_address,
            port,
            username,
            password,
            restconf_enabled=restconf_enabled,
            log_id=log_id
        )

        NsoCnfm.__init__(self)
        NsoCommon.__init__(self)
        NsoDevice.__init__(self)

        self.nfvo_handler = None
        if nfvo is not None:
            if 'etsi:' in nfvo:
                nfvo_etsi = True
                nfvo_version = nfvo.split(':')[1]
            else:
                nfvo_etsi = False
                nfvo_version = nfvo

            self.nfvo_handler = nfvo_library.Nfvo(
                self.rest_handler,
                nfvo_etsi=nfvo_etsi,
                nfvo_version=nfvo_version,
                log_id=log_id
            )

    def is_connected(self):
        success, content = self.rest_handler.get_rest(
            'json',
            None,
            'Accept',
            'application/yang-data',
            'data',
            'depth=1'
        )
        return success
