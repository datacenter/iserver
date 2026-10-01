from lib.k8s.splunk_standalone.api import K8sSplunkStandaloneApi
from lib.k8s.splunk_standalone.info import K8sSplunkStandaloneInfo
from lib.k8s.splunk_standalone.create import K8sSplunkStandaloneCreate
from lib.k8s.splunk_standalone.delete import K8sSplunkStandaloneDelete
from lib.k8s.splunk_standalone.wait import K8sSplunkStandaloneWait


class K8sSplunkStandalone(
        K8sSplunkStandaloneApi,
        K8sSplunkStandaloneInfo,
        K8sSplunkStandaloneCreate,
        K8sSplunkStandaloneDelete,
        K8sSplunkStandaloneWait
        ):
    def __init__(self):
        K8sSplunkStandaloneApi.__init__(self)
        K8sSplunkStandaloneInfo.__init__(self)
        K8sSplunkStandaloneCreate.__init__(self)
        K8sSplunkStandaloneDelete.__init__(self)
        K8sSplunkStandaloneWait.__init__(self)