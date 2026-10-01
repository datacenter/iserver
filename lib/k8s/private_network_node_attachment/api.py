class K8sPrivateNetworkNodeAttachmentApi():
    def __init__(self):
        self.private_network_node_attachment_mo = None

    def get_private_network_node_attachment_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.private_network_node_attachment_mo
        )
        if cache_hit:
            return response

        response, self.private_network_node_attachment_mo = self.get_resources(
            'PrivateNetworkNodeAttachment', 
            'isovalent.com/v1alpha1', 
            self.private_network_node_attachment_mo,
            name=name
        )

        return response

    def delete_private_network_node_attachment_mo(self, name):
        success, _ = self.delete_resource('PrivateNetworkNodeAttachment', 'isovalent.com/v1alpha1', name)
        return success