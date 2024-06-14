from lib.k8s.virtual_machine_instance_type.api import K8sVirtualMachineInstanceTypeApi
from lib.k8s.virtual_machine_instance_type.info import K8sVirtualMachineInstanceTypeInfo


class K8sVirtualMachineInstanceType(
        K8sVirtualMachineInstanceTypeApi,
        K8sVirtualMachineInstanceTypeInfo
        ):
    def __init__(self):
        K8sVirtualMachineInstanceTypeApi.__init__(self)
        K8sVirtualMachineInstanceTypeInfo.__init__(self)
