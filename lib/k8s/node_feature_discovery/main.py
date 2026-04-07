from lib.k8s.node_feature_discovery.api import K8sNodeFeatureDiscoveryApi
from lib.k8s.node_feature_discovery.info import K8sNodeFeatureDiscoveryInfo
from lib.k8s.node_feature_discovery.create import K8sNodeFeatureDiscoveryCreate
from lib.k8s.node_feature_discovery.delete import K8sNodeFeatureDiscoveryDelete
from lib.k8s.node_feature_discovery.wait import K8sNodeFeatureDiscoveryWait


class K8sNodeFeatureDiscovery(
        K8sNodeFeatureDiscoveryApi,
        K8sNodeFeatureDiscoveryInfo,
        K8sNodeFeatureDiscoveryCreate,
        K8sNodeFeatureDiscoveryDelete,
        K8sNodeFeatureDiscoveryWait
        ):
    def __init__(self):
        K8sNodeFeatureDiscoveryApi.__init__(self)
        K8sNodeFeatureDiscoveryInfo.__init__(self)
        K8sNodeFeatureDiscoveryCreate.__init__(self)
        K8sNodeFeatureDiscoveryDelete.__init__(self)
        K8sNodeFeatureDiscoveryWait.__init__(self)
