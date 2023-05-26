from lib.ocp.vm.create import OcpVmCreate
from lib.ocp.vm.day0 import OcpVmDay0
from lib.ocp.vm.delete import OcpVmDelete
from lib.ocp.vm.disk import OcpVmDisk
from lib.ocp.vm.image import OcpVmImage
from lib.ocp.vm.info import OcpVmInfo
from lib.ocp.vm.instance import OcpVmInstance
from lib.ocp.vm.mo import OcpVmMo
from lib.ocp.vm.net import OcpVmNet
from lib.ocp.vm.pod import OcpVmPod
from lib.ocp.vm.report import OcpVmReport
from lib.ocp.vm.svc import OcpVmSvc
from lib.ocp.vm.ssh import OcpVmSsh


class OcpVm(
    OcpVmCreate,
    OcpVmDay0,
    OcpVmDelete,
    OcpVmDisk,
    OcpVmImage,
    OcpVmInfo,
    OcpVmInstance,
    OcpVmMo,
    OcpVmNet,
    OcpVmPod,
    OcpVmReport,
    OcpVmSvc,
    OcpVmSsh
    ):
    def __init__(self):
        OcpVmCreate.__init__(self)
        OcpVmDay0.__init__(self)
        OcpVmDelete.__init__(self)
        OcpVmDisk.__init__(self)
        OcpVmImage.__init__(self)
        OcpVmInfo.__init__(self)
        OcpVmInstance.__init__(self)
        OcpVmMo.__init__(self)
        OcpVmNet.__init__(self)
        OcpVmPod.__init__(self)
        OcpVmReport.__init__(self)
        OcpVmSvc.__init__(self)
        OcpVmSsh.__init__(self)
