from lib import log_helper
from lib import output_helper

from lib.ocp.lcm.common import OcpCommon
from lib.ocp.lcm.create import OcpCreate
from lib.ocp.lcm.delete import OcpDelete
from lib.ocp.lcm.validate import OcpValidate
from lib.ocp.lcm.vsphere.main import OcpVsphere
from lib.ocp import settings as ocp_settings


class Ocp(OcpCommon, OcpCreate, OcpDelete, OcpValidate, OcpVsphere):
    def __init__(self, verbose=False, debug=False, log_id=None):
        OcpCommon.__init__(self)
        OcpCreate.__init__(self)
        OcpDelete.__init__(self)
        OcpValidate.__init__(self)
        OcpVsphere.__init__(self)

        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id

        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)
        self.ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
