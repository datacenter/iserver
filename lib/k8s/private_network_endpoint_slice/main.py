from lib.k8s.private_network_endpoint_slice.api import K8sPrivateNetworkEndpointSliceApi
from lib.k8s.private_network_endpoint_slice.info import K8sPrivateNetworkEndpointSliceInfo


class K8sPrivateNetworkEndpointSlice(
        K8sPrivateNetworkEndpointSliceApi,
        K8sPrivateNetworkEndpointSliceInfo
        ):
    def __init__(self):
        K8sPrivateNetworkEndpointSliceApi.__init__(self)
        K8sPrivateNetworkEndpointSliceInfo.__init__(self)
