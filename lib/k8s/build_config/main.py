from lib.k8s.build_config.api import K8sBuildConfigApi
from lib.k8s.build_config.info import K8sBuildConfigInfo
from lib.k8s.build_config.delete import K8sBuildConfigDelete
from lib.k8s.build_config.wait import K8sBuildConfigWait


class K8sBuildConfig(
        K8sBuildConfigApi,
        K8sBuildConfigInfo,
        K8sBuildConfigDelete,
        K8sBuildConfigWait,
        ):
    def __init__(self):
        K8sBuildConfigApi.__init__(self)
        K8sBuildConfigInfo.__init__(self)
        K8sBuildConfigDelete.__init__(self)
        K8sBuildConfigWait.__init__(self)
