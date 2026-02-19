from lib.k8s.ssp.api import K8sSspApi
from lib.k8s.ssp.info import K8sSspInfo


class K8sSsp(
        K8sSspApi,
        K8sSspInfo
        ):
    def __init__(self):
        K8sSspApi.__init__(self)
        K8sSspInfo.__init__(self)
