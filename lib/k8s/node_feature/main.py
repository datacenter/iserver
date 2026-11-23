from lib.k8s.node_feature.api import K8sNodeFeatureApi
from lib.k8s.node_feature.info import K8sNodeFeatureInfo


class K8sNodeFeature(
        K8sNodeFeatureApi,
        K8sNodeFeatureInfo
        ):
    def __init__(self):
        K8sNodeFeatureApi.__init__(self)
        K8sNodeFeatureInfo.__init__(self)
