from lib import log_helper
from lib import output_helper

from lib.nso.api import main as nso_api
from lib.nso.nfvo.main import Nfvo


class Nso(Nfvo):
    def __init__(self, protocol, ip_address, port, username=None, password=None, restconf_enabled=True, nfvo_version='4.x', nfvo_etsi=False, log_id=None, verbose=False, debug=False):
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        self.nfvo_version = nfvo_version
        self.nfvo_etsi = nfvo_etsi
        self.restconf_enabled = restconf_enabled

        self.api_handler = nso_api.Api(
            protocol=protocol,
            ip_address=ip_address,
            port=port,
            username=username,
            password=password,
            restconf_enabled=restconf_enabled,
            nfvo_version=nfvo_version,
            log_id=log_id
        )

        Nfvo.__init__(self)

    def is_connected(self):
        return self.api_handler.is_rest_api()
