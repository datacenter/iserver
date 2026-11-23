from lib.k8s.private_network_external_endpoint.api import K8sPrivateNetworkExternalEndpointApi
from lib.k8s.private_network_external_endpoint.info import K8sPrivateNetworkExternalEndpointInfo


class K8sPrivateNetworkExternalEndpoint(
        K8sPrivateNetworkExternalEndpointApi,
        K8sPrivateNetworkExternalEndpointInfo
        ):
    def __init__(self):
        K8sPrivateNetworkExternalEndpointApi.__init__(self)
        K8sPrivateNetworkExternalEndpointInfo.__init__(self)
