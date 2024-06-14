from lib.nso.device.api import NsoDeviceApi
from lib.nso.device.info import NsoDeviceInfo


class NsoDevice(
        NsoDeviceApi,
        NsoDeviceInfo
        ):
    def __init__(self):
        NsoDeviceApi.__init__(self)
        NsoDeviceInfo.__init__(self)
