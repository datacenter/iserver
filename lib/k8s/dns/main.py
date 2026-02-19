from lib.k8s.dns.api import K8sDnsApi
from lib.k8s.dns.info import K8sDnsInfo


class K8sDns(
        K8sDnsApi,
        K8sDnsInfo
        ):
    def __init__(self):
        K8sDnsApi.__init__(self)
        K8sDnsInfo.__init__(self)
