class K8sKnativeKafkaApi():
    def __init__(self):
        self.knative_kafka_mo = None
        self.knative_kafka_namespace_mo = {}

    def get_knative_kafka_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.knative_kafka_mo,
            self.knative_kafka_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.knative_kafka_mo, self.knative_kafka_namespace_mo = self.get_namespaced_resources(
            'KnativeKafka', 
            'operator.serverless.openshift.io/v1alpha1', 
            self.knative_kafka_mo,
            self.knative_kafka_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_knative_kafka_mo(self, namespace, name):
        success, _ = self.delete_resource('KnativeKafka', 'operator.serverless.openshift.io/v1alpha1', name, namespace=namespace)
        return success