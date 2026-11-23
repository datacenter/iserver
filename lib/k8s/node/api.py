import traceback


class K8sNodeApi():
    def __init__(self):
        self.node_mo = None

    def get_node_mo(self, name=None, cache_enabled=True, fast=False):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.node_mo
        )
        if cache_hit:
            return response

        response, self.node_mo = self.get_resources(
            'Node', 
            'v1', 
            self.node_mo,
            name=name,
            fast=fast
        )

        return response