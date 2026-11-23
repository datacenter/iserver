class K8sKnativeServingApi():
    def __init__(self):
        self.knative_serving_mo = None
        self.knative_serving_namespace_mo = {}

    def get_knative_serving_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.knative_serving_mo,
            self.knative_serving_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.knative_serving_mo, self.knative_serving_namespace_mo = self.get_namespaced_resources(
            'KnativeServing', 
            'operator.knative.dev/v1beta1', 
            self.knative_serving_mo,
            self.knative_serving_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_knative_serving_mo(self, namespace, name):
        success, _ = self.delete_resource('KnativeServing', 'operator.knative.dev/v1beta1', name, namespace=namespace)
        return success