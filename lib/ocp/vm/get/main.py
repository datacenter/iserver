from lib.ocp.vm.get.bgp import OcpVmGetBgp
from lib.ocp.vm.get.day0 import OcpVmGetDay0
from lib.ocp.vm.get.disk import OcpVmGetDisk
from lib.ocp.vm.get.fabric import OcpVmGetFabric
from lib.ocp.vm.get.image import OcpVmGetImage
from lib.ocp.vm.get.info import OcpVmGetInfo
from lib.ocp.vm.get.network import OcpVmGetNetwork
from lib.ocp.vm.get.node import OcpVmGetNode
from lib.ocp.vm.get.pod import OcpVmGetPod
from lib.ocp.vm.get.service import OcpVmGetService
from lib.ocp.vm.get.sriov import OcpVmGetSriov
from lib.ocp.vm.get.ssh import OcpVmGetSsh
from lib.ocp.vm.get.vm import OcpVmGetVm
from lib.ocp.vm.get.vmi import OcpVmGetVmi


class OcpVmGet(
    OcpVmGetBgp,
    OcpVmGetDay0,
    OcpVmGetDisk,
    OcpVmGetFabric,
    OcpVmGetImage,
    OcpVmGetInfo,
    OcpVmGetNetwork,
    OcpVmGetNode,
    OcpVmGetPod,
    OcpVmGetService,
    OcpVmGetSsh,
    OcpVmGetSriov,
    OcpVmGetVm,
    OcpVmGetVmi
    ):
    def __init__(self):
        OcpVmGetBgp.__init__(self)
        OcpVmGetDay0.__init__(self)
        OcpVmGetDisk.__init__(self)
        OcpVmGetFabric.__init__(self)
        OcpVmGetImage.__init__(self)
        OcpVmGetInfo.__init__(self)
        OcpVmGetNetwork.__init__(self)
        OcpVmGetNode.__init__(self)
        OcpVmGetPod.__init__(self)
        OcpVmGetService.__init__(self)
        OcpVmGetSsh.__init__(self)
        OcpVmGetSriov.__init__(self)
        OcpVmGetVm.__init__(self)
        OcpVmGetVmi.__init__(self)
