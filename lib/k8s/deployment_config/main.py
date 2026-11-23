from lib.k8s.deployment_config.api import K8sDeploymentConfigApi
from lib.k8s.deployment_config.info import K8sDeploymentConfigInfo


class K8sDeploymentConfig(
        K8sDeploymentConfigApi,
        K8sDeploymentConfigInfo
        ):
    def __init__(self):
        K8sDeploymentConfigApi.__init__(self)
        K8sDeploymentConfigInfo.__init__(self)
