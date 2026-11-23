import json

class K8sNetworkAttachmentDefinitionInfo():
    def __init__(self):
        self.nad = None

    def get_nad_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(
            managed_object
        )
        if info is None:
            return None

        info['resource_name'] = self.get(managed_object, 'metadata:annotations:k8s.v1.cni.cncf.io/resourceName')
        info['config'] = json.loads(
            self.get(managed_object, 'spec:config')
        )

        info['cudn'] = None
        if info['ownerT'][0] is not None and info['ownerT'][0] == 'ClusterUserDefinedNetwork':
            info['cudn'] = info['ownerT'][1]
            
        return info

    def get_nads(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'nad', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos  

    def is_nad(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_nad(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_nad(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'nad',
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )