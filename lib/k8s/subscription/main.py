from lib.k8s.subscription.api import K8sSubscriptionApi
from lib.k8s.subscription.info import K8sSubscriptionInfo


class K8sSubscription(
        K8sSubscriptionApi,
        K8sSubscriptionInfo
        ):
    def __init__(self):
        K8sSubscriptionApi.__init__(self)
        K8sSubscriptionInfo.__init__(self)
