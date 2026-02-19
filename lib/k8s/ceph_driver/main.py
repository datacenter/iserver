from lib.k8s.ceph_driver.api import K8sCephDriverApi
from lib.k8s.ceph_driver.info import K8sCephDriverInfo


class K8sCephDriver(
        K8sCephDriverApi,
        K8sCephDriverInfo
        ):
    def __init__(self):
        K8sCephDriverApi.__init__(self)
        K8sCephDriverInfo.__init__(self)
