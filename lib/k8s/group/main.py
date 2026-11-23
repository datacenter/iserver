from lib.k8s.group.api import K8sGroupApi
from lib.k8s.group.info import K8sGroupInfo
from lib.k8s.group.delete import K8sGroupDelete
from lib.k8s.group.match import K8sGroupMatch
from lib.k8s.group.wait import K8sGroupWait


class K8sGroup(
        K8sGroupApi,
        K8sGroupInfo,
        K8sGroupDelete,
        K8sGroupMatch,
        K8sGroupWait
        ):
    def __init__(self):
        K8sGroupApi.__init__(self)
        K8sGroupInfo.__init__(self)
        K8sGroupDelete.__init__(self)
        K8sGroupMatch.__init__(self)
        K8sGroupWait.__init__(self)
