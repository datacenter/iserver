from lib.ocp.lcm.vsphere.ipi.create import OcpVsphereIpiCreate
from lib.ocp.lcm.vsphere.ipi.delete import OcpVsphereIpiDelete
from lib.ocp.lcm.vsphere.ipi.installer import OcpVsphereIpiInstaller
from lib.ocp.lcm.vsphere.ipi.validate import OcpVsphereIpiValidate


class OcpVsphereIpi(OcpVsphereIpiCreate, OcpVsphereIpiDelete, OcpVsphereIpiInstaller, OcpVsphereIpiValidate):
    def __init__(self):
        OcpVsphereIpiCreate.__init__(self)
        OcpVsphereIpiDelete.__init__(self)
        OcpVsphereIpiInstaller.__init__(self)
        OcpVsphereIpiValidate.__init__(self)
