from lib.kubevirt.virtual_machine.api import KubevirtVirtualMachineApi
from lib.kubevirt.virtual_machine.info import KubevirtVirtualMachineInfo


class KubevirtVirtualMachine(
        KubevirtVirtualMachineApi,
        KubevirtVirtualMachineInfo
        ):
    def __init__(self):
        KubevirtVirtualMachineApi.__init__(self)
        KubevirtVirtualMachineInfo.__init__(self)
