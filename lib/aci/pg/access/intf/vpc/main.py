from lib.aci.pg.access.intf.vpc.api import PolicyGroupAccessInterfaceVpcApi
from lib.aci.pg.access.intf.vpc.info import PolicyGroupAccessInterfaceVpcInfo
from lib.aci.pg.access.intf.vpc.audit.main import PolicyGroupAccessInterfaceVpcAudit
from lib.aci.pg.access.intf.vpc.event.main import PolicyGroupAccessInterfaceVpcEvent
from lib.aci.pg.access.intf.vpc.fault.main import PolicyGroupAccessInterfaceVpcFault
from lib.aci.pg.access.intf.vpc.node.main import PolicyGroupAccessInterfaceVpcNode
from lib.aci.pg.access.intf.vpc.nodes.main import PolicyGroupAccessInterfaceVpcNodes
from lib.aci.pg.access.intf.vpc.ports.main import PolicyGroupAccessInterfaceVpcPort


class PolicyGroupAccessInterfaceVpc(
        PolicyGroupAccessInterfaceVpcApi,
        PolicyGroupAccessInterfaceVpcInfo,
        PolicyGroupAccessInterfaceVpcAudit,
        PolicyGroupAccessInterfaceVpcEvent,
        PolicyGroupAccessInterfaceVpcFault,
        PolicyGroupAccessInterfaceVpcNode,
        PolicyGroupAccessInterfaceVpcNodes,
        PolicyGroupAccessInterfaceVpcPort
        ):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcApi.__init__(self)
        PolicyGroupAccessInterfaceVpcInfo.__init__(self)
        PolicyGroupAccessInterfaceVpcNode.__init__(self)
        PolicyGroupAccessInterfaceVpcNodes.__init__(self)
        PolicyGroupAccessInterfaceVpcPort.__init__(self)
        PolicyGroupAccessInterfaceVpcAudit.__init__(self)
        PolicyGroupAccessInterfaceVpcEvent.__init__(self)
        PolicyGroupAccessInterfaceVpcFault.__init__(self)
