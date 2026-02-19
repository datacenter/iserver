from lib.k8s.cdi_config.api import K8sCdiConfigApi
from lib.k8s.cdi_config.info import K8sCdiConfigInfo


class K8sCdiConfig(
        K8sCdiConfigApi,
        K8sCdiConfigInfo
        ):
    def __init__(self):
        K8sCdiConfigApi.__init__(self)
        K8sCdiConfigInfo.__init__(self)
