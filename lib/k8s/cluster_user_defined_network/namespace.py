from lib import filter_helper


class K8sClusterUserDefinedNetworkNamespace():
    def __init__(self):
        pass

    def validate_cluster_user_defined_network_namespace(self, params, cache_enabled=True, validate_primary=False, cudn=None):
        if len(params) == 0:
            return None, 'namespace dict with entries required'

        if len(params) != 1:
            return None, 'namespace dict with single entry required'

        namespaces = []
        names = []

        for key in params:
            if key not in ['label']:
                return None, 'unsupported namespace key'
        
            if key == 'label':
                if not isinstance(params[key], list):
                    return None, 'namespace label with list of strings required'
                
                if len(params[key]) == 0:
                    return None, 'namespace label with list of strings required'
                
                for item in params[key]:
                    if len(item.split(':')) != 2:
                        return None, 'namespace label with list of key:value required'

                    candidates = self.get_namespaces(object_filter=['label:%s' % (item)], cache_enabled=cache_enabled)
                    cache_enabled = True
                    if candidates is None:
                        return None, 'failed to get namespaces'
                    
                    for candidate in candidates:
                        if candidate['name'] == 'default':
                            return None, 'default namespace not supported'
                        
                        if candidate['name'].startswith('openshift-'):
                            return None, 'openshift-* namespace not supported'

                        if candidate['name'] not in namespaces:
                            names.append(candidate['name'])
                            namespaces.append(candidate)
        
        if len(namespaces) == 0:
            return None, 'select at least one namespace'
        
        if validate_primary and cudn is not None:
            for name in names:
                namespace_cudn = self.get_namespace_primary_cudn(name, cache_enabled=False)
                if namespace_cudn is not None and namespace_cudn != cudn:
                    return None, 'namespace %s already primary cudn enabled with %s' % (name, namespace_cudn)
            
        return namespaces, None
    

    def is_namespace_cudn_enabled(self, name=None, info=None, managed_object=None):
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

    def get_namespace_cudns(self, name, cache_enabled=True):
        cudns = self.get_cluster_user_defined_networks(nad_info=True, cache_enabled=cache_enabled)
        if cudns is None:
            return None
        
        namespace_cudns = []
        for cudn in cudns:
            if name not in cudn['namespace']:
                continue

            namespace_cudns.append(cudn['name'])
            
        return namespace_cudns

    def get_namespace_primary_cudn(self, name, cache_enabled=True):
        cudns = self.get_cluster_user_defined_networks(nad_info=True, cache_enabled=cache_enabled)
        if cudns is None:
            return None

        for cudn in cudns:
            if name not in cudn['namespace']:
                continue

            if cudn['primary']:
                return cudn['name']
            
        return None
    
    def is_namespace_primary_cudn_configured(self, name, cache_enabled=True):
        if self.get_namespace_primary_cudn(name, cache_enabled=cache_enabled) is None:
            return False
        return True
    