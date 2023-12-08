from lib import output_helper

from lib.nexus.lacp.output import LacpOutput
from lib.nexus.lldp.output import LldpOutput
from lib.nexus.mac.output import MacOutput
from lib.nexus.version.output import VersionOutput


class NexusOutput(
    LacpOutput,
    LldpOutput,
    MacOutput,
    VersionOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        LacpOutput.__init__(self)
        LldpOutput.__init__(self)
        MacOutput.__init__(self)
        VersionOutput.__init__(self)
