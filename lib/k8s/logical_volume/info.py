class K8sLogicalVolumeInfo():
    def __init__(self):
        self.logical_volume = None

    def get_logical_volume_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info['node_name'] = self.get(managed_object, 'spec:nodeName')
        info['device_class'] = self.get(managed_object, 'spec:deviceClass')
        info['requested_size'] = self.get(managed_object, 'spec:size')
        info['current_size'] = self.get(managed_object, 'status:currentSize')
        info['volume_id'] = self.get(managed_object, 'status:volumeID')

        return info

    def get_logical_volumes(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'logical_volume', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_logical_volume(self, name, cache_enabled=True, optimized=True):
        if self.get_logical_volume(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_logical_volume(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'logical_volume', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )