from lib import output_helper

from lib.nso.nfvo.vnfd.output import NfvoVnfdOutput
from lib.nso.nfvo.vnfi.output import NfvoVnfiOutput


class NfvoOutput(
    NfvoVnfdOutput,
    NfvoVnfiOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        NfvoVnfdOutput.__init__(self)
        NfvoVnfiOutput.__init__(self)
