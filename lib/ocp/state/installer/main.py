from lib import log_helper
from lib import output_helper

from lib.ocp.state.installer.info import OcpInstallerInfo
from lib.ocp.state.installer.output import OcpInstallerOutput


class OcpInstaller(OcpInstallerInfo, OcpInstallerOutput):
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        OcpInstallerInfo.__init__(self)
        OcpInstallerOutput.__init__(self)
