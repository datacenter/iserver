from lib.k8s.machine_config.api import K8sMachineConfigApi
from lib.k8s.machine_config.info import K8sMachineConfigInfo
from lib.k8s.machine_config.ssh import K8sMachineConfigSsh


class K8sMachineConfig(
        K8sMachineConfigApi,
        K8sMachineConfigInfo,
        K8sMachineConfigSsh
        ):
    def __init__(self):
        K8sMachineConfigApi.__init__(self)
        K8sMachineConfigInfo.__init__(self)
        K8sMachineConfigSsh.__init__(self)
