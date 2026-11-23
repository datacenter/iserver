from lib.k8s.host_path_provisioner.api import K8sHostPathProvisionerApi
from lib.k8s.host_path_provisioner.info import K8sHostPathProvisionerInfo


class K8sHostPathProvisioner(
        K8sHostPathProvisionerApi,
        K8sHostPathProvisionerInfo
        ):
    def __init__(self):
        K8sHostPathProvisionerApi.__init__(self)
        K8sHostPathProvisionerInfo.__init__(self)
