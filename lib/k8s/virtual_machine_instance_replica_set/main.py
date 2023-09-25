from lib.k8s.virtual_machine_instance_replica_set.api import K8sVirtualMachineInstanceReplicaSetApi
from lib.k8s.virtual_machine_instance_replica_set.info import K8sVirtualMachineInstanceReplicaSetInfo


class K8sVirtualMachineInstanceReplicaSet(
        K8sVirtualMachineInstanceReplicaSetApi,
        K8sVirtualMachineInstanceReplicaSetInfo
        ):
    def __init__(self):
        K8sVirtualMachineInstanceReplicaSetApi.__init__(self)
        K8sVirtualMachineInstanceReplicaSetInfo.__init__(self)
