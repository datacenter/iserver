from lib import log_helper
from lib import output_helper
from lib.iwo.lcm.ocp.main import IwoOcpLcm


class IwoLcm(IwoOcpLcm):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id

        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        IwoOcpLcm.__init__(self)
