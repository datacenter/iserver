from lib.aci.ap.event.api import ApplicationProfileEventApi
from lib.aci.ap.event.info import ApplicationProfileEventInfo


class ApplicationProfileEvent(ApplicationProfileEventApi, ApplicationProfileEventInfo):
    def __init__(self):
        ApplicationProfileEventApi.__init__(self)
        ApplicationProfileEventInfo.__init__(self)
