from lib.k8s.infrastructure_config.api import K8sInfrastructureConfigApi
from lib.k8s.infrastructure_config.info import K8sInfrastructureConfigInfo


class K8sInfrastructureConfig(
        K8sInfrastructureConfigApi,
        K8sInfrastructureConfigInfo
        ):
    def __init__(self):
        K8sInfrastructureConfigApi.__init__(self)
        K8sInfrastructureConfigInfo.__init__(self)
