from lib.k8s.service_account.api import K8sServiceAccountApi
from lib.k8s.service_account.info import K8sServiceAccountInfo
from lib.k8s.service_account.create import K8sServiceAccountCreate
from lib.k8s.service_account.delete import K8sServiceAccountDelete
from lib.k8s.service_account.wait import K8sServiceAccountWait


class K8sServiceAccount(
        K8sServiceAccountApi,
        K8sServiceAccountInfo,
        K8sServiceAccountCreate,
        K8sServiceAccountDelete,
        K8sServiceAccountWait
        ):
    def __init__(self):
        K8sServiceAccountApi.__init__(self)
        K8sServiceAccountInfo.__init__(self)
        K8sServiceAccountCreate.__init__(self)
        K8sServiceAccountDelete.__init__(self)
        K8sServiceAccountWait.__init__(self)
