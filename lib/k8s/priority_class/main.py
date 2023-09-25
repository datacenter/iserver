from lib.k8s.priority_class.api import K8sPriorityClassApi
from lib.k8s.priority_class.info import K8sPriorityClassInfo


class K8sPriorityClass(
        K8sPriorityClassApi,
        K8sPriorityClassInfo
        ):
    def __init__(self):
        K8sPriorityClassApi.__init__(self)
        K8sPriorityClassInfo.__init__(self)
