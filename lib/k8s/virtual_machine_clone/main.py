from lib.k8s.virtual_machine_clone.api import K8sVirtualMachineCloneApi
from lib.k8s.virtual_machine_clone.info import K8sVirtualMachineCloneInfo


class K8sVirtualMachineClone(
        K8sVirtualMachineCloneApi,
        K8sVirtualMachineCloneInfo
        ):
    def __init__(self):
        K8sVirtualMachineCloneApi.__init__(self)
        K8sVirtualMachineCloneInfo.__init__(self)
