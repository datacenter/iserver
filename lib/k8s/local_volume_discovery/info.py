import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sLocalVolumeDiscoveryInfo():
    def __init__(self):
        self.local_volume_discovery = None

    def get_local_volume_discovery_info(self, local_volume_discovery_mo):
        if local_volume_discovery_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            local_volume_discovery_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(local_volume_discovery_mo, 'spec')
        info['status'] = self.get(local_volume_discovery_mo, 'status')

        info['phase'] = self.get(local_volume_discovery_mo, 'status:phase')
        info['available'] = False

        conditions_mo = self.get(local_volume_discovery_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                condition_type = self.get(condition_mo, 'type')
                if condition_type == 'Available':
                    condition_status = self.get(condition_mo, 'status')
                    if condition_status == 'True':
                        info['available'] = True
        
        if info['available']:
            info['availableT'] = '\u2713'
            info['__Output']['availableT'] = 'Green'
        else:
            info['availableT'] = '\u2717'
            info['__Output']['availableT'] = 'Red'

        return info

    def get_local_volume_discoveries_info(self, cache_enabled=True):
        if cache_enabled:
            if self.local_volume_discovery is not None:
                return self.local_volume_discovery

        managed_objects = self.get_local_volume_discovery_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.local_volume_discovery = []
        for managed_object in managed_objects:
            local_volume_discovery_info = {}
            local_volume_discovery_info['info'] = self.get_local_volume_discovery_info(
                managed_object
            )
            local_volume_discovery_info['mo'] = managed_object
            self.local_volume_discovery.append(
                local_volume_discovery_info
            )

        return self.local_volume_discovery

    def match_local_volume_discovery(self, local_volume_discovery_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, local_volume_discovery_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, local_volume_discovery_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_local_volume_discovery',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_local_volume_discoveries(self, object_filter=None, results_info=False, return_mo=False, cache_enabled=True):
        all_local_volume_discoveries = self.get_local_volume_discoveries_info(cache_enabled=cache_enabled)
        if all_local_volume_discoveries is None:
            return None

        local_volume_discoveries = []

        for local_volume_discovery_info in all_local_volume_discoveries:
            if not self.match_local_volume_discovery(local_volume_discovery_info['info'], object_filter):
                continue

            if return_mo:
                local_volume_discoveries.append(
                    local_volume_discovery_info['mo']
                )
                continue

            local_volume_discoveries.append(
                local_volume_discovery_info['info']
            )

        return local_volume_discoveries

    def is_local_volume_discovery(self, namespace, name, cache_enabled=True):
        if self.get_local_volume_discovery(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_local_volume_discovery(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        local_volume_discoveries = self.get_local_volume_discoveries(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if local_volume_discoveries is None:
            return None

        if len(local_volume_discoveries) == 1:
            return local_volume_discoveries[0]

        return None

    def get_local_volume_discovery_body(
            self, 
            node_names, 
            name='auto-discover-devices', 
            namespace='openshift-local-storage',
            tolerations=False
        ):
        body = {}
        body['apiVersion'] = 'local.storage.openshift.io/v1alpha1'
        body['kind'] = 'LocalVolumeDiscovery'
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

        if tolerations:
            toleration_mo = {}
            toleration_mo['effect'] = 'NoSchedule'
            toleration_mo['key'] = 'cluster.ocs.openshift.io/openshift-storage'
            toleration_mo['operator'] = 'Equal'
            toleration_mo['value'] = ''
            body['spec']['tolerations'] = [toleration_mo]

        return body

    def create_local_volume_discovery(self, namespace, name, nodes, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Local Volume Discovery', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- nodes: %s' % (','.join(nodes)))

        if self.is_local_volume_discovery(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already defined')
            return True
        
        body = self.get_local_volume_discovery_body(
            nodes,
            name=name, 
            namespace=namespace
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_local_volume_discovery_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('- Local volume discover created', before_newline=True, after_newline=True)
    
        if wait:
            if my_output is not None:
                my_output.default('- wait for LocalVolumeDiscovery crd [timeout:60]...')
            
            success = self.wait_local_volume_discovery(
                namespace,
                name,
                max_time=60
            )
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
        
            if my_output is not None:
                my_output.default('- wait for LocalVolumeDiscoveryResult crd [timeout:360]...')

            for node_name in nodes:
                if my_output is not None:
                    my_output.default('\t%s' % (node_name))

                success = self.wait_local_volume_discovery_result(
                    node_name,
                    max_time=360
                )
                if not success:
                    if my_output is not None:
                        my_output.error('Timed out')
                    return False
        
        return True

    def wait_local_volume_discovery(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            local_volume_discovery_info = self.get_local_volume_discovery(
                namespace,
                name,
                cache_enabled=False
            )
            if local_volume_discovery_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_local_volume_discovery',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_local_volume_discovery(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            local_volume_discovery_info = self.get_local_volume_discovery(
                namespace,
                name,
                cache_enabled=False
            )
            if local_volume_discovery_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_local_volume_discovery',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def delete_local_volume_discoveries(self, items, my_output=None, k8s_output=None, confirmation=False, wait=True):
        if my_output is not None:
            my_output.default('Delete local volume discovieries', before_newline=True, underline=True)

        if items is None:
            if my_output is not None:
                my_output.error('Failed to get local volume discover')
                return False
            
        if len(items) == 0:
            if my_output is not None:
                my_output.default('No local volume discover found')
            return True

        if k8s_output is not None:
            k8s_output.print_local_volume_discoveries(
                items,
                title=True
            )

        if confirmation:
            if not get_confirmation():
                return False
            
        for item in items:
            if my_output is not None:
                my_output.default('- %s' % (item['namespace_name']))
            
            if not self.is_local_volume_discovery(item['namespace'], item['name'], cache_enabled=False):
                if my_output is not None:
                    my_output.default('\talready deleted')
                    continue

            if not self.delete_local_volume_discovery_mo(item['namespace'], item['name']):
                if my_output is not None:
                    my_output.error('REST API failed')
                    return False
            
            if my_output is not None:
                my_output.default('\tREST API successful')
            
            if wait:
                if my_output is not None:
                    my_output.default('\tWait for no local volume discovery [timeout:60]...')

                if not self.wait_no_local_volume_discovery(item['namespace'], item['name'], max_time=60):
                    if my_output is not None:
                        my_output.error('Timed out waiting for no local volume discovery')
                        return False
                    
        return True
