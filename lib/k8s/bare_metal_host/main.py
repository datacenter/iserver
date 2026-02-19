from lib.k8s.bare_metal_host.api import K8sBareMetalHostApi
from lib.k8s.bare_metal_host.info import K8sBareMetalHostInfo


class K8sBareMetalHost(
        K8sBareMetalHostApi,
        K8sBareMetalHostInfo
        ):
    def __init__(self):
        K8sBareMetalHostApi.__init__(self)
        K8sBareMetalHostInfo.__init__(self)
