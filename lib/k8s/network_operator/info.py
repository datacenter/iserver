class K8sNetworkOperatorInfo():
    def __init__(self):
        self.network_operator = None

    def get_network_operator_info(self, managed_object):
        info = self.get_base_info(managed_object, condition_map={})

        info['title'] = '%s %s' % (info['name'], self.get(info, 'status:version'))
        info['cni'] = self.get(managed_object, 'spec:defaultNetwork:type')
        info['cidrT'] = []
        for item in self.get(info, 'spec:clusterNetwork', on_error=[], on_none=[]):
            info['cidrT'].append('Pod %s/%s' % (item['cidr'], item['hostPrefix']))
        for item in self.get(info, 'spec:serviceNetwork', on_error=[], on_none=[]):
            info['cidrT'].append('Svc %s' % (item))
        info['settingsT'] = []

        keys = [
            'deployKubeProxy',
            'disableMultiNetwork',
            'disableNetworkDiagnostics',
            'logLevel',
            'managementState',
            'operatorLogLevel',
        ]
        for key in keys:
            value = self.get(managed_object, 'spec:%s' % (key))
            if value is not None:
                info['settingsT'].append('%s:%s' % (key, value))

        extras = []
        if 'FRR' in self.get(managed_object, 'spec:additionalRoutingCapabilities:providers', on_error=[], on_none=[]):
            extras.append('frr-k8s')

        if self.get(managed_object, 'spec:defaultNetwork:ovnKubernetesConfig:routeAdvertisements') == 'Enabled':
            extras.append('route advertisement')

        if len(extras) > 0:
            info['settingsT'].append('---')
            info['settingsT'] = info['settingsT'] + extras

        return info

    def get_network_operators(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'network_operator', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_network_operator(self, name, cache_enabled=True, optimized=True):
        if self.get_network_operator(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_network_operator(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'network_operator', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def get_cluster_network_operator(self, return_mo=False, cache_enabled=True):
        return self.get_network_operator(
            'cluster', 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
    
    def is_cluster_network_operator_progressing(self, cache_enabled=True):
        return self.get(
            self.get_cluster_network_operator(cache_enabled=cache_enabled),
            'Progressing'
        ) == 'True'
    
    def get_cluster_network_operator_type(self, cache_enabled=True):
        return self.get(
            self.get_cluster_network_operator(cache_enabled=cache_enabled), 
            'spec:defaultNetwork:type'
        )
    
    def is_cluster_network_operator_ovn(self, cache_enabled=True):
        return self.get_cluster_network_operator_type(cache_enabled=cache_enabled) == 'OVNKubernetes'

    def is_ovn_frr_enabled(self, cache_enabled=True):
        # "spec": {
        #     "additionalRoutingCapabilities": {
        #       "providers": ["FRR"]
        #     }
        # }
        managed_object = self.cleanup_managed_object(
            self.get_cluster_network_operator(return_mo=True, cache_enabled=cache_enabled)
        )
        providers_mo = self.get(managed_object, 'spec:additionalRoutingCapabilities:providers', on_error=[], on_none=[])
        return 'FRR' in providers_mo
    
    def is_ovn_frr_ra_enabled(self, cache_enabled=True):
        # "spec": {
        #     "defaultNetwork": {
        #         "ovnKubernetesConfig": {
        #             "routeAdvertisements": "Enabled"
        #         }
        #     }
        # }
        managed_object = self.cleanup_managed_object(
            self.get_cluster_network_operator(return_mo=True, cache_enabled=cache_enabled)
        )
        return self.get(managed_object, 'spec:defaultNetwork:ovnKubernetesConfig:routeAdvertisements') == 'Enabled'