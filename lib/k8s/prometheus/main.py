from lib.k8s.prometheus.api import K8sPrometheusApi
from lib.k8s.prometheus.info import K8sPrometheusInfo


class K8sPrometheus(
        K8sPrometheusApi,
        K8sPrometheusInfo
        ):
    def __init__(self):
        K8sPrometheusApi.__init__(self)
        K8sPrometheusInfo.__init__(self)
