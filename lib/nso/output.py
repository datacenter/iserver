from lib import output_helper

from lib.nso.cnfm.output import NsoCnfmOutput
from lib.nso.device.output import NsoDeviceOutput
from lib.nso.nfvo.output import NfvoOutput


class NsoOutput(
    NsoCnfmOutput,
    NfvoOutput,
    NsoDeviceOutput,
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        NsoCnfmOutput.__init__(self)
        NfvoOutput.__init__(self)
        NsoDeviceOutput.__init__(self)
