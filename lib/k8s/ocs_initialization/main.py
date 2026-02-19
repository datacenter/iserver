from lib.k8s.ocs_initialization.api import K8sOcsInitializationApi
from lib.k8s.ocs_initialization.info import K8sOcsInitializationInfo


class K8sOcsInitialization(
        K8sOcsInitializationApi,
        K8sOcsInitializationInfo
        ):
    def __init__(self):
        K8sOcsInitializationApi.__init__(self)
        K8sOcsInitializationInfo.__init__(self)
