import yaml


class K8sVastDriverInfo():
    def __init__(self):
        self.vast_driver = None

    def get_vast_managed_object_info(self, managed_object):
        if managed_object is None:
            return None

        condition_map = {}
        condition_map['initialized'] = 'Initialized'
        condition_map['deployed'] = 'Deployed'
        condition_map['failed'] = 'ReleaseFailed'

        info = self.get_base_info(
            managed_object,
            condition_map=condition_map
        )

        info['manifest'] = self.get(managed_object, 'status:deployedRelease:manifest')
        info['resource'] = []
        if info['manifest'] is not None:
            for manifest in info['manifest'].split('---'):
                content = yaml.safe_load(manifest)
                resource = {}
                resource['kind'] = self.get(content, 'kind')
                if resource['kind'] is None:
                    continue

                resource['namespace'] = self.get(content, 'metadata:namespace')
                resource['name'] = self.get(content, 'metadata:name')
                if resource['namespace'] is None:
                    resource['description'] = '[%s] %s' % (
                        resource['kind'],
                        resource['name']
                    )
                else:
                    resource['description'] = '[%s] %s/%s' % (
                        resource['kind'],
                        resource['namespace'],
                        resource['name']
                    )
                info['resource'].append(resource)

        info['resource'] = sorted(
            info['resource'],
            key=lambda i: (
                i['kind'],
                i['name']
            )
        )
        return info

    def get_vast_driver_info(self, managed_object):
        return self.get_vast_managed_object_info(managed_object)

    def get_vast_drivers(self, object_filter=None, storage_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'vast_driver', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if return_mo:
            return infos
        
        if storage_info:
            for item in infos:
                item['storage'] = []

            storages = self.get_vast_storages(cache_enabled=cache_enabled)
            if storages is not None:
                for storage in storages:
                    for item in infos:
                        if self.get(storage, 'spec:provisioner') == item['name']:
                            item['storage'].append(storage['name'])

        return infos
    
    def is_vast_driver(self, namespace, name, cache_enabled=True):
        if self.get_vast_driver(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_vast_driver(self, namespace, name, storage_info=False, return_mo=False, cache_enabled=True):
        return self.get_info(
            'vast_driver', 
            name,
            namespace=namespace,
            storage_info=storage_info,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
    