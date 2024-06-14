from lib.openshift.assistedinstall.event.api import AssistedInstallEventApi
from lib.openshift.assistedinstall.event.info import AssistedInstallEventInfo


class AssistedInstallEvent(
        AssistedInstallEventApi,
        AssistedInstallEventInfo
        ):
    def __init__(self):
        AssistedInstallEventApi.__init__(self)
        AssistedInstallEventInfo.__init__(self)
