from lib.k8s.secret.api import K8sSecretApi
from lib.k8s.secret.info import K8sSecretInfo


class K8sSecret(
        K8sSecretApi,
        K8sSecretInfo
        ):
    def __init__(self):
        K8sSecretApi.__init__(self)
        K8sSecretInfo.__init__(self)
