import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sLocalVolumeInfo():
    def __init__(self):
        self.local_volume = None

    def get_local_volume_info(self, local_volume_mo):
        if local_volume_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            local_volume_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(local_volume_mo, 'spec')
        info['status'] = self.get(local_volume_mo, 'status')

        info['node'] = []
        terms_mo = self.get(local_volume_mo, 'spec:nodeSelector:nodeSelectorTerms', on_error=[], on_none=[])
        for term_mo in terms_mo:
            exprs_mo = self.get(term_mo, 'matchExpressions', on_error=[], on_none=[])
            for expr_mo in exprs_mo:
                key_mo = self.get(expr_mo, 'key')
                if key_mo == 'kubernetes.io/hostname':
                    values_mo = self.get(expr_mo, 'values', on_error=[], on_none=[])
                    for hostname in values_mo:
                        if hostname not in info['node']:
                            info['node'].append(hostname)

        info['device_path'] = []
        info['storage_class'] = []
        info['device'] = []
        info['mode'] = []

        devices_mo = self.get(local_volume_mo, 'spec:storageClassDevices')
        for device_mo in devices_mo:
            storage_class = self.get(device_mo, 'storageClassName')
            if storage_class not in info['storage_class']:
                info['storage_class'].append(
                    storage_class
                )

            volume_mode = self.get(device_mo, 'volumeMode')
            device_paths = self.get(device_mo, 'devicePaths')
            for device_path in device_paths:
                info['device_path'].append(
                    device_path.split('/')[-1]
                )

                device_info = {}
                device_info['path'] = device_path.split('/')[-1]
                device_info['sc'] = storage_class
                device_info['mode'] = volume_mode
                if volume_mode not in info['mode']:
                    info['mode'].append(
                        volume_mode
                    )

                info['device'].append(
                    device_info
                )

        return info

    def get_local_volumes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.local_volume is not None:
                return self.local_volume

        managed_objects = self.get_local_volume_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.local_volume = []
        for managed_object in managed_objects:
            local_volume_info = {}
            local_volume_info['info'] = self.get_local_volume_info(
                managed_object
            )
            local_volume_info['mo'] = managed_object
            self.local_volume.append(
                local_volume_info
            )

        return self.local_volume

    def match_local_volume(self, local_volume_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, local_volume_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, local_volume_info['name']):
                    return False

            if key == 'mode':
                key_found = True
                if value not in local_volume_info['mode']:
                    return False

            if key == 'node':
                key_found = True
                found = False
                for item in local_volume_info['node']:
                    if filter_helper.match_string(value, item):
                        found = True

                if not found:
                    return False

            if key == 'sc':
                key_found = True
                found = False
                for item in local_volume_info['storage_class']:
                    if filter_helper.match_string(value, item):
                        found = True

                if not found:
                    return False

            if key == 'device':
                key_found = True
                found = False
                for item in local_volume_info['device_path']:
                    if filter_helper.match_string(value, item):
                        found = True

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_local_volume',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_local_volumes(self, object_filter=None, pv_info=False, return_mo=False, cache_enabled=True):
        all_local_volumes = self.get_local_volumes_info(cache_enabled=cache_enabled)
        if all_local_volumes is None:
            return None

        local_volumes = []

        for local_volume_info in all_local_volumes:
            if not self.match_local_volume(local_volume_info['info'], object_filter):
                continue

            if return_mo:
                local_volumes.append(
                    local_volume_info['mo']
                )
                continue

            if pv_info:
                pvs = self.get_pvs(
                    object_filter=['local-volume:%s' % (local_volume_info['info']['name'])],
                    cache_enabled=cache_enabled
                )
                if pvs is not None and len(pvs) == 1:
                    local_volume_info['info']['pv'] = pvs[0]

            local_volumes.append(
                local_volume_info['info']
            )

        self.log.k8s_mo(
            'local_volume.info',
            local_volumes
        )

        return local_volumes
    
    def is_local_volume(self, namespace, name, cache_enabled=True):
        if self.get_local_volume(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_local_volume(self, namespace, name, pv_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        local_volumes = self.get_local_volumes(
            object_filter=object_filter,
            pv_info=pv_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if local_volumes is None:
            return None

        if len(local_volumes) == 1:
            return local_volumes[0]

        return None

    def get_local_volume_body(
            self, 
            namespace,
            name,
            node_names, 
            volume_mode,
            device_paths,
            storage_class,
            wipe=False
        ):
        body = {}
        body['apiVersion'] = 'local.storage.openshift.io/v1'
        body['kind'] = 'LocalVolume'
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

        body['spec']['storageClassDevices'] = []
        
        devices_mo = {}
        devices_mo['storageClassName'] = storage_class
        
        if volume_mode == 'block':
            devices_mo['volumeMode'] = 'Block'

        if volume_mode == 'fs':
            devices_mo['volumeMode'] = 'Filesystem'

        devices_mo['forceWipeDevicesAndDestroyAllData'] = wipe
        devices_mo['devicePaths'] = device_paths

        body['spec']['storageClassDevices'].append(devices_mo)
        return body

    def create_local_volume(
            self, 
            namespace, 
            name, 
            nodes, 
            volume_mode, 
            device_paths,
            storage_class_name,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Local Volume', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- nodes: %s' % (','.join(nodes)))
            my_output.default('- device paths: %s' % (','.join(device_paths)))
            my_output.default('- volume mode: %s' % (volume_mode))
            my_output.default('- storage class: %s' % (storage_class_name))

        if self.is_local_volume(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already defined')
            return True
        
        body = self.get_local_volume_body(
            namespace,
            name,
            nodes, 
            volume_mode,
            device_paths,
            storage_class_name
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
            my_output.default('- Local volume created', before_newline=True, after_newline=True)
    
        if wait:
            if my_output is not None:
                my_output.default('- wait for LocalVolume crd [timeout:60]...')
            
            success = self.wait_local_volume(
                namespace,
                name,
                max_time=60
            )
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
        
            if my_output is not None:
                my_output.default('- wait for persistent volume assiated with local volume %s [timeout:180]...' % (name))

            success = self.wait_pv_local_volume(
                name,
                expected=1,
                max_time=180
            )
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
                    
        return True

    def wait_local_volume(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            local_volume_info = self.get_local_volume(
                namespace,
                name,
                cache_enabled=False
            )
            if local_volume_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_local_volume',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_local_volume(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            local_volume_info = self.get_local_volume(
                namespace,
                name,
                cache_enabled=False
            )
            if local_volume_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_local_volume',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def delete_local_volumes(self, items, my_output=None, k8s_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Delete local volumes', before_newline=True, underline=True)

        if items is None:
            if my_output is not None:
                my_output.error('Failed to get local volumes')
            return False
            
        if len(items) == 0:
            if my_output is not None:
                my_output.default('No local volumes found')
            return True

        if k8s_output is not None:
            k8s_output.print_local_volumes(
                items
            )

            pvs = []
            for item in items:
                if 'pv' in item and item['pv'] is not None:
                    pvs.append(item['pv'])

            if len(pvs) > 0:
                if my_output is not None:
                    my_output.default(
                        'Associated Persistent Volumes', 
                        underline=True, 
                        before_newline=True,
                        after_newline=True
                    )

                k8s_output.print_pvs(pvs)

        if confirmation:
            if not get_confirmation():
                return False
            
        for item in items:
            if my_output is not None:
                my_output.default('- %s' % (item['namespace_name']))
            
            if not self.is_local_volume(item['namespace'], item['name'], cache_enabled=False):
                if my_output is not None:
                    my_output.default('\talready deleted')

                continue

            if not self.delete_local_volume_mo(item['namespace'], item['name']):
                if my_output is not None:
                    my_output.error('REST API failed')
                    
                return False
            
            if my_output is not None:
                my_output.default('\tREST API successful')
            
            if wait:
                if my_output is not None:
                    my_output.default('\tWait for no local volume [timeout:60]...')

                if not self.wait_no_local_volume(item['namespace'], item['name'], max_time=60):
                    if my_output is not None:
                        my_output.error('Timed out waiting for no local volume')

                    return False
                    
        return True
