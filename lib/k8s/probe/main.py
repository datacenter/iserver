from lib.k8s.probe.api import K8sProbeApi
from lib.k8s.probe.info import K8sProbeInfo


class K8sProbe(
        K8sProbeApi,
        K8sProbeInfo
        ):
    def __init__(self):
        K8sProbeApi.__init__(self)
        K8sProbeInfo.__init__(self)
