from lib.k8s.service_monitor.api import K8sServiceMonitorApi
from lib.k8s.service_monitor.info import K8sServiceMonitorInfo


class K8sServiceMonitor(
        K8sServiceMonitorApi,
        K8sServiceMonitorInfo
        ):
    def __init__(self):
        K8sServiceMonitorApi.__init__(self)
        K8sServiceMonitorInfo.__init__(self)
