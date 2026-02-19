from lib import filter_helper


class K8sVolumeImportSourceInfo():
    def __init__(self):
        self.volume_import_source = None

    def get_volume_import_source_info(self, volume_import_source_mo):
        if volume_import_source_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            volume_import_source_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(volume_import_source_mo, 'spec')
        info['status'] = self.get(volume_import_source_mo, 'status')
        return info

    def get_volume_import_sources_info(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_import_source is not None:
                return self.volume_import_source

        managed_objects = self.get_volume_import_source_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.volume_import_source = []
        for managed_object in managed_objects:
            volume_import_source_info = {}
            volume_import_source_info['info'] = self.get_volume_import_source_info(
                managed_object
            )
            volume_import_source_info['mo'] = managed_object
            self.volume_import_source.append(
                volume_import_source_info
            )

        return self.volume_import_source

    def match_volume_import_source(self, volume_import_source_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, volume_import_source_info['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, volume_import_source_info['namespace']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_volume_import_source',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_volume_import_sources(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_volume_import_sources = self.get_volume_import_sources_info(cache_enabled=cache_enabled)
        if all_volume_import_sources is None:
            return None

        volume_import_sources = []

        for volume_import_source_info in all_volume_import_sources:
            if not self.match_volume_import_source(volume_import_source_info['info'], object_filter):
                continue

            if return_mo:
                volume_import_sources.append(
                    volume_import_source_info['mo']
                )
                continue

            volume_import_sources.append(
                volume_import_source_info['info']
            )

        return volume_import_sources

    def is_volume_import_source(self, namespace, name, cache_enabled=True):
        if self.get_volume_import_source(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_volume_import_source(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        volume_import_sources = self.get_volume_import_sources(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if volume_import_sources is None:
            return None

        if len(volume_import_sources) == 1:
            return volume_import_sources[0]

        return None
