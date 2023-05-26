from lib.aci.ap.api import ApplicationProfileApi
from lib.aci.ap.info import ApplicationProfileInfo


class ApplicationProfile(ApplicationProfileApi, ApplicationProfileInfo):
    def __init__(self):
        ApplicationProfileApi.__init__(self)
        ApplicationProfileInfo.__init__(self)
