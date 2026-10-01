class K8sNemoGuardrailApi():
    def __init__(self):
        self.nemo_guardrail_mo = None
        self.nemo_guardrail_namespace_mo = {}

    def get_nemo_guardrail_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.nemo_guardrail_mo,
            self.nemo_guardrail_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.nemo_guardrail_mo, self.nemo_guardrail_namespace_mo = self.get_namespaced_resources(
            'NemoGuardrail', 
            'apps.nvidia.com/v1alpha1', 
            self.nemo_guardrail_mo,
            self.nemo_guardrail_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_nemo_guardrail_mo(self, namespace, name):
        success, _ = self.delete_resource('NemoGuardrail', 'apps.nvidia.com/v1alpha1', name, namespace=namespace)
        return success