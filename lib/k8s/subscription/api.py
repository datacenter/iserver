class K8sSubscriptionApi():
    def __init__(self):
        self.subscription_mo = None
        self.subscription_namespace_mo = {}

    def get_subscription_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.subscription_mo,
            self.subscription_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.subscription_mo, self.subscription_namespace_mo = self.get_namespaced_resources(
            'Subscription', 
            'operators.coreos.com/v1alpha1', 
            self.subscription_mo,
            self.subscription_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_subscription_mo(self, namespace, name):
        return self.delete_resource('Subscription', 'operators.coreos.com/v1alpha1', name, namespace=namespace)
