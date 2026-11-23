from lib.k8s.prometheus_target.api import K8sPrometheusTargetApi
from lib.k8s.prometheus_target.info import K8sPrometheusTargetInfo


class K8sPrometheusTarget(
        K8sPrometheusTargetApi,
        K8sPrometheusTargetInfo
        ):
    def __init__(self):
        K8sPrometheusTargetApi.__init__(self)
        K8sPrometheusTargetInfo.__init__(self)
