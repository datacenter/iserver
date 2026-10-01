class K8sKnativeEventingApi():
    def __init__(self):
        self.knative_eventing_mo = None
        self.knative_eventing_namespace_mo = {}

    def get_knative_eventing_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.knative_eventing_mo,
            self.knative_eventing_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.knative_eventing_mo, self.knative_eventing_namespace_mo = self.get_namespaced_resources(
            'KnativeEventing', 
            'operator.knative.dev/v1beta1', 
            self.knative_eventing_mo,
            self.knative_eventing_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_knative_eventing_mo(self, namespace, name):
        success, _ = self.delete_resource('KnativeEventing', 'operator.knative.dev/v1beta1', name, namespace=namespace)
        return success