from lib import filter_helper


class K8sVolumeCloneSourceInfo():
    def __init__(self):
        self.volume_clone_source = None

    def get_volume_clone_source_info(self, volume_clone_source_mo):
        if volume_clone_source_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            volume_clone_source_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(volume_clone_source_mo, 'spec')
        info['status'] = self.get(volume_clone_source_mo, 'status')
        return info

    def get_volume_clone_sources_info(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_clone_source is not None:
                return self.volume_clone_source

        managed_objects = self.get_volume_clone_source_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.volume_clone_source = []
        for managed_object in managed_objects:
            volume_clone_source_info = {}
            volume_clone_source_info['info'] = self.get_volume_clone_source_info(
                managed_object
            )
            volume_clone_source_info['mo'] = managed_object
            self.volume_clone_source.append(
                volume_clone_source_info
            )

        return self.volume_clone_source

    def match_volume_clone_source(self, volume_clone_source_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, volume_clone_source_info['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, volume_clone_source_info['namespace']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_volume_clone_source',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_volume_clone_sources(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_volume_clone_sources = self.get_volume_clone_sources_info(cache_enabled=cache_enabled)
        if all_volume_clone_sources is None:
            return None

        volume_clone_sources = []

        for volume_clone_source_info in all_volume_clone_sources:
            if not self.match_volume_clone_source(volume_clone_source_info['info'], object_filter):
                continue

            if return_mo:
                volume_clone_sources.append(
                    volume_clone_source_info['mo']
                )
                continue

            volume_clone_sources.append(
                volume_clone_source_info['info']
            )

        return volume_clone_sources

    def is_volume_clone_source(self, namespace, name, cache_enabled=True):
        if self.get_volume_clone_source(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_volume_clone_source(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        volume_clone_sources = self.get_volume_clone_sources(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if volume_clone_sources is None:
            return None

        if len(volume_clone_sources) == 1:
            return volume_clone_sources[0]

        return None
