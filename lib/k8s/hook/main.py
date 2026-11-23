from lib.k8s.hook.api import K8sHookApi
from lib.k8s.hook.info import K8sHookInfo


class K8sHook(
        K8sHookApi,
        K8sHookInfo,
        ):
    def __init__(self):
        K8sHookApi.__init__(self)
        K8sHookInfo.__init__(self)

