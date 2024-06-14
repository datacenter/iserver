from lib.k8s.deployment.api import K8sDeploymentApi
from lib.k8s.deployment.info import K8sDeploymentInfo


class K8sDeployment(
        K8sDeploymentApi,
        K8sDeploymentInfo
        ):
    def __init__(self):
        K8sDeploymentApi.__init__(self)
        K8sDeploymentInfo.__init__(self)
