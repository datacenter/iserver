class K8sObjectTransferApi():
    def __init__(self):
        self.object_transfer_mo = None

    def get_object_transfer_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.object_transfer_mo
        )
        if cache_hit:
            return response

        response, self.object_transfer_mo = self.get_resources(
            'ObjectTransfer', 
            'cdi.kubevirt.io/v1beta1', 
            self.object_transfer_mo,
            name=name
        )

        return response