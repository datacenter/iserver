from lib.k8s.event.api import K8sEventApi
from lib.k8s.event.info import K8sEventInfo


class K8sEvent(
        K8sEventApi,
        K8sEventInfo
        ):
    def __init__(self):
        K8sEventApi.__init__(self)
        K8sEventInfo.__init__(self)
