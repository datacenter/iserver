from lib.k8s.user_defined_network.api import K8sUserDefinedNetworkApi
from lib.k8s.user_defined_network.info import K8sUserDefinedNetworkInfo
from lib.k8s.user_defined_network.delete import K8sUserDefinedNetworkDelete
from lib.k8s.user_defined_network.l2 import K8sUserDefinedNetworkL2
from lib.k8s.user_defined_network.l3 import K8sUserDefinedNetworkL3
from lib.k8s.user_defined_network.match import K8sUserDefinedNetworkMatch
from lib.k8s.user_defined_network.namespace import K8sUserDefinedNetworkNamespace
from lib.k8s.user_defined_network.wait import K8sUserDefinedNetworkWait


class K8sUserDefinedNetwork(
        K8sUserDefinedNetworkApi,
        K8sUserDefinedNetworkInfo,
        K8sUserDefinedNetworkDelete,
        K8sUserDefinedNetworkL2,
        K8sUserDefinedNetworkL3,
        K8sUserDefinedNetworkMatch,
        K8sUserDefinedNetworkNamespace,
        K8sUserDefinedNetworkWait
        ):
    def __init__(self):
        K8sUserDefinedNetworkApi.__init__(self)
        K8sUserDefinedNetworkInfo.__init__(self)
        K8sUserDefinedNetworkDelete.__init__(self)
        K8sUserDefinedNetworkL2.__init__(self)
        K8sUserDefinedNetworkL3.__init__(self)
        K8sUserDefinedNetworkMatch.__init__(self)
        K8sUserDefinedNetworkNamespace
        K8sUserDefinedNetworkWait.__init__(self)
