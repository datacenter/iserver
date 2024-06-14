from lib.k8s.endpoint.api import K8sEndpointApi
from lib.k8s.endpoint.info import K8sEndpointInfo


class K8sEndpoint(
        K8sEndpointApi,
        K8sEndpointInfo
        ):
    def __init__(self):
        K8sEndpointApi.__init__(self)
        K8sEndpointInfo.__init__(self)
