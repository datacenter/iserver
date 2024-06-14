from lib.ocp.task.node.down import OcpTaskNodeDown
from lib.ocp.task.node.nestedhv import OcpTaskNestedHv
from lib.ocp.task.node.up import OcpTaskNodeUp


class OcpTaskNode(OcpTaskNodeDown, OcpTaskNestedHv, OcpTaskNodeUp):
    def __init__(self):
        OcpTaskNodeDown.__init__(self)
        OcpTaskNestedHv.__init__(self)
        OcpTaskNodeUp.__init__(self)

    def is_ocp_node_vm_powered_on(self, node_vm_name):
        if self.ocp_vcenter_handler is None:
            self.log.error(
                'ocp.is_node_vm_down',
                'vcenter connection failed'
            )
            return False

        return self.ocp_vcenter_handler.is_vm_powered_on(node_vm_name)
