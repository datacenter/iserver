from lib.k8s.endpoint.api import K8sEndpointApi
from lib.k8s.endpoint.info import K8sEndpointInfo
from lib.k8s.endpoint.wait import K8sEndpointWait
from lib.k8s.endpoint.cilium_timescape import K8sEndpointCiliumTimescape


class K8sEndpoint(
        K8sEndpointApi,
        K8sEndpointInfo,
        K8sEndpointWait,
        K8sEndpointCiliumTimescape
        ):
    def __init__(self):
        K8sEndpointApi.__init__(self)
        K8sEndpointInfo.__init__(self)
        K8sEndpointWait.__init__(self)
        K8sEndpointCiliumTimescape.__init__(self)
