from lib.k8s.ceph_operator_config.api import K8sCephOperatorConfigApi
from lib.k8s.ceph_operator_config.info import K8sCephOperatorConfigInfo


class K8sCephOperatorConfig(
        K8sCephOperatorConfigApi,
        K8sCephOperatorConfigInfo
        ):
    def __init__(self):
        K8sCephOperatorConfigApi.__init__(self)
        K8sCephOperatorConfigInfo.__init__(self)
