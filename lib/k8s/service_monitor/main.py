from lib.k8s.service_monitor.api import K8sServiceMonitorApi
from lib.k8s.service_monitor.info import K8sServiceMonitorInfo
from lib.k8s.service_monitor.create import K8sServiceMonitorCreate
from lib.k8s.service_monitor.delete import K8sServiceMonitorDelete
from lib.k8s.service_monitor.wait import K8sServiceMonitorWait


class K8sServiceMonitor(
        K8sServiceMonitorApi,
        K8sServiceMonitorInfo,
        K8sServiceMonitorCreate,
        K8sServiceMonitorDelete,
        K8sServiceMonitorWait
        ):
    def __init__(self):
        K8sServiceMonitorApi.__init__(self)
        K8sServiceMonitorInfo.__init__(self)
        K8sServiceMonitorCreate.__init__(self)
        K8sServiceMonitorDelete.__init__(self)
        K8sServiceMonitorWait.__init__(self)
