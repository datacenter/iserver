from lib.psirt.advisory.api import PsirtAdvisoryApi
from lib.psirt.advisory.info import PsirtAdvisoryInfo


class PsirtAdvisory(
        PsirtAdvisoryApi,
        PsirtAdvisoryInfo
        ):
    def __init__(self):
        PsirtAdvisoryApi.__init__(self)
        PsirtAdvisoryInfo.__init__(self)
