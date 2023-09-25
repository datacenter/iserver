from lib.k8s.virtual_machine_restore.api import K8sVirtualMachineRestoreApi
from lib.k8s.virtual_machine_restore.info import K8sVirtualMachineRestoreInfo


class K8sVirtualMachineRestore(
        K8sVirtualMachineRestoreApi,
        K8sVirtualMachineRestoreInfo
        ):
    def __init__(self):
        K8sVirtualMachineRestoreApi.__init__(self)
        K8sVirtualMachineRestoreInfo.__init__(self)
