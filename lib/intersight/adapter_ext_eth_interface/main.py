from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.adapter_ext_eth_interface.info import AdapterExtEthInterfaceInfo

class AdapterExtEthInterface(IntersightCommon, AdapterExtEthInterfaceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'adapter extethinterface'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        AdapterExtEthInterfaceInfo.__init__(self)
