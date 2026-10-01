from lib import ip_helper


class K8sPrivateNetworkNodeAttachmentInfo():
    def __init__(self):
        self.private_network_node_attachment = None

    def get_private_network_node_attachment_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        return info

    def get_private_network_node_attachments(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'private_network_node_attachment', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if return_mo:
            return infos

        return infos   
            
    def is_private_network_node_attachment(self, name, cache_enabled=True, optimized=True):
        if self.get_private_network_node_attachment(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_private_network_node_attachment(self, name, return_mo=False, cache_enabled=True, optimized=True):
        info = self.get_info(
            'private_network_node_attachment', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
        return info