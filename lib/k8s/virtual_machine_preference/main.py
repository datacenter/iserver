from lib.k8s.virtual_machine_preference.api import K8sVirtualMachinePreferenceApi
from lib.k8s.virtual_machine_preference.info import K8sVirtualMachinePreferenceInfo


class K8sVirtualMachinePreference(
        K8sVirtualMachinePreferenceApi,
        K8sVirtualMachinePreferenceInfo
        ):
    def __init__(self):
        K8sVirtualMachinePreferenceApi.__init__(self)
        K8sVirtualMachinePreferenceInfo.__init__(self)
