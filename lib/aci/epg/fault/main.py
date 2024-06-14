from lib.aci.epg.fault.api import EpgFaultApi
from lib.aci.epg.fault.info import EpgFaultInfo


class EpgFault(EpgFaultApi, EpgFaultInfo):
    def __init__(self):
        EpgFaultApi.__init__(self)
        EpgFaultInfo.__init__(self)
