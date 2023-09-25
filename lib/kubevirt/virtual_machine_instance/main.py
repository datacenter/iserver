from lib.kubevirt.virtual_machine_instance.api import KubevirtVirtualMachineInstanceApi
from lib.kubevirt.virtual_machine_instance.info import KubevirtVirtualMachineInstanceInfo


class KubevirtVirtualMachineInstance(
        KubevirtVirtualMachineInstanceApi,
        KubevirtVirtualMachineInstanceInfo
        ):
    def __init__(self):
        KubevirtVirtualMachineInstanceApi.__init__(self)
        KubevirtVirtualMachineInstanceInfo.__init__(self)
