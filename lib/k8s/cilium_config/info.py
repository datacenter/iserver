class K8sCiliumConfigInfo():
    def __init__(self):
        self.cilium_config = None

    def get_cilium_config_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        
        info['values_error'] = True
        info['values_error_reason'] = None
        info['values_error_message'] = None
        info['processing_error'] = True
        info['processing_error_reason'] = None
        info['processing_error_message'] = None

        conditions_mo = self.get(managed_object, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                condition_type = self.get(condition_mo, 'type')
                if condition_type is not None:
                    if condition_type == 'ValuesError':
                        if self.get(condition_mo, 'status') == 'False':
                            info['values_error'] = False
                        if self.get(condition_mo, 'status') == 'True':
                            info['values_error_reason'] = self.get(condition_mo, 'reason')
                            info['values_error_message'] = self.get(condition_mo, 'message')

                    if condition_type == 'ProcessingError':
                        if self.get(condition_mo, 'status') == 'False':
                            info['processing_error'] = False
                        if self.get(condition_mo, 'status') == 'True':
                            info['processing_error_reason'] = self.get(condition_mo, 'reason')
                            info['processing_error_message'] = self.get(condition_mo, 'message')

        info['valid'] = not info['values_error'] and not info['processing_error']
        return info

    def get_cilium_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cilium_config', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_cilium_config(self, name=None, cache_enabled=True, optimized=True):
        if self.get_cilium_config(name=name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        
        return True

    def get_cilium_config(self, name=None, return_mo=False, cache_enabled=True, optimized=True):
        if name is not None:
            return self.get_info(
                'cluster_role', 
                name,
                return_mo=return_mo, 
                cache_enabled=cache_enabled,
                optimized=optimized
            )
    
        infos = self.get_infos(
            'cilium_config', 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if infos is None:
            return None
        
        if len(infos) == 1:
            return infos[0]

        return None
