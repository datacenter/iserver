from lib.k8s.virtual_machine_instance_preset.api import K8sVirtualMachineInstancePresetApi
from lib.k8s.virtual_machine_instance_preset.info import K8sVirtualMachineInstancePresetInfo


class K8sVirtualMachineInstancePreset(
        K8sVirtualMachineInstancePresetApi,
        K8sVirtualMachineInstancePresetInfo
        ):
    def __init__(self):
        K8sVirtualMachineInstancePresetApi.__init__(self)
        K8sVirtualMachineInstancePresetInfo.__init__(self)
