from lib.k8s.sriov_operator_config.api import K8sSriovOperatorConfigApi
from lib.k8s.sriov_operator_config.info import K8sSriovOperatorConfigInfo


class K8sSriovOperatorConfig(
        K8sSriovOperatorConfigApi,
        K8sSriovOperatorConfigInfo
        ):
    def __init__(self):
        K8sSriovOperatorConfigApi.__init__(self)
        K8sSriovOperatorConfigInfo.__init__(self)
