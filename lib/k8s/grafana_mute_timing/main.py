from lib.k8s.grafana_mute_timing.api import K8sGrafanaMuteTimingApi
from lib.k8s.grafana_mute_timing.info import K8sGrafanaMuteTimingInfo


class K8sGrafanaMuteTiming(
        K8sGrafanaMuteTimingApi,
        K8sGrafanaMuteTimingInfo
        ):
    def __init__(self):
        K8sGrafanaMuteTimingApi.__init__(self)
        K8sGrafanaMuteTimingInfo.__init__(self)
