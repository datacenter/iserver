from lib import log_helper

from lib.psirt.api import PsirtApi
from lib.psirt.cache import PsirtCache
from lib.psirt.common import PsirtCommon

from lib.psirt.advisory.main import PsirtAdvisory


class Psirt(
        PsirtApi,
        PsirtCache,
        PsirtCommon,
        PsirtAdvisory
        ):
    def __init__(self, key, secret, verbose=False, debug=False, log_id=None):
        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        PsirtApi.__init__(self, key, secret)
        PsirtCache.__init__(self)
        PsirtCommon.__init__(self)
        PsirtAdvisory.__init__(self)
