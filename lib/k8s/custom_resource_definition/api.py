class K8sCustomResourceDefinitionApi():
    def __init__(self):
        self.custom_resource_definition_mo = None

    def get_custom_resource_definition_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.custom_resource_definition_mo
        )
        if cache_hit:
            return response

        response, self.custom_resource_definition_mo = self.get_resources(
            'CustomResourceDefinition', 
            'apiextensions.k8s.io/v1', 
            self.custom_resource_definition_mo,
            name=name
        )

        return response