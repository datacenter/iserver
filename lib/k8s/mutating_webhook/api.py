class K8sMutatingWebhookApi():
    def __init__(self):
        self.mutating_webhook_mo = None
        
    def get_mutating_webhook_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.mutating_webhook_mo
        )
        if cache_hit:
            return response

        response, self.mutating_webhook_mo = self.get_resources(
            'MutatingWebhookConfiguration', 
            'admissionregistration.k8s.io/v1', 
            self.mutating_webhook_mo,
            name=name,
            api_type='admission'
        )

        return response

    def delete_mutating_webhook_mo(self, name):
        success, _ = self.delete_resource('MutatingWebhookConfiguration', 'admissionregistration.k8s.io/v1', name, api_type='admission')
        return success