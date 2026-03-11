from lib.k8s.user.api import K8sUserApi
from lib.k8s.user.info import K8sUserInfo
from lib.k8s.user.delete import K8sUserDelete
from lib.k8s.user.match import K8sUserMatch
from lib.k8s.user.wait import K8sUserWait


class K8sUser(
        K8sUserApi,
        K8sUserInfo,
        K8sUserDelete,
        K8sUserMatch,
        K8sUserWait
        ):
    def __init__(self):
        K8sUserApi.__init__(self)
        K8sUserInfo.__init__(self)
        K8sUserDelete.__init__(self)
        K8sUserMatch.__init__(self)
        K8sUserWait.__init__(self)
