from lib.k8s.user.api import K8sUserApi
from lib.k8s.user.info import K8sUserInfo


class K8sUser(
        K8sUserApi,
        K8sUserInfo
        ):
    def __init__(self):
        K8sUserApi.__init__(self)
        K8sUserInfo.__init__(self)
