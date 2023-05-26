from lib import log_helper
from lib import output_helper

from lib.ocp.state.vcenter.info import OcpVcenterInfo
from lib.ocp.state.vcenter.output import OcpVcenterOutput


class OcpVcenter(OcpVcenterInfo, OcpVcenterOutput):
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        OcpVcenterInfo.__init__(self)
        OcpVcenterOutput.__init__(self)
