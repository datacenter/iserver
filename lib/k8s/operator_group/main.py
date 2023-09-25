from lib.k8s.operator_group.api import K8sOperatorGroupApi
from lib.k8s.operator_group.info import K8sOperatorGroupInfo


class K8sOperatorGroup(
        K8sOperatorGroupApi,
        K8sOperatorGroupInfo
        ):
    def __init__(self):
        K8sOperatorGroupApi.__init__(self)
        K8sOperatorGroupInfo.__init__(self)
