from lib.nexus.hardware.api import HardwareApi
from lib.nexus.hardware.info import HardwareInfo


class Hardware(
        HardwareApi,
        HardwareInfo
        ):
    def __init__(self):
        HardwareApi.__init__(self)
        HardwareInfo.__init__(self)
