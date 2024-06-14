from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.adapter_host_fc_interface.info import AdapterHostFcInterfaceInfo

class AdapterHostFcInterface(IntersightCommon, AdapterHostFcInterfaceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'adapter hostfcinterface'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        AdapterHostFcInterfaceInfo.__init__(self)
