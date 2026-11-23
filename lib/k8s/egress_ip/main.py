from lib.k8s.egress_ip.api import K8sEgressIpApi
from lib.k8s.egress_ip.info import K8sEgressIpInfo


class K8sEgressIp(
        K8sEgressIpApi,
        K8sEgressIpInfo
        ):
    def __init__(self):
        K8sEgressIpApi.__init__(self)
        K8sEgressIpInfo.__init__(self)
