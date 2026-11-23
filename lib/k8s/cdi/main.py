from lib.k8s.cdi.api import K8sCdiApi
from lib.k8s.cdi.info import K8sCdiInfo


class K8sCdi(
        K8sCdiApi,
        K8sCdiInfo
        ):
    def __init__(self):
        K8sCdiApi.__init__(self)
        K8sCdiInfo.__init__(self)
