from lib.k8s.virtual_machine_instance.api import K8sVirtualMachineInstanceApi
from lib.k8s.virtual_machine_instance.info import K8sVirtualMachineInstanceInfo
from lib.k8s.virtual_machine_instance.wait import K8sVirtualMachineInstanceWait


class K8sVirtualMachineInstance(
        K8sVirtualMachineInstanceApi,
        K8sVirtualMachineInstanceInfo,
        K8sVirtualMachineInstanceWait
        ):
    def __init__(self):
        K8sVirtualMachineInstanceApi.__init__(self)
        K8sVirtualMachineInstanceInfo.__init__(self)
        K8sVirtualMachineInstanceWait.__init__(self)
