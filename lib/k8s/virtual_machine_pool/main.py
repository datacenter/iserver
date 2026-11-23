from lib.k8s.virtual_machine_pool.api import K8sVirtualMachinePoolApi
from lib.k8s.virtual_machine_pool.info import K8sVirtualMachinePoolInfo


class K8sVirtualMachinePool(
        K8sVirtualMachinePoolApi,
        K8sVirtualMachinePoolInfo
        ):
    def __init__(self):
        K8sVirtualMachinePoolApi.__init__(self)
        K8sVirtualMachinePoolInfo.__init__(self)
