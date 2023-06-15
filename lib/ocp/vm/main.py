from lib.ocp.vm.create.main import OcpVmCreate
from lib.ocp.vm.delete.main import OcpVmDelete
from lib.ocp.vm.get.main import OcpVmGet


class OcpVm(
    OcpVmCreate,
    OcpVmDelete,
    OcpVmGet
    ):
    def __init__(self):
        OcpVmCreate.__init__(self)
        OcpVmDelete.__init__(self)
        OcpVmGet.__init__(self)

        self.user_input = None

    def set_user_input(self, user_input):
        self.user_input = user_input
