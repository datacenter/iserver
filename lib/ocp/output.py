from lib import output_helper

from lib.ocp.cluster.output import OcpClusterOutput
from lib.ocp.task.output import OcpTaskOutput
from lib.ocp.vm.output import OcpVmOutput


class OcpOutput(
        OcpClusterOutput,
        OcpTaskOutput,
        OcpVmOutput
        ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        OcpClusterOutput.__init__(self)
        OcpTaskOutput.__init__(self)
        OcpVmOutput.__init__(self)
