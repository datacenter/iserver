from lib.nso.cnfm.cnfd.output import NsoCnfmCnfdOutput
from lib.nso.cnfm.cnfi.output import NsoCnfmCnfiOutput
from lib.nso.cnfm.device.output import NsoCnfmDeviceOutput


class NsoCnfmOutput(
        NsoCnfmCnfdOutput,
        NsoCnfmCnfiOutput,
        NsoCnfmDeviceOutput
        ):
    def __init__(self):
        NsoCnfmCnfdOutput.__init__(self)
        NsoCnfmCnfiOutput.__init__(self)
        NsoCnfmDeviceOutput.__init__(self)
