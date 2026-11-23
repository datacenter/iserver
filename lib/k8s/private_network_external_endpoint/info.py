import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sPrivateNetworkExternalEndpointInfo():
    def __init__(self):
        self.private_network_external_endpoint = None

    def get_private_network_external_endpoint_info(self, private_network_external_endpoint_mo):
        if private_network_external_endpoint_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            private_network_external_endpoint_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(private_network_external_endpoint_mo, 'spec')
        info['status'] = self.get(private_network_external_endpoint_mo, 'status')
        return info

    def get_private_network_external_endpoints_info(self, cache_enabled=True):
        if cache_enabled:
            if self.private_network_external_endpoint is not None:
                return self.private_network_external_endpoint

        managed_objects = self.get_private_network_external_endpoint_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.private_network_external_endpoint = []
        for managed_object in managed_objects:
            private_network_external_endpoint_info = {}
            private_network_external_endpoint_info['info'] = self.get_private_network_external_endpoint_info(
                managed_object
            )
            private_network_external_endpoint_info['mo'] = managed_object
            self.private_network_external_endpoint.append(
                private_network_external_endpoint_info
            )

        return self.private_network_external_endpoint

    def match_private_network_external_endpoint(self, private_network_external_endpoint_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, private_network_external_endpoint_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (private_network_external_endpoint_info['namespace'], private_network_external_endpoint_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_private_network_external_endpoint',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_private_network_external_endpoints(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_private_network_external_endpoints = self.get_private_network_external_endpoints_info(cache_enabled=cache_enabled)
        if all_private_network_external_endpoints is None:
            return None

        private_network_external_endpoints = []

        for private_network_external_endpoint_info in all_private_network_external_endpoints:
            if not self.match_private_network_external_endpoint(private_network_external_endpoint_info['info'], object_filter):
                continue

            if return_mo:
                private_network_external_endpoints.append(
                    private_network_external_endpoint_info['mo']
                )
                continue

            private_network_external_endpoints.append(
                private_network_external_endpoint_info['info']
            )

        return private_network_external_endpoints

    def is_private_network_external_endpoint(self, namespace, name, cache_enabled=True):
        if self.get_private_network_external_endpoint(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_private_network_external_endpoint(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        private_network_external_endpoints = self.get_private_network_external_endpoints(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if private_network_external_endpoints is None:
            return None

        if len(private_network_external_endpoints) == 1:
            return private_network_external_endpoints[0]

        return None

    def delete_private_network_external_endpoint(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Private Network External Endpoint', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_private_network_external_endpoint(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already gone')
            return True

        if not self.delete_private_network_external_endpoint_mo(namespace, name):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('External endpoint deleted', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for no external endpoint...')

            if not self.wait_no_private_network_external_endpoint(name):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    

    def delete_private_network_external_endpoints(self, my_output=None, wait=True):
        endpoints = self.get_private_network_external_endpoints(cache_enabled=False)
        if endpoints is None:
            return True
        
        if len(endpoints) == 0:
            if my_output is not None:
                my_output.default('No PrivateNetworkExternalEndpoint crds found')
            return True
        
        for endpoint in endpoints:
            if not self.delete_private_network_external_endpoint(endpoint['namespace'], endpoint['name'], wait=wait, my_output=my_output):
                return False
            
        return True

    def wait_no_private_network_external_endpoint(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_private_network_external_endpoint(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_private_network_external_endpoint',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)
