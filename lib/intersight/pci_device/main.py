from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.pci_device.info import PciDeviceInfo


class PciDevice(IntersightCommon, PciDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'pci device'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        PciDeviceInfo.__init__(self)
