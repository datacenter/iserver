from lib import output_helper
from lib import log_helper
from lib.cnc.api import Api
from lib.cnc.cache import Cache
from lib.cnc import settings

from lib.cnc.node.main import Node


class Cnc(
        Api,
        Cache,
        Node
        ):
    def __init__(self, cnc_ip, cnc_port, username, password, cnc_name=None, verbose=False, debug=False, log_id=None, requested_ttl=-1):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)
        self.cnc_settings = None
        self.cnc_name = cnc_name

        if cnc_name is not None:
            settings_handler = settings.CncSettings()
            self.cnc_settings = settings_handler.get_cnc_controller(
                cnc_name
            )

        Api.__init__(
            self,
            cnc_ip,
            cnc_port,
            username,
            password
        )
        Cache.__init__(self, self.cnc_name, requested_ttl=requested_ttl)
        Node.__init__(self)
