from lib.k8s.virtual_machine_snapshot_content.api import K8sVirtualMachineSnapshotContentApi
from lib.k8s.virtual_machine_snapshot_content.info import K8sVirtualMachineSnapshotContentInfo


class K8sVirtualMachineSnapshotContent(
        K8sVirtualMachineSnapshotContentApi,
        K8sVirtualMachineSnapshotContentInfo
        ):
    def __init__(self):
        K8sVirtualMachineSnapshotContentApi.__init__(self)
        K8sVirtualMachineSnapshotContentInfo.__init__(self)
