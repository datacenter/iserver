from lib.k8s.virtual_machine_cluster_instance_type.api import K8sVirtualMachineClusterInstanceTypeApi
from lib.k8s.virtual_machine_cluster_instance_type.info import K8sVirtualMachineClusterInstanceTypeInfo


class K8sVirtualMachineClusterInstanceType(
        K8sVirtualMachineClusterInstanceTypeApi,
        K8sVirtualMachineClusterInstanceTypeInfo
        ):
    def __init__(self):
        K8sVirtualMachineClusterInstanceTypeApi.__init__(self)
        K8sVirtualMachineClusterInstanceTypeInfo.__init__(self)
