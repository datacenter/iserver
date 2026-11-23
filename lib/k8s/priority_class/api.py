class K8sPriorityClassApi():
    def __init__(self):
        self.priority_class_mo = None

    def get_priority_class_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.priority_class_mo
        )
        if cache_hit:
            return response

        response, self.priority_class_mo = self.get_resources(
            'PriorityClass', 
            'scheduling.k8s.io/v1', 
            self.priority_class_mo,
            name=name
        )

        return response