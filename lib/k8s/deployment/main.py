from lib.k8s.deployment.api import K8sDeploymentApi
from lib.k8s.deployment.info import K8sDeploymentInfo
from lib.k8s.deployment.create import K8sDeploymentCreate
from lib.k8s.deployment.delete import K8sDeploymentDelete
from lib.k8s.deployment.oauth import K8sDeploymentOauth
from lib.k8s.deployment.update import K8sDeploymentUpdate
from lib.k8s.deployment.wait import K8sDeploymentWait


class K8sDeployment(
        K8sDeploymentApi,
        K8sDeploymentInfo,
        K8sDeploymentCreate,
        K8sDeploymentDelete,
        K8sDeploymentOauth,
        K8sDeploymentUpdate,
        K8sDeploymentWait
        ):
    def __init__(self):
        K8sDeploymentApi.__init__(self)
        K8sDeploymentInfo.__init__(self)
        K8sDeploymentCreate.__init__(self)
        K8sDeploymentDelete.__init__(self)
        K8sDeploymentOauth.__init__(self)
        K8sDeploymentUpdate.__init__(self)
        K8sDeploymentWait.__init__(self)

