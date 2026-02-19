import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sTetragonNetworkPolicyNamespacedInfo():
    def __init__(self):
        self.tetragon_network_policy_namespaced = None

    def get_tetragon_network_policy_namespaced_info(self, tetragon_network_policy_namespaced_mo):
        if tetragon_network_policy_namespaced_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            tetragon_network_policy_namespaced_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(tetragon_network_policy_namespaced_mo, 'spec')
        return info

    def get_tetragon_network_policies_namespaced_info(self, cache_enabled=True):
        if cache_enabled:
            if self.tetragon_network_policy_namespaced is not None:
                return self.tetragon_network_policy_namespaced

        managed_objects = self.get_tetragon_network_policy_namespaced_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.tetragon_network_policy_namespaced = []
        for managed_object in managed_objects:
            tetragon_network_policy_namespaced_info = {}
            tetragon_network_policy_namespaced_info['info'] = self.get_tetragon_network_policy_namespaced_info(
                managed_object
            )
            tetragon_network_policy_namespaced_info['mo'] = managed_object
            self.tetragon_network_policy_namespaced.append(
                tetragon_network_policy_namespaced_info
            )

        return self.tetragon_network_policy_namespaced

    def match_tetragon_network_policy_namespaced(self, tetragon_network_policy_namespaced_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, tetragon_network_policy_namespaced_info['namespace']):
                    return False
                
            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, tetragon_network_policy_namespaced_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_tetragon_network_policy_namespaced',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_tetragon_network_policies_namespaced(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_tetragon_network_policies_namespaced = self.get_tetragon_network_policies_namespaced_info(cache_enabled=cache_enabled)
        if all_tetragon_network_policies_namespaced is None:
            return None

        tetragon_network_policies_namespaced = []

        for tetragon_network_policy_namespaced_info in all_tetragon_network_policies_namespaced:
            if not self.match_tetragon_network_policy_namespaced(tetragon_network_policy_namespaced_info['info'], object_filter):
                continue

            if return_mo:
                tetragon_network_policies_namespaced.append(
                    tetragon_network_policy_namespaced_info['mo']
                )
                continue

            tetragon_network_policies_namespaced.append(
                tetragon_network_policy_namespaced_info['info']
            )

        return tetragon_network_policies_namespaced

    def is_tetragon_network_policy_namespaced(self, namespace, name, cache_enabled=True):
        if self.get_tetragon_network_policy_namespaced(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_tetragon_network_policy_namespaced(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        tetragon_network_policies_namespaced = self.get_tetragon_network_policies_namespaced(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if tetragon_network_policies_namespaced is None:
            return None

        if len(tetragon_network_policies_namespaced) == 1:
            return tetragon_network_policies_namespaced[0]

        return None

    def create_tetragon_network_policy_namespaced(self, body, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Tetragon Network Policy Namespaced', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (body['metadata']['namespace']))
            my_output.default('- name: %s' % (body['metadata']['name']))

        if self.is_tetragon_network_policy_namespaced(body['metadata']['namespace'], body['metadata']['name']):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        if confirmation:
            if my_output is not None:
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

            if not get_confirmation():
                return False

        if not self.create_tetragon_network_policy_namespaced_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Tetragon Network policy namespaced created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for tetragon network policy namespaced [timeout:60]...')

            if not self.wait_tetragon_network_policy_namespaced(body['metadata']['namespace'], body['metadata']['name'], max_time=30):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    

    def wait_tetragon_network_policy_namespaced(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_tetragon_network_policy_namespaced(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_tetragon_network_policy_namespaced',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def delete_tetragon_network_policy_namespaced(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Tetragon Network Policy Namespaced', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_tetragon_network_policy_namespaced(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if not self.delete_tetragon_network_policy_namespaced_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('Failed to delete tetragon network policy namespaced')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no tetragon network policy namespaced')

            if not self.wait_no_tetragon_network_policy_namespaced(info['namespace'], info['name']):
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True

    def wait_no_tetragon_network_policy_namespaced(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_tetragon_network_policy_namespaced(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_tetragon_network_policy_namespaced',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
