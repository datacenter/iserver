from lib.k8s.frr_node_state.api import K8sFrrNodeStateApi
from lib.k8s.frr_node_state.info import K8sFrrNodeStateInfo


class K8sFrrNodeState(
        K8sFrrNodeStateApi,
        K8sFrrNodeStateInfo
        ):
    def __init__(self):
        K8sFrrNodeStateApi.__init__(self)
        K8sFrrNodeStateInfo.__init__(self)
