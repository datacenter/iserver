from lib.ocp.vm.create.day0 import OcpVmCreateDay0
from lib.ocp.vm.create.deployment import OcpVmCreateDeployment
from lib.ocp.vm.create.image import OcpVmCreateImage
from lib.ocp.vm.create.network import OcpVmCreateNetwork
from lib.ocp.vm.create.policy import OcpVmCreatePolicy
from lib.ocp.vm.create.service import OcpVmCreateService
from lib.ocp.vm.create.vm import OcpVmCreateVm


class OcpVmCreate(
    OcpVmCreateDay0,
    OcpVmCreateDeployment,
    OcpVmCreateImage,
    OcpVmCreateNetwork,
    OcpVmCreatePolicy,
    OcpVmCreateService,
    OcpVmCreateVm
    ):
    def __init__(self):
        OcpVmCreateDay0.__init__(self)
        OcpVmCreateDeployment.__init__(self)
        OcpVmCreateImage.__init__(self)
        OcpVmCreateNetwork.__init__(self)
        OcpVmCreatePolicy.__init__(self)
        OcpVmCreateService.__init__(self)
        OcpVmCreateVm.__init__(self)
