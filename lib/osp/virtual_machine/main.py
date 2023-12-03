from lib.osp.virtual_machine.api import OspVirtualMachineApi
from lib.osp.virtual_machine.info import OspVirtualMachineInfo
from lib.osp.virtual_machine.task import OspVirtualMachineTask


class OspVirtualMachine(
        OspVirtualMachineApi,
        OspVirtualMachineInfo,
        OspVirtualMachineTask
        ):
    def __init__(self):
        OspVirtualMachineApi.__init__(self)
        OspVirtualMachineInfo.__init__(self)
        OspVirtualMachineTask.__init__(self)
