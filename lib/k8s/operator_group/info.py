import time
import yaml
from lib import ip_helper
from lib import filter_helper
from menu.common import get_confirmation


class K8sOperatorGroupInfo():
    def __init__(self):
        self.operator_group = None

    def get_operator_group_info(self, operator_group_mo):
        if operator_group_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            operator_group_mo
        )
        info.update(metadata_info)

        actual_namespaces = self.get(operator_group_mo, 'status:namespaces', on_error=[], on_none=[])
        info['ns'] = []
        for namespace_name in actual_namespaces:
            if len(namespace_name) == 0:
                continue

            ns_info = {}
            ns_info['__Output'] = {}
            ns_info['name'] = namespace_name
            info['ns'].append(
                ns_info
            )

        info['ns'] = sorted(
            info['ns'],
            key=lambda i: i['name']
        )
        info['nsCount'] = len(info['ns'])

        return info

    def get_operator_groups_info(self, cache_enabled=True):
        if cache_enabled:
            if self.operator_group is not None:
                return self.operator_group

        managed_objects = self.get_operator_group_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.operator_group = []
        for managed_object in managed_objects:
            operator_group_info = {}
            operator_group_info['info'] = self.get_operator_group_info(
                managed_object
            )
            operator_group_info['mo'] = managed_object
            self.operator_group.append(
                operator_group_info
            )

        return self.operator_group

    def match_operator_group(self, operator_group_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, operator_group_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (operator_group_info['namespace'], operator_group_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_operator_group',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_operator_groups(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_operator_groups = self.get_operator_groups_info(cache_enabled=cache_enabled)
        if all_operator_groups is None:
            return None

        operator_groups = []

        for operator_group_info in all_operator_groups:
            if not self.match_operator_group(operator_group_info['info'], object_filter):
                continue

            if return_mo:
                operator_groups.append(
                    operator_group_info['mo']
                )
                continue

            operator_groups.append(
                operator_group_info['info']
            )

        return operator_groups

    def is_operator_group(self, namespace, name, cache_enabled=True):
        if self.get_operator_group(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_operator_group(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        operator_groups = self.get_operator_groups(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if operator_groups is None:
            return None

        if len(operator_groups) == 1:
            return operator_groups[0]

        return None

    def wait_operator_group(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            operator_group_info = self.get_operator_group(
                namespace,
                name,
                cache_enabled=False
            )
            if operator_group_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_operator_group',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_operator_group(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            operator_group_info = self.get_operator_group(
                namespace,
                name,
                cache_enabled=False
            )
            if operator_group_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_operator_group',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def get_operator_group_body(self, namespace, name=None, add_target_namespaces=True, target_namespaces=None, upgrade_strategy='Default'):
        body = {}
        body['apiVersion'] = 'operators.coreos.com/v1'
        body['kind'] = 'OperatorGroup'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        if name is not None:
            body['metadata']['name'] = name
        else:
            body['metadata']['name'] = '%s-%s' % (
                namespace,
                ip_helper.get_short_uuid()
            )

        body['spec'] = {}

        if add_target_namespaces:
            if target_namespaces is None:
                body['spec']['targetNamespaces'] = []
                body['spec']['targetNamespaces'].append(
                    namespace
                )
            else:
                body['spec']['targetNamespaces'] = target_namespaces

        if upgrade_strategy is not None:
            body['spec']['upgradeStrategy'] = upgrade_strategy

        return body

    def create_operator_group(
            self, 
            namespace, 
            name=None, 
            add_target_namespaces=True, 
            target_namespaces=None, 
            upgrade_strategy='Default', 
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Operator Group', before_newline=True, underline=True)
            my_output.default('Operator group: %s/%s' % (namespace, name))
            if add_target_namespaces and target_namespaces is not None:
                my_output.default('Target namespaces: %s' % (','.join(target_namespaces)))
            
        if name is None:
            name = '%s-%s' % (
                namespace,
                ip_helper.get_short_uuid()
            )
        
        if not self.is_namespace(namespace, cache_enabled=False):
            if my_output is not None:
                my_output.error(
                    'Namespace does not exist: %s' % (namespace)
                )

            self.log.error(
                'create_operator_group',
                'Namespace does not exist: %s' % (namespace)
            )
            return False
            
        if self.is_operator_group(namespace, name):
            if my_output is not None:
                my_output.default('Operator Group already exists: %s/%s' % (namespace, name))
            return True
        
        body = self.get_operator_group_body(
            namespace,
            name=name,
            add_target_namespaces=add_target_namespaces,
            target_namespaces=target_namespaces,
            upgrade_strategy=upgrade_strategy
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_operator_group_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Operator group created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for operator group [timeout:60]...')

            if not self.wait_operator_group(namespace, name, max_time=30):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    

    def delete_operator_group(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Operator Group', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_operator_group(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_operator_group_mo(namespace, name):
            if my_output is not None:
                my_output.error('Failed to delete operator group')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no operator group')

            if not self.wait_no_operator_group(namespace, name):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True
    
    def delete_operator_group_in_namespace(self, namespace, my_output=None, wait=True):
        groups = self.get_operator_groups(
            object_filter=['namespace:%s' % (namespace)],
            cache_enabled=False
        )
        for group in groups:
            success = self.delete_operator_group(namespace, group['name'], my_output=my_output, wait=wait)
            if not success:
                return False

        return True