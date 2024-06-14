from lib.k8s.machine_config_pool.api import K8sMachineConfigPoolApi
from lib.k8s.machine_config_pool.info import K8sMachineConfigPoolInfo


class K8sMachineConfigPool(
        K8sMachineConfigPoolApi,
        K8sMachineConfigPoolInfo
        ):
    def __init__(self):
        K8sMachineConfigPoolApi.__init__(self)
        K8sMachineConfigPoolInfo.__init__(self)
