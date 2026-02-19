from lib.k8s.secret.api import K8sSecretApi
from lib.k8s.secret.info import K8sSecretInfo
from lib.k8s.secret.create import K8sSecretCreate
from lib.k8s.secret.delete import K8sSecretDelete
from lib.k8s.secret.wait import K8sSecretWait


class K8sSecret(
        K8sSecretApi,
        K8sSecretInfo,
        K8sSecretCreate,
        K8sSecretDelete,
        K8sSecretWait
        ):
    def __init__(self):
        K8sSecretApi.__init__(self)
        K8sSecretInfo.__init__(self)
        K8sSecretCreate.__init__(self)
        K8sSecretDelete.__init__(self)
        K8sSecretWait.__init__(self)
