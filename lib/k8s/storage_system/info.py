import time
from lib import filter_helper


class K8sStorageSystemInfo():
    def __init__(self):
        self.storage_system = None

    def get_storage_system_info(self, storage_system_mo):
        if storage_system_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_system_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(storage_system_mo, 'spec')
        info['status'] = self.get(storage_system_mo, 'status')

        info['available'] = False
        conditions_mo = self.get(storage_system_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                type_mo = self.get(condition_mo, 'type')
                status_mo = self.get(condition_mo, 'status')
                if type_mo == 'Available':
                    if status_mo == 'True':
                        info['available'] = True
                        info['availableTick'] = '\u2713'
                        info['__Output']['availableTick'] = 'Green'
                    else:
                        info['available'] = False
                        info['availableTick'] = '\u2717'
                        info['__Output']['availableTick'] = 'Red'

        return info

    def get_storage_systems_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_system is not None:
                return self.storage_system

        managed_objects = self.get_storage_system_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_system = []
        for managed_object in managed_objects:
            storage_system_info = {}
            storage_system_info['info'] = self.get_storage_system_info(
                managed_object
            )
            storage_system_info['mo'] = managed_object
            self.storage_system.append(
                storage_system_info
            )

        return self.storage_system

    def match_storage_system(self, storage_system_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, storage_system_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, storage_system_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_storage_system',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_systems(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_storage_systems = self.get_storage_systems_info(cache_enabled=cache_enabled)
        if all_storage_systems is None:
            return None

        storage_systems = []

        for storage_system_info in all_storage_systems:
            if not self.match_storage_system(storage_system_info['info'], object_filter):
                continue

            if return_mo:
                storage_systems.append(
                    storage_system_info['mo']
                )
                continue

            storage_systems.append(
                storage_system_info['info']
            )

        return storage_systems

    def is_storage_system(self, namespace, name, cache_enabled=True):
        if self.get_storage_system(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_storage_system(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        storage_systems = self.get_storage_systems(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if storage_systems is None:
            return None

        if len(storage_systems) == 1:
            return storage_systems[0]

        return None

    def remove_storage_system_finalizers(self, namespace, name):
        storage_system_mo = self.get_storage_system(namespace, name, return_mo=True, cache_enabled=False)
        if storage_system_mo is None:
            return False
        
        if 'finalizers' not in storage_system_mo['metadata']:
            return True
        
        del storage_system_mo['metadata']['finalizers']

        return self.set_storage_system_mo(storage_system_mo)

    def delete_namespaced_storage_systems(self, namespace, my_output=None, wait=True, finalizers=False):
        if my_output is not None:
            my_output.default('Delete odf storage systems', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))

        items = self.get_storage_systems(
            object_filter=['namespace:%s' % (namespace)]
        )
        if items is None:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        for item in items:
            my_output.default('- %s' % (item['name']))
            success = self.delete_storage_system_mo(item['namespace'], item['name'])
            if not success:
                if my_output is not None:
                    my_output.error('REST API failed')

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no storage system...')

                if not self.wait_no_storage_system(item['namespace'], item['name']):
                    if my_output is not None:
                        my_output.error('Timed out')

                    if not finalizers:
                        return False
                    
                    if my_output is not None:
                        my_output.default('Remove finalizers')

                    if not self.remove_storage_system_finalizers(item['namespace'], item['name']):
                        if my_output is not None:
                            my_output.error('REST API failed')
                        return False
                    
                    if not self.wait_no_storage_system(item['namespace'], item['name']):
                        if my_output is not None:
                            my_output.error('Giving up')

                        return False

        return True

    def wait_no_storage_system(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_storage_system(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_storage_system',
                    'Max time reached'
                )
                return False

            time.sleep(5)
