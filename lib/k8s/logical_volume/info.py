from lib import filter_helper


class K8sLogicalVolumeInfo():
    def __init__(self):
        self.logical_volume = None

    def get_logical_volume_info(self, logical_volume_mo):
        if logical_volume_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            logical_volume_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(logical_volume_mo, 'spec')
        info['status'] = self.get(logical_volume_mo, 'status')

        info['info'] = {}
        info['info']['node_name'] = self.get(logical_volume_mo, 'spec:nodeName')
        info['info']['device_class'] = self.get(logical_volume_mo, 'spec:deviceClass')
        info['info']['requested_size'] = self.get(logical_volume_mo, 'spec:size')
        info['info']['current_size'] = self.get(logical_volume_mo, 'status:currentSize')
        info['info']['volume_id'] = self.get(logical_volume_mo, 'status:volumeID')

        return info

    def get_logical_volumes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.logical_volume is not None:
                return self.logical_volume

        managed_objects = self.get_logical_volume_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.logical_volume = []
        for managed_object in managed_objects:
            logical_volume_info = {}
            logical_volume_info['info'] = self.get_logical_volume_info(
                managed_object
            )
            logical_volume_info['mo'] = managed_object
            self.logical_volume.append(
                logical_volume_info
            )

        return self.logical_volume

    def match_logical_volume(self, logical_volume_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, logical_volume_info['name']):
                    return False

            if key == 'names':
                key_found = True
                found = False
                for item in value.split(','):
                    if filter_helper.match_string(item, logical_volume_info['name']):
                        found = True
                        break

                if not found:
                    return False
                
            if not key_found:
                self.log.error(
                    'match_logical_volume',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_logical_volumes(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_logical_volumes = self.get_logical_volumes_info(cache_enabled=cache_enabled)
        if all_logical_volumes is None:
            return None

        logical_volumes = []

        for logical_volume_info in all_logical_volumes:
            if not self.match_logical_volume(logical_volume_info['info'], object_filter):
                continue

            if return_mo:
                logical_volumes.append(
                    logical_volume_info['mo']
                )
                continue

            logical_volumes.append(
                logical_volume_info['info']
            )

        return logical_volumes

    def is_logical_volume(self, name, cache_enabled=True):
        if self.get_logical_volume(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_logical_volume(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        logical_volumes = self.get_logical_volumes(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if logical_volumes is None:
            return None

        if len(logical_volumes) == 1:
            return logical_volumes[0]

        return None
