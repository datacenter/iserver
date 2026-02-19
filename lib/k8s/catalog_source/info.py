import time
import yaml
import copy
from lib import filter_helper
from menu.common import get_confirmation


class K8sCatalogSourceInfo():
    def __init__(self):
        self.catalog_source = None

    def get_catalog_source_info(self, catalog_source_mo):
        if catalog_source_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            catalog_source_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(catalog_source_mo, 'spec')
        info['status'] = self.get(catalog_source_mo, 'status')
        info['info'] = {}
        info['info']['display_name'] = self.get(catalog_source_mo, 'spec:displayName')

        return info

    def get_catalog_sources_info(self, cache_enabled=True):
        if cache_enabled:
            if self.catalog_source is not None:
                return self.catalog_source

        managed_objects = self.get_catalog_source_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.catalog_source = []
        for managed_object in managed_objects:
            catalog_source_info = {}
            catalog_source_info['info'] = self.get_catalog_source_info(
                managed_object
            )
            catalog_source_info['mo'] = managed_object
            self.catalog_source.append(
                catalog_source_info
            )

        return self.catalog_source

    def match_catalog_source(self, catalog_source_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, catalog_source_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (catalog_source_info['namespace'], catalog_source_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_catalog_source',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_catalog_sources(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_catalog_sources = self.get_catalog_sources_info(cache_enabled=cache_enabled)
        if all_catalog_sources is None:
            return None

        catalog_sources = []

        for catalog_source_info in all_catalog_sources:
            if not self.match_catalog_source(catalog_source_info['info'], object_filter):
                continue

            if return_mo:
                catalog_sources.append(
                    catalog_source_info['mo']
                )
                continue

            catalog_sources.append(
                catalog_source_info['info']
            )

        return catalog_sources

    def is_catalog_source(self, namespace, name, cache_enabled=True):
        if self.get_catalog_source(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_catalog_source(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        catalog_sources = self.get_catalog_sources(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if catalog_sources is None:
            return None

        if len(catalog_sources) == 1:
            return catalog_sources[0]

        return None

    def get_catalog_source_body(self, namespace, name, source, image):
        body = {}
        body['apiVersion'] = 'operators.coreos.com/v1alpha1'
        body['kind'] = 'CatalogSource'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['sourceType'] = source
        body['spec']['image'] = image
        return body
    

    def create_catalog_source(self, namespace, name, image, source='grpc', confirmation=False, my_output=None, wait=True, hide_image=False):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Catalog Source', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- source: %s' % (source))
            if not hide_image:
                my_output.default('- image: %s' % (image))

        if self.is_catalog_source(namespace, name):
            if my_output is not None:
                my_output.default('- catalog source already exists')
            return True

        body = self.get_catalog_source_body(
            namespace,
            name,
            source,
            image
        )
        if my_output is not None:
            if hide_image:
                new_body = copy.deepcopy(body)
                new_body['spec']['image'] = 'user-provided'
                my_output.default(yaml.dump(new_body), before_newline=True, wrap='~~~')
            else:
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_catalog_source_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Catalog source created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for catalog source [timeout:60]...')

            if not self.wait_catalog_source(namespace, name, max_time=30):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    

    def wait_catalog_source(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            catalog_source_info = self.get_catalog_source(
                namespace,
                name,
                cache_enabled=False
            )
            if catalog_source_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_catalog_source',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def delete_catalog_source(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Catalog Source', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_catalog_source(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if not self.delete_catalog_source_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('Failed to delete catalog source')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no catalog source')

            if not self.wait_no_catalog_source(info['namespace'], info['name']):
                if my_output is not None:
                    my_output.error('Giving up')
                return False
            
            if my_output is not None:
                my_output.default('- wait for no catalog source pod')

            if not self.wait_no_catalog_source_pod('CatalogSource/%s' % (name)):
                if my_output is not None:
                    my_output.error('Giving up')
                return False
            
        return True

    def wait_no_catalog_source(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            catalog_source_info = self.get_catalog_source(
                namespace,
                name,
                cache_enabled=False
            )
            if catalog_source_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_catalog_source',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)


    def wait_no_catalog_source_pod(self, owner, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_pods(
                object_filter=['owner:%s' % (owner)],
                cache_enabled=False
            )
            if info is not None and len(info) == 0:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_catalog_source_pod',
                    'Max time reached: owner %s' % (owner)
                )
                return False

            time.sleep(5)
