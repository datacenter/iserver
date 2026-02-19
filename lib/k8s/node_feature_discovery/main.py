from lib.k8s.node_feature_discovery.api import K8sNodeFeatureDiscoveryApi
from lib.k8s.node_feature_discovery.info import K8sNodeFeatureDiscoveryInfo


class K8sNodeFeatureDiscovery(
        K8sNodeFeatureDiscoveryApi,
        K8sNodeFeatureDiscoveryInfo
        ):
    def __init__(self):
        K8sNodeFeatureDiscoveryApi.__init__(self)
        K8sNodeFeatureDiscoveryInfo.__init__(self)
