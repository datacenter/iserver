from lib.k8s.virtual_machine_snapshot.api import K8sVirtualMachineSnapshotApi
from lib.k8s.virtual_machine_snapshot.info import K8sVirtualMachineSnapshotInfo


class K8sVirtualMachineSnapshot(
        K8sVirtualMachineSnapshotApi,
        K8sVirtualMachineSnapshotInfo
        ):
    def __init__(self):
        K8sVirtualMachineSnapshotApi.__init__(self)
        K8sVirtualMachineSnapshotInfo.__init__(self)
