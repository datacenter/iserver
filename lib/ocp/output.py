from lib import output_helper

from lib.ocp.cluster.output import OcpClusterOutput
from lib.ocp.node.output import OcpNodeOutput
from lib.ocp.vm.output import OcpVmOutput


class OcpOutput(OcpClusterOutput, OcpNodeOutput, OcpVmOutput):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        OcpClusterOutput.__init__(self)
        OcpNodeOutput.__init__(self)
        OcpVmOutput.__init__(self)
