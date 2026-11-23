from lib.k8s.nmstate.api import K8sNmstateApi
from lib.k8s.nmstate.info import K8sNmstateInfo


class K8sNmstate(
        K8sNmstateApi,
        K8sNmstateInfo
        ):
    def __init__(self):
        K8sNmstateApi.__init__(self)
        K8sNmstateInfo.__init__(self)
