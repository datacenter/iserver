from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.adapter_host_eth_interface.info import AdapterHostEthInterfaceInfo

class AdapterHostEthInterface(IntersightCommon, AdapterHostEthInterfaceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'adapter hostethinterface'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        AdapterHostEthInterfaceInfo.__init__(self)
