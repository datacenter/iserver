from lib.k8s.network_addons_config.api import K8sNetworkAddonsConfigApi
from lib.k8s.network_addons_config.info import K8sNetworkAddonsConfigInfo


class K8sNetworkAddonsConfig(
        K8sNetworkAddonsConfigApi,
        K8sNetworkAddonsConfigInfo
        ):
    def __init__(self):
        K8sNetworkAddonsConfigApi.__init__(self)
        K8sNetworkAddonsConfigInfo.__init__(self)
