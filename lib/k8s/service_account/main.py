from lib.k8s.service_account.api import K8sServiceAccountApi
from lib.k8s.service_account.info import K8sServiceAccountInfo


class K8sServiceAccount(
        K8sServiceAccountApi,
        K8sServiceAccountInfo
        ):
    def __init__(self):
        K8sServiceAccountApi.__init__(self)
        K8sServiceAccountInfo.__init__(self)
