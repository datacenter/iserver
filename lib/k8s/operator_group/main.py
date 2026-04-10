from lib.k8s.operator_group.api import K8sOperatorGroupApi
from lib.k8s.operator_group.info import K8sOperatorGroupInfo
from lib.k8s.operator_group.create import K8sOperatorGroupCreate
from lib.k8s.operator_group.delete import K8sOperatorGroupDelete
from lib.k8s.operator_group.wait import K8sOperatorGroupWait


class K8sOperatorGroup(
        K8sOperatorGroupApi,
        K8sOperatorGroupInfo,
        K8sOperatorGroupCreate,
        K8sOperatorGroupDelete,
        K8sOperatorGroupWait
        ):
    def __init__(self):
        K8sOperatorGroupApi.__init__(self)
        K8sOperatorGroupInfo.__init__(self)
        K8sOperatorGroupCreate.__init__(self)
        K8sOperatorGroupDelete.__init__(self)
        K8sOperatorGroupWait.__init__(self)
