class K8sFrrNodeStateInfo():
    def __init__(self):
        self.frr_node_state = None

    def get_frr_node_state_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['last_conversion'] = self.get(managed_object, 'status:lastConversionResult')
        info = self.add_tick(info, 'last_conversion', 'success', 'last_conversionT', bool_attribute='converted')
        info['last_reload'] = self.get(managed_object, 'status:lastReloadResult')
        info = self.add_tick(info, 'last_reload', 'success', 'last_reloadT', bool_attribute='reloaded')

        return info

    def get_frr_node_states(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'frr_node_state', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos
