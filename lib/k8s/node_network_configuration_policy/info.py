from lib import filter_helper


class K8sNodeNetworkConfigurationPolicyInfo():
    def __init__(self):
        self.node_network_configuration_policy = None

    def get_node_network_configuration_policy_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        conditions_mo = self.get(managed_object, 'status:conditions')

        info['status'] = None
        info['reason'] = None
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                if condition_mo['status'] == 'True':
                    info['status'] = condition_mo['type']
                    info['reason'] = condition_mo['reason']

        info['available'] = False
        info['degraded'] = False
        info['progressing'] = False

        if info['status'] is not None:
            if info['status'] == 'Available':
                info['available'] = True

            if info['status'] == 'Degraded':
                info['degraded'] = True

            if info['status'] == 'Progressing':
                info['progressing'] = True

        if info['status'] is None:
            info['status'] = 'Unknown'
            info['reason'] = 'N/A'

        return info

    def get_node_network_configuration_policys(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'node_network_configuration_policy', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if return_mo:
            return infos
        
        return infos
    
    def is_node_network_configuration_policy(self, name, cache_enabled=True):
        if self.get_node_network_configuration_policy(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_node_network_configuration_policy(self, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'node_network_configuration_policy', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
