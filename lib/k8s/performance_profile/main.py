from lib.k8s.performance_profile.api import K8sPerformanceProfileApi
from lib.k8s.performance_profile.info import K8sPerformanceProfileInfo


class K8sPerformanceProfile(
        K8sPerformanceProfileApi,
        K8sPerformanceProfileInfo
        ):
    def __init__(self):
        K8sPerformanceProfileApi.__init__(self)
        K8sPerformanceProfileInfo.__init__(self)
