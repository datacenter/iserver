from lib.k8s.virtual_machine.api import K8sVirtualMachineApi
from lib.k8s.virtual_machine.info import K8sVirtualMachineInfo
from lib.k8s.virtual_machine.create.main import K8sVirtualMachineCreate
from lib.k8s.virtual_machine.cpu import K8sVirtualMachineCpu
from lib.k8s.virtual_machine.delete import K8sVirtualMachineDelete
from lib.k8s.virtual_machine.memory import K8sVirtualMachineMemory
from lib.k8s.virtual_machine.pause import K8sVirtualMachinePause
from lib.k8s.virtual_machine.restart import K8sVirtualMachineRestart
from lib.k8s.virtual_machine.start import K8sVirtualMachineStart
from lib.k8s.virtual_machine.stop import K8sVirtualMachineStop
from lib.k8s.virtual_machine.unpause import K8sVirtualMachineUnpause
from lib.k8s.virtual_machine.wait import K8sVirtualMachineWait


class K8sVirtualMachine(
        K8sVirtualMachineApi,
        K8sVirtualMachineInfo,
        K8sVirtualMachineCreate,
        K8sVirtualMachineCpu,
        K8sVirtualMachineDelete,
        K8sVirtualMachineMemory,
        K8sVirtualMachinePause,
        K8sVirtualMachineRestart,
        K8sVirtualMachineStart,
        K8sVirtualMachineStop,
        K8sVirtualMachineUnpause,
        K8sVirtualMachineWait
        ):
    def __init__(self):
        K8sVirtualMachineApi.__init__(self)
        K8sVirtualMachineInfo.__init__(self)
        K8sVirtualMachineCreate.__init__(self)
        K8sVirtualMachineCpu.__init__(self)
        K8sVirtualMachineDelete.__init__(self)
        K8sVirtualMachineMemory.__init__(self)
        K8sVirtualMachinePause.__init__(self)
        K8sVirtualMachineRestart.__init__(self)
        K8sVirtualMachineStart.__init__(self)
        K8sVirtualMachineStop.__init__(self)
        K8sVirtualMachineUnpause.__init__(self)
        K8sVirtualMachineWait.__init__(self)
