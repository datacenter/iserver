class K8sStorageMapInfo():
    def __init__(self):
        self.storage_map = None

    def get_storage_map_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

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
        
    def get_storage_maps(self, object_filter=None, plan_info=False, all_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'storage_map', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if return_mo:
            return infos
        
        if infos is None:
            return None

        plans = None
        if plan_info or all_info:
            plans = self.get_plans(cache_enabled=False)

        for info in infos:
            info = self.add_storage_map_info(
                info,
                plans=plans
            )

        return infos

    def is_storage_map(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_storage_map(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_storage_map(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'storage_map', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )