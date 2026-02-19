import json
import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sNodeFeatureDiscoveryInfo():
    def __init__(self):
        self.node_feature_discovery = None

    def get_node_feature_discovery_info(self, node_feature_discovery_mo):
        if node_feature_discovery_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            node_feature_discovery_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(node_feature_discovery_mo, 'spec')
        return info

    def get_node_feature_discoveries_info(self, cache_enabled=True):
        if cache_enabled:
            if self.node_feature_discovery is not None:
                return self.node_feature_discovery

        managed_objects = self.get_node_feature_discovery_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.node_feature_discovery = []
        for managed_object in managed_objects:
            node_feature_discovery_info = {}
            node_feature_discovery_info['info'] = self.get_node_feature_discovery_info(
                managed_object
            )
            node_feature_discovery_info['mo'] = managed_object
            self.node_feature_discovery.append(
                node_feature_discovery_info
            )

        return self.node_feature_discovery

    def match_node_feature_discovery(self, node_feature_discovery_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, node_feature_discovery_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_feature_discovery_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_node_feature_discovery',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_node_feature_discoveries(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_node_feature_discoverys = self.get_node_feature_discoveries_info(cache_enabled=cache_enabled)
        if all_node_feature_discoverys is None:
            return None

        node_feature_discoverys = []

        for node_feature_discovery_info in all_node_feature_discoverys:
            if not self.match_node_feature_discovery(node_feature_discovery_info['info'], object_filter):
                continue

            if return_mo:
                node_feature_discoverys.append(
                    node_feature_discovery_info['mo']
                )
                continue

            node_feature_discoverys.append(
                node_feature_discovery_info['info']
            )

        return node_feature_discoverys

    def is_node_feature_discovery(self, namespace, name, cache_enabled=True):
        if self.get_node_feature_discovery(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_node_feature_discovery(self, cache_enabled=True):
        policies = self.get_node_feature_discoveries(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_node_feature_discovery(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        node_feature_discoverys = self.get_node_feature_discoveries(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if node_feature_discoverys is None:
            return None

        if len(node_feature_discoverys) == 1:
            return node_feature_discoverys[0]

        return None

    def delete_node_feature_discoveries(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Node Feature Discovery Instances', before_newline=True, underline=True)

        nfds = self.get_node_feature_discoveries(
            cache_enabled=False
        )
        if nfds is None:
            if my_output is not None:
                my_output.error('Failed to get nfd instances')
            return False

        if len(nfds) == 0:
            if my_output is not None:
                my_output.default('- no instances found')
            return True
        
        for nfd in nfds:
            if my_output is not None:
                my_output.default('- %s' % (nfd['namespace_name']))

            success = self.delete_node_feature_discovery_mo(
                nfd['namespace'],
                nfd['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('NFD instance delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no nfd instance')

                if not self.wait_no_node_feature_discovery(nfd['namespace'], nfd['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
    
    def wait_node_feature_discovery(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_node_feature_discovery(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_node_feature_discovery',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_node_feature_discovery(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_node_feature_discovery(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_node_feature_discovery',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def create_node_feature_discovery(self, body, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        namespace = body['metadata']['namespace']
        name = body['metadata']['name']
        if my_output is not None:
            my_output.default('Create NFD Default Instance', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if self.is_node_feature_discovery(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
                return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_node_feature_discovery_mo(body):
            if my_output is not None:
                my_output.error('NodeFeatureDiscovery instance create failed')
            return False

        if my_output is not None:
            my_output.default('NFD instance created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for nfd instance [timeout:60]...')

        if not self.wait_node_feature_discovery(namespace, name, max_time=30):
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        if my_output is not None:
            my_output.default('Wait for nfd instance resources...')

        success = self.wait_subscription_nfd_ready(my_output=my_output, with_instance=True)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        success = self.wait_nodes_annotations(
            ['nfd.node.kubernetes.io/feature-labels'],
            my_output=my_output,
            worker_only=True
        )
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        return True    