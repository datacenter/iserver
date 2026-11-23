from lib import filter_helper


class K8sUserDefinedNetworkNamespace():
    def __init__(self):
        pass

    def is_namespace_udn_enabled(self, name=None, info=None, managed_object=None):
        if name is not None:
            info = self.get_namespace(name, cache_enabled=False)
            if info is None:
                return False
        
        if info is not None:
            labels = info['label']

        if managed_object is not None:
            labels = filter_helper.get(managed_object, 'metadata:labels', on_error={}, on_none={})

        if 'k8s.ovn.org/primary-user-defined-network' not in labels:
            return False
        
        if labels['k8s.ovn.org/primary-user-defined-network'] != '':
            return False
        
        return True

    def get_namespace_udns(self, name, cache_enabled=True):
        udns = self.get_user_defined_networks(cache_enabled=cache_enabled)
        if udns is None:
            return None
        
        namespace_udns = []
        for udn in udns:
            if udn['namespace'] != name:
                continue

            namespace_udns.append(udn['name'])
            
        return namespace_udns

    def get_namespace_primary_udn(self, name, cache_enabled=True):
        udns = self.get_user_defined_networks(cache_enabled=cache_enabled)
        if udns is None:
            return False
        
        for udn in udns:
            if udn['namespace'] != name:
                continue

            if udn['primary']:
                return udn['name']
            
        return None
    
    def is_namespace_primary_udn_configured(self, name, cache_enabled=True):
        if self.get_namespace_primary_udn(name, cache_enabled=cache_enabled) is None:
            return False
        return True
    