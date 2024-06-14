from lib.nso.cnfm.device.api import NsoCnfmDeviceApi
from lib.nso.cnfm.device.info import NsoCnfmDeviceInfo


class NsoCnfmDevice(
        NsoCnfmDeviceApi,
        NsoCnfmDeviceInfo
        ):
    def __init__(self):
        NsoCnfmDeviceApi.__init__(self)
        NsoCnfmDeviceInfo.__init__(self)
