from lib import filter_helper


class K8sStorageMapInfo():
    def __init__(self):
        self.storage_map = None

    def get_storage_map_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['source_provider'] = self.get(managed_object, 'spec:provider:source:name')
        info['destination_provider'] = self.get(managed_object, 'spec:provider:destination:name')
        info['provider'] = [
            info['source_provider'],
            info['destination_provider']
        ]
        
        maps_mo = self.get(managed_object, 'spec:map', on_error=[], on_none=[])
        references_mo = self.get(managed_object, 'status:references', on_error=[], on_none=[])

        info['map'] = []
        for map_mo in maps_mo:
            item = {}
            item['source'] = None
            item['destination'] = None

            if 'storageClass' in map_mo['source']:
                item['source'] = map_mo['source']['storageClass']

            if 'name' in map_mo['source']:
                item['source'] = map_mo['source']['name']

            if 'storageClass' in map_mo['destination']:
                item['destination'] = map_mo['destination']['storageClass']

            if 'name' in map_mo['destination']:
                item['destination'] = map_mo['destination']['name']

            if 'id' in map_mo['source']:
                for reference_mo in references_mo:
                    if reference_mo['id'] == map_mo['source']['id']:
                        item['source'] = '%s [%s]' % (
                            reference_mo['name'],
                            reference_mo['id']
                        )

            if 'id' in map_mo['destination']:
                for reference_mo in references_mo:
                    if reference_mo['id'] == map_mo['destination']['id']:
                        item['destination'] = '%s [%s]' % (
                            reference_mo['name'],
                            reference_mo['id']
                        )

            info['map'].append(item)
            
        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'

        info['status'] = 'Not ready'
        info['__Output']['status'] = 'Red'

        if 'Ready' in info['conditions']:
            info['ready'] = True 
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'

            info['status'] = 'Ready'
            info['__Output']['status'] = 'Green'

        info['invalid'] = False
        if 'DestinationStorageNotValid' in info['conditions']:
            info['invalid'] = True

        if 'SourceStorageNotValid'  in info['conditions']:
            info['invalid'] = True

        return info

    def add_storage_map_info(self, info, plans=None):
        if plans is not None:
            info['plan'] = []

            for plan in plans:
                if plan['storage_map_namespace'] != info['namespace']:
                    continue

                if plan['storage_map_name'] != info['name']:
                    continue

                info['plan'].append(
                    plan['name']
                )

        return info
        
    def get_storage_maps_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_map is not None:
                return self.storage_map

        managed_objects = self.get_storage_map_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_map = []
        for managed_object in managed_objects:
            storage_map_info = {}
            storage_map_info['info'] = self.get_storage_map_info(
                managed_object
            )
            storage_map_info['mo'] = managed_object
            self.storage_map.append(
                storage_map_info
            )

        return self.storage_map

    def match_storage_map(self, storage_map_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, storage_map_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (storage_map_info['namespace'], storage_map_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_storage_map',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_maps(self, object_filter=None, plan_info=False, return_mo=False, cache_enabled=True):
        all_storage_maps = self.get_storage_maps_info(cache_enabled=cache_enabled)
        if all_storage_maps is None:
            return None

        storage_maps = []

        plans = None
        if plan_info:
            plans = self.get_plans(cache_enabled=False)

        for storage_map_info in all_storage_maps:
            storage_map_info['info'] = self.add_storage_map_info(
                storage_map_info['info'],
                plans=plans
            )

            if not self.match_storage_map(storage_map_info['info'], object_filter):
                continue

            if return_mo:
                storage_maps.append(
                    storage_map_info['mo']
                )
                continue

            storage_maps.append(
                storage_map_info['info']
            )

        return storage_maps

    def is_storage_map(self, namespace, name, cache_enabled=True):
        if self.get_storage_map(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_storage_map(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        storage_maps = self.get_storage_maps(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if storage_maps is None:
            return None

        if len(storage_maps) == 1:
            return storage_maps[0]

        return None
