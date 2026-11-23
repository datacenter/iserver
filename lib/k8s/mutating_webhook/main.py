from lib.k8s.mutating_webhook.api import K8sMutatingWebhookApi
from lib.k8s.mutating_webhook.info import K8sMutatingWebhookInfo
from lib.k8s.mutating_webhook.delete import K8sMutatingWebhookDelete
from lib.k8s.mutating_webhook.wait import K8sMutatingWebhookWait


class K8sMutatingWebhook(
        K8sMutatingWebhookApi,
        K8sMutatingWebhookInfo,
        K8sMutatingWebhookDelete,
        K8sMutatingWebhookWait
        ):
    def __init__(self):
        K8sMutatingWebhookApi.__init__(self)
        K8sMutatingWebhookInfo.__init__(self)
        K8sMutatingWebhookDelete.__init__(self)
        K8sMutatingWebhookWait.__init__(self)
