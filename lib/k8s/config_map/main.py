from lib.k8s.config_map.api import K8sConfigMapApi
from lib.k8s.config_map.info import K8sConfigMapInfo


class K8sConfigMap(
        K8sConfigMapApi,
        K8sConfigMapInfo
        ):
    def __init__(self):
        K8sConfigMapApi.__init__(self)
        K8sConfigMapInfo.__init__(self)
