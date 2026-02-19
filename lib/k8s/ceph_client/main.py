from lib.k8s.ceph_client.api import K8sCephClientApi
from lib.k8s.ceph_client.info import K8sCephClientInfo


class K8sCephClient(
        K8sCephClientApi,
        K8sCephClientInfo
        ):
    def __init__(self):
        K8sCephClientApi.__init__(self)
        K8sCephClientInfo.__init__(self)
