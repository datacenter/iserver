class K8sTracingPolicyNamespacedDelete():
    def __init__(self):
        pass

    def delete_tracing_policy_namespaced(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'TracingPolicyNamespaced', 
            'cilium.io/v1alpha1',
            name, 
            'tracing_policy_namespaced',
            namespace=namespace, 
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        return success
    
    def delete_tracing_policy_namespaceds(self, my_output=None, wait=True):
        items = self.get_tracing_policy_namespaceds(
            cache_enabled=False
        )
        if items is None:
            if my_output is not None:
                my_output.error('Failed to get tetragon tracing policy namespaced')
            return False
        
        for item in items:
            success = self.delete_tracing_policy_namespaced(
                item['namespace'],
                item['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True