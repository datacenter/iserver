from lib.k8s.splunk_standalone.api import K8sSplunkStandaloneApi
from lib.k8s.splunk_standalone.info import K8sSplunkStandaloneInfo


class K8sSplunkStandalone(
        K8sSplunkStandaloneApi,
        K8sSplunkStandaloneInfo,
        ):
    def __init__(self):
        K8sSplunkStandaloneApi.__init__(self)
        K8sSplunkStandaloneInfo.__init__(self)

