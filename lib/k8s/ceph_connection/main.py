from lib.k8s.ceph_connection.api import K8sCephConnectionApi
from lib.k8s.ceph_connection.info import K8sCephConnectionInfo


class K8sCephConnection(
        K8sCephConnectionApi,
        K8sCephConnectionInfo
        ):
    def __init__(self):
        K8sCephConnectionApi.__init__(self)
        K8sCephConnectionInfo.__init__(self)
