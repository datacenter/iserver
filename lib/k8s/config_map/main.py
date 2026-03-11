from lib.k8s.config_map.api import K8sConfigMapApi
from lib.k8s.config_map.info import K8sConfigMapInfo
from lib.k8s.config_map.create import K8sConfigMapCreate
from lib.k8s.config_map.delete import K8sConfigMapDelete
from lib.k8s.config_map.match import K8sConfigMapMatch
from lib.k8s.config_map.update import K8sConfigMapUpdate
from lib.k8s.config_map.wait import K8sConfigMapWait


class K8sConfigMap(
        K8sConfigMapApi,
        K8sConfigMapInfo,
        K8sConfigMapCreate,
        K8sConfigMapDelete,
        K8sConfigMapMatch,
        K8sConfigMapUpdate,
        K8sConfigMapWait
        ):
    def __init__(self):
        K8sConfigMapApi.__init__(self)
        K8sConfigMapInfo.__init__(self)
        K8sConfigMapCreate.__init__(self)
        K8sConfigMapDelete.__init__(self)
        K8sConfigMapMatch.__init__(self)
        K8sConfigMapUpdate.__init__(self)
        K8sConfigMapWait.__init__(self)
