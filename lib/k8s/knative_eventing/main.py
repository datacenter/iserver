from lib.k8s.knative_eventing.api import K8sKnativeEventingApi
from lib.k8s.knative_eventing.info import K8sKnativeEventingInfo


class K8sKnativeEventing(
        K8sKnativeEventingApi,
        K8sKnativeEventingInfo
        ):
    def __init__(self):
        K8sKnativeEventingApi.__init__(self)
        K8sKnativeEventingInfo.__init__(self)
