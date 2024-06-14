from lib.ocp.vm.delete.day0 import OcpVmDeleteDay0
from lib.ocp.vm.delete.deployment import OcpVmDeleteDeployment
from lib.ocp.vm.delete.image import OcpVmDeleteImage
from lib.ocp.vm.delete.network import OcpVmDeleteNetwork
from lib.ocp.vm.delete.policy import OcpVmDeletePolicy
from lib.ocp.vm.delete.service import OcpVmDeleteService
from lib.ocp.vm.delete.vm import OcpVmDeleteVm


class OcpVmDelete(
    OcpVmDeleteDay0,
    OcpVmDeleteDeployment,
    OcpVmDeleteImage,
    OcpVmDeleteNetwork,
    OcpVmDeletePolicy,
    OcpVmDeleteService,
    OcpVmDeleteVm
    ):
    def __init__(self):
        OcpVmDeleteDay0.__init__(self)
        OcpVmDeleteDeployment.__init__(self)
        OcpVmDeleteImage.__init__(self)
        OcpVmDeleteNetwork.__init__(self)
        OcpVmDeletePolicy.__init__(self)
        OcpVmDeleteService.__init__(self)
        OcpVmDeleteVm.__init__(self)
