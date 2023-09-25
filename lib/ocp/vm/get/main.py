from lib.ocp.vm.get.bgp import OcpVmGetBgp
from lib.ocp.vm.get.disk import OcpVmGetDisk
from lib.ocp.vm.get.fabric import OcpVmGetFabric
from lib.ocp.vm.get.image import OcpVmGetImage
from lib.ocp.vm.get.info import OcpVmGetInfo
from lib.ocp.vm.get.network import OcpVmGetNetwork
from lib.ocp.vm.get.sriov import OcpVmGetSriov
from lib.ocp.vm.get.ssh import OcpVmGetSsh


class OcpVmGet(
    OcpVmGetBgp,
    OcpVmGetDisk,
    OcpVmGetFabric,
    OcpVmGetImage,
    OcpVmGetInfo,
    OcpVmGetNetwork,
    OcpVmGetSsh,
    OcpVmGetSriov
    ):
    def __init__(self):
        OcpVmGetBgp.__init__(self)
        OcpVmGetDisk.__init__(self)
        OcpVmGetFabric.__init__(self)
        OcpVmGetImage.__init__(self)
        OcpVmGetInfo.__init__(self)
        OcpVmGetNetwork.__init__(self)
        OcpVmGetSsh.__init__(self)
        OcpVmGetSriov.__init__(self)
