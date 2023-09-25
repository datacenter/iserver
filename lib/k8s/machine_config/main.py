from lib.k8s.machine_config.api import K8sMachineConfigApi
from lib.k8s.machine_config.info import K8sMachineConfigInfo


class K8sMachineConfig(
        K8sMachineConfigApi,
        K8sMachineConfigInfo
        ):
    def __init__(self):
        K8sMachineConfigApi.__init__(self)
        K8sMachineConfigInfo.__init__(self)
