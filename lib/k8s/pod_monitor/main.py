from lib.k8s.pod_monitor.api import K8sPodMonitorApi
from lib.k8s.pod_monitor.info import K8sPodMonitorInfo


class K8sPodMonitor(
        K8sPodMonitorApi,
        K8sPodMonitorInfo
        ):
    def __init__(self):
        K8sPodMonitorApi.__init__(self)
        K8sPodMonitorInfo.__init__(self)
