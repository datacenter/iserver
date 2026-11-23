from lib.k8s.ceph_cosi_driver.api import K8sCephCosiDriverApi
from lib.k8s.ceph_cosi_driver.info import K8sCephCosiDriverInfo


class K8sCephCosiDriver(
        K8sCephCosiDriverApi,
        K8sCephCosiDriverInfo
        ):
    def __init__(self):
        K8sCephCosiDriverApi.__init__(self)
        K8sCephCosiDriverInfo.__init__(self)
