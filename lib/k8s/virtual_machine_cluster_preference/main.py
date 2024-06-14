from lib.k8s.virtual_machine_cluster_preference.api import K8sVirtualMachineClusterPreferenceApi
from lib.k8s.virtual_machine_cluster_preference.info import K8sVirtualMachineClusterPreferenceInfo


class K8sVirtualMachineClusterPreference(
        K8sVirtualMachineClusterPreferenceApi,
        K8sVirtualMachineClusterPreferenceInfo
        ):
    def __init__(self):
        K8sVirtualMachineClusterPreferenceApi.__init__(self)
        K8sVirtualMachineClusterPreferenceInfo.__init__(self)
