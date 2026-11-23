from lib.k8s.stateful_set.api import K8sStatefulSetApi
from lib.k8s.stateful_set.info import K8sStatefulSetInfo


class K8sStatefulSet(
        K8sStatefulSetApi,
        K8sStatefulSetInfo
        ):
    def __init__(self):
        K8sStatefulSetApi.__init__(self)
        K8sStatefulSetInfo.__init__(self)
