from lib.k8s.virtual_machine.api import K8sVirtualMachineApi
from lib.k8s.virtual_machine.info import K8sVirtualMachineInfo


class K8sVirtualMachine(
        K8sVirtualMachineApi,
        K8sVirtualMachineInfo
        ):
    def __init__(self):
        K8sVirtualMachineApi.__init__(self)
        K8sVirtualMachineInfo.__init__(self)
