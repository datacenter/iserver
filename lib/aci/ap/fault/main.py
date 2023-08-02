from lib.aci.ap.fault.api import ApplicationProfileFaultApi
from lib.aci.ap.fault.info import ApplicationProfileFaultInfo


class ApplicationProfileFault(ApplicationProfileFaultApi, ApplicationProfileFaultInfo):
    def __init__(self):
        ApplicationProfileFaultApi.__init__(self)
        ApplicationProfileFaultInfo.__init__(self)
