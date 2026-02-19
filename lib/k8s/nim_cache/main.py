from lib.k8s.nim_cache.api import K8sNimCacheApi
from lib.k8s.nim_cache.info import K8sNimCacheInfo
from lib.k8s.nim_cache.create import K8sNimCacheCreate
from lib.k8s.nim_cache.delete import K8sNimCacheDelete
from lib.k8s.nim_cache.wait import K8sNimCacheWait


class K8sNimCache(
        K8sNimCacheApi,
        K8sNimCacheInfo,
        K8sNimCacheCreate,
        K8sNimCacheDelete,
        K8sNimCacheWait
        ):
    def __init__(self):
        K8sNimCacheApi.__init__(self)
        K8sNimCacheInfo.__init__(self)
        K8sNimCacheCreate.__init__(self)
        K8sNimCacheDelete.__init__(self)
        K8sNimCacheWait.__init__(self)
