from lib.k8s.virtual_machine_instance.api import K8sVirtualMachineInstanceApi
from lib.k8s.virtual_machine_instance.info import K8sVirtualMachineInstanceInfo


class K8sVirtualMachineInstance(
        K8sVirtualMachineInstanceApi,
        K8sVirtualMachineInstanceInfo
        ):
    def __init__(self):
        K8sVirtualMachineInstanceApi.__init__(self)
        K8sVirtualMachineInstanceInfo.__init__(self)
