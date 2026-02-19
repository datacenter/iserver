from lib.k8s.nim_build.api import K8sNimBuildApi
from lib.k8s.nim_build.info import K8sNimBuildInfo
from lib.k8s.nim_build.create import K8sNimBuildCreate
from lib.k8s.nim_build.delete import K8sNimBuildDelete
from lib.k8s.nim_build.wait import K8sNimBuildWait


class K8sNimBuild(
        K8sNimBuildApi,
        K8sNimBuildInfo,
        K8sNimBuildCreate,
        K8sNimBuildDelete,
        K8sNimBuildWait
        ):
    def __init__(self):
        K8sNimBuildApi.__init__(self)
        K8sNimBuildInfo.__init__(self)
        K8sNimBuildCreate.__init__(self)
        K8sNimBuildDelete.__init__(self)
        K8sNimBuildWait.__init__(self)
