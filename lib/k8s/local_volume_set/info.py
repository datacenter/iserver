import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sLocalVolumeSetInfo():
    def __init__(self):
        self.local_volume_set = None

    def get_local_volume_set_info(self, local_volume_set_mo):
        if local_volume_set_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            local_volume_set_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(local_volume_set_mo, 'spec')
        info['status'] = self.get(local_volume_set_mo, 'status')

        info['volume_mode'] = self.get(local_volume_set_mo, 'spec:volumeMode')
        info['storage_class'] = self.get(local_volume_set_mo, 'spec:storageClassName')
        info['device_count'] = self.get(local_volume_set_mo, 'status:totalProvisionedDeviceCount')
        info['available'] = False
        info['dm_available'] = False

        conditions_mo = self.get(local_volume_set_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                condition_type = self.get(condition_mo, 'type')
                if condition_type == 'Available':
                    condition_status = self.get(condition_mo, 'status')
                    if condition_status == 'True':
                        info['available'] = True

                if condition_type == 'DaemonSetsAvailable':
                    condition_status = self.get(condition_mo, 'status')
                    if condition_status == 'True':
                        info['dm_available'] = True

        if info['available']:
            info['availableT'] = '\u2713'
            info['__Output']['availableT'] = 'Green'
        else:
            info['availableT'] = '\u2717'
            info['__Output']['availableT'] = 'Red'

        if info['dm_available']:
            info['dm_availableT'] = '\u2713'
            info['__Output']['dm_availableT'] = 'Green'
        else:
            info['dm_availableT'] = '\u2717'
            info['__Output']['dm_availableT'] = 'Red'

        info['ready'] = info['available'] and info['dm_available']
        return info

    def get_local_volume_sets_info(self, cache_enabled=True):
        if cache_enabled:
            if self.local_volume_set is not None:
                return self.local_volume_set

        managed_objects = self.get_local_volume_set_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.local_volume_set = []
        for managed_object in managed_objects:
            local_volume_set_info = {}
            local_volume_set_info['info'] = self.get_local_volume_set_info(
                managed_object
            )
            local_volume_set_info['mo'] = managed_object
            self.local_volume_set.append(
                local_volume_set_info
            )

        return self.local_volume_set

    def match_local_volume_set(self, local_volume_set_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, local_volume_set_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, local_volume_set_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_local_volume_set',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_local_volume_sets(self, object_filter=None, pv_info=False, return_mo=False, cache_enabled=True):
        all_local_volume_sets = self.get_local_volume_sets_info(cache_enabled=cache_enabled)
        if all_local_volume_sets is None:
            return None

        local_volume_sets = []

        for local_volume_set_info in all_local_volume_sets:
            if not self.match_local_volume_set(local_volume_set_info['info'], object_filter):
                continue

            if return_mo:
                local_volume_sets.append(
                    local_volume_set_info['mo']
                )
                continue

            if pv_info:
                local_volume_set_info['info']['pv'] = self.get_pvs(
                    object_filter=['sc:%s' % (local_volume_set_info['info']['storage_class'])],
                    cache_enabled=cache_enabled
                )
                
            local_volume_sets.append(
                local_volume_set_info['info']
            )

        return local_volume_sets

    def is_any_local_volume_set(self, cache_enabled=True):
        lvs = self.get_local_volume_sets(cache_enabled=cache_enabled)
        if lvs is None or len(lvs) == 0:
            return False
        return True

    def is_local_volume_set(self, namespace, name, cache_enabled=True):
        if self.get_local_volume_set(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_local_volume_set(self, namespace, name, pv_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        local_volume_sets = self.get_local_volume_sets(
            object_filter=object_filter,
            pv_info=pv_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if local_volume_sets is None:
            return None

        if len(local_volume_sets) == 1:
            return local_volume_sets[0]

        return None

    def get_local_volume_set_body(
            self, 
            namespace,
            name,
            node_names, 
            volume_mode,
            storage_class,
            limits=[],
            max_count=-1,
            fstype='ext4'
        ):
        body = {}
        body['apiVersion'] = 'local.storage.openshift.io/v1alpha1'
        body['kind'] = 'LocalVolumeSet'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['nodeSelector'] = {}

        expr_mo = {}
        expr_mo['key'] = 'kubernetes.io/hostname'
        expr_mo['operator'] = 'In'
        expr_mo['values'] = node_names
        body['spec']['nodeSelector']['nodeSelectorTerms'] = [dict(matchExpressions=[expr_mo])]

        body['spec']['storageClassName'] = storage_class

        if volume_mode == 'block':
            body['spec']['volumeMode'] = 'Block'

        if volume_mode == 'fs':
            body['spec']['volumeMode'] = 'Filesystem'

        if volume_mode == 'fs':
            body['spec']['fsType'] = fstype
  
        if max_count > 0:
            body['spec']['maxDeviceCount'] = max_count

        if len(limits) > 0:
            body['spec']['deviceInclusionSpec'] = {}

        for item in limits:
            key = item.split(':')[0]
            value = item.split(':')[1]

            if key == 'type':
                if 'deviceTypes' not in body['spec']['deviceInclusionSpec']:
                    body['spec']['deviceInclusionSpec']['deviceTypes'] = []

                body['spec']['deviceInclusionSpec']['deviceTypes'].append(
                    value
                )

            if key == 'mechanical':
                if 'deviceMechanicalProperties' not in body['spec']['deviceInclusionSpec']:
                    body['spec']['deviceInclusionSpec']['deviceMechanicalProperties'] = []

                if value == 'rotational':
                    body['spec']['deviceInclusionSpec']['deviceTypes'].append(
                        'Rotational'
                    )
                if value == 'nonrotational':
                    body['spec']['deviceInclusionSpec']['deviceTypes'].append(
                        'NonRotational'
                    )

            if key == 'minsize':
                body['spec']['deviceInclusionSpec']['minSize'] = value
                
            if key == 'maxsize':
                body['spec']['deviceInclusionSpec']['maxSize'] = value

            if key == 'model':
                if 'models' not in body['spec']['deviceInclusionSpec']:
                    body['spec']['deviceInclusionSpec']['models'] = []

                body['spec']['deviceInclusionSpec']['models'].append(
                    value
                )

            if key == 'vendor':
                if 'vendors' not in body['spec']['deviceInclusionSpec']:
                    body['spec']['deviceInclusionSpec']['vendors'] = []

                body['spec']['deviceInclusionSpec']['vendors'].append(
                    value
                )

        return body

    def create_local_volume_set(
            self, 
            namespace, 
            name, 
            nodes, 
            volume_mode, 
            storage_class_name, 
            limits=[],
            max_count=-1,
            fstype='ext4',
            expected_outcome=None,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Local Volume Set', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- nodes: %s' % (','.join(nodes)))

        if self.is_local_volume_set(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already defined')
            return True
        
        body = self.get_local_volume_set_body(
            namespace,
            name,
            nodes,
            volume_mode,
            storage_class_name,
            limits=limits,
            max_count=max_count,
            fstype=fstype,
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_resource(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('- Local volume set created', before_newline=True, after_newline=True)
    
        if wait:
            if my_output is not None:
                my_output.default('- wait for LocalVolumeSet crd [timeout:60]...')
            
            success = self.wait_local_volume_set(
                namespace,
                name,
                max_time=60
            )
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
        
            if my_output is not None:
                my_output.default('- wait for LocalVolumeSet ready [timeout:360]...')

            success = self.wait_local_volume_set_ready(
                namespace,
                name,
                max_time=360
            )
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
        
            if expected_outcome is not None:
                if my_output is not None:
                    my_output.default('- wait for all devices to be provisioned [timeout:360]...')

                success = self.wait_local_volume_set_devices(
                    namespace,
                    name,
                    expected_outcome,
                    max_time=360
                )
                if not success:
                    if my_output is not None:
                        my_output.error('Timed out')
                    return False
                    
        return True

    def wait_local_volume_set(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            local_volume_set_info = self.get_local_volume_set(
                namespace,
                name,
                cache_enabled=False
            )
            if local_volume_set_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_local_volume_set',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_local_volume_set_ready(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            local_volume_set_info = self.get_local_volume_set(
                namespace,
                name,
                cache_enabled=False
            )
            if local_volume_set_info is not None:
                if local_volume_set_info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_local_volume_set_ready',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_local_volume_set_devices(self, namespace, name, device_count, max_time=60):
        start_time = int(time.time())
        while True:
            local_volume_set_info = self.get_local_volume_set(
                namespace,
                name,
                cache_enabled=False
            )
            if local_volume_set_info is not None:
                if local_volume_set_info['ready']:
                    if local_volume_set_info['device_count'] is not None:
                        if local_volume_set_info['device_count'] == device_count:
                            return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_local_volume_set_ready',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_local_volume_set(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            local_volume_set_info = self.get_local_volume_set(
                namespace,
                name,
                cache_enabled=False
            )
            if local_volume_set_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_local_volume_set',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def delete_local_volume_sets(self, items, my_output=None, k8s_output=None, confirmation=False, wait=True):
        if my_output is not None:
            my_output.default('Delete local volume sets', before_newline=True, underline=True)

        if items is None:
            if my_output is not None:
                my_output.error('Failed to get local volume sets')
                return False
            
        if len(items) == 0:
            if my_output is not None:
                my_output.default('No local volume set found')
            return True

        if k8s_output is not None:
            k8s_output.print_local_volume_sets(
                items
            )

        if confirmation:
            if not get_confirmation():
                return False
            
        for item in items:
            if my_output is not None:
                my_output.default('- %s' % (item['namespace_name']))
            
            if not self.is_local_volume_set(item['namespace'], item['name'], cache_enabled=False):
                if my_output is not None:
                    my_output.default('\talready deleted')
                    continue

            if not self.delete_local_volume_set_mo(item['namespace'], item['name']):
                if my_output is not None:
                    my_output.error('REST API failed')
                    return False
            
            if my_output is not None:
                my_output.default('\tREST API successful')
            
            if wait:
                if my_output is not None:
                    my_output.default('\tWait for no local volume set [timeout:60]...')

                if not self.wait_no_local_volume_set(item['namespace'], item['name'], max_time=60):
                    if my_output is not None:
                        my_output.error('Timed out waiting for no local volume set')
                        return False
                    
        return True
