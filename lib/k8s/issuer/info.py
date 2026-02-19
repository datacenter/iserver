import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sIssuerInfo():
    def __init__(self):
        self.issuer = None

    def get_issuer_info(self, issuer_mo):
        if issuer_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            issuer_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(issuer_mo, 'spec')
        info['status'] = self.get(issuer_mo, 'status')
        return info

    def get_issuers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.issuer is not None:
                return self.issuer

        managed_objects = self.get_issuer_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.issuer = []
        for managed_object in managed_objects:
            issuer_info = {}
            issuer_info['info'] = self.get_issuer_info(
                managed_object
            )
            issuer_info['mo'] = managed_object
            self.issuer.append(
                issuer_info
            )

        return self.issuer

    def match_issuer(self, issuer_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, issuer_info['namespace']):
                    return False
                
            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, issuer_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_issuer',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_issuers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_issuers = self.get_issuers_info(cache_enabled=cache_enabled)
        if all_issuers is None:
            return None

        issuers = []

        for issuer_info in all_issuers:
            if not self.match_issuer(issuer_info['info'], object_filter):
                continue

            if return_mo:
                issuers.append(
                    issuer_info['mo']
                )
                continue

            issuers.append(
                issuer_info['info']
            )

        return issuers

    def is_issuer(self, namespace, name, cache_enabled=True):
        if self.get_issuer(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_issuer(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        issuers = self.get_issuers(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if issuers is None:
            return None

        if len(issuers) == 1:
            return issuers[0]

        return None

    def get_issuer_body(self, namespace, name, secret_name):
        body = {}
        body['apiVersion'] = 'cert-manager.io/v1'
        body['kind'] = 'Issuer'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['ca'] = {}
        body['spec']['ca']['secretName'] = secret_name
        return body

    def create_issuer(self, namespace, name, secret_name, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Issuer', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if self.is_issuer(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already created')
            return True
        
        body = self.get_issuer_body(
            namespace,
            name,
            secret_name
        )

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False
        
        success = self.create_issuer_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('Issuer create failed')
            return False

        if my_output is not None:
            my_output.default('- issuer created')
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait until issuer found...')

        success = self.wait_issuer(namespace, name, max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False
        
        return True
    
    def wait_issuer(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_issuer(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_issuer',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def delete_issuer(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Issuer', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_issuer(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        success = self.delete_issuer_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no issuer')

        success = self.wait_no_issuer(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
    
    def wait_no_issuer(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_issuer(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_issuer',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wipe_issuers(self):
        issuers_mo = self.get_issuers(return_mo=True)
        if issuers_mo is None:
            return False
        
        for issuer_mo in issuers_mo:
            success = self.delete_issuer_mo(
                issuer_mo['metadata']['namespace'],
                issuer_mo['metadata']['name']
            )
            if not success:
                return False
            
        return True
    