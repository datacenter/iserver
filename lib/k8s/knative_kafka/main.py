from lib.k8s.knative_kafka.api import K8sKnativeKafkaApi
from lib.k8s.knative_kafka.info import K8sKnativeKafkaInfo


class K8sKnativeKafka(
        K8sKnativeKafkaApi,
        K8sKnativeKafkaInfo
        ):
    def __init__(self):
        K8sKnativeKafkaApi.__init__(self)
        K8sKnativeKafkaInfo.__init__(self)
