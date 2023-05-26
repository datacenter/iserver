from lib import log_helper
from lib import output_helper

from lib.ocp.state.kc.info import OcpKubeconfigInfo
from lib.ocp.state.kc.output import OcpKubeconfigOutput


class OcpKubeconfig(OcpKubeconfigInfo, OcpKubeconfigOutput):
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        OcpKubeconfigInfo.__init__(self)
        OcpKubeconfigOutput.__init__(self)
