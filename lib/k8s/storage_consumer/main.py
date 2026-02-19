from lib.k8s.storage_consumer.api import K8sStorageConsumerApi
from lib.k8s.storage_consumer.info import K8sStorageConsumerInfo


class K8sStorageConsumer(
        K8sStorageConsumerApi,
        K8sStorageConsumerInfo
        ):
    def __init__(self):
        K8sStorageConsumerApi.__init__(self)
        K8sStorageConsumerInfo.__init__(self)
