import time
import yaml
from lib import filter_helper


class K8sStorageClassDefault():
    def __init__(self):
        pass

    def get_default_storage_class(self, fallback_to_single=False, cache_enabled=True):
        storage_classes = self.get_storage_classes(cache_enabled=cache_enabled)
        if storage_classes is None:
            return None
        
        for storage_class in storage_classes:
            if storage_class['default']:
                return storage_class
            
        if fallback_to_single and len(storage_classes) == 1:
            return storage_classes[0]
        
        return None
    
    def get_default_storage_class_name(self, cache_enabled=True):
        storage_class = self.get_default_storage_class(cache_enabled=cache_enabled)
        if storage_class is None:
            return None
        return storage_class['name']
    
    def is_default_storage_class(self, cache_enabled=True):
        if self.get_default_storage_class(cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def get_storage_class_default_body(self, name, is_default):
        body = {}
        body['apiVersion'] = 'storage.k8s.io/v1'
        body['kind'] = 'StorageClass'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['metadata']['annotations'] = {}
        if is_default:
            body['metadata']['annotations']['storageclass.kubernetes.io/is-default-class'] = 'true'
        else:
            body['metadata']['annotations']['storageclass.kubernetes.io/is-default-class'] = 'false'
        return body
    
    def set_storage_class_default(self, name, my_output=None, swap_allowed=False):
        if my_output is not None:
            my_output.default('Set Default Storage Class', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        current_default = self.get_default_storage_class_name(cache_enabled=False)
        if current_default is not None:
            if current_default == name:
                if my_output is not None:
                    my_output.default('- already default')
                return True
            
            if not swap_allowed:
                if my_output is not None:
                    my_output.error('Default storage class exists [%s] and swap is not allowed' % (current_default))
                return False
            
            body = self.get_storage_class_default_body(current_default, False)
            if my_output is not None:
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')
    
            success = self.patch_storage_class_mo(body)
            if not success:
                if my_output is not None:
                    my_output.error('rest api failed')
                return False
            
            if my_output is not None:
                my_output.default('- storage class [%s] set to no-default' % (current_default))

        body = self.get_storage_class_default_body(name, True)
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        success = self.patch_storage_class_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False

        if my_output is not None:
            my_output.default('- storage class set to default')

        return True

    def unset_storage_class_default(self, name, my_output=None):
        if my_output is not None:
            my_output.default('Unset Default Storage Class', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        current_default = self.get_default_storage_class_name(cache_enabled=False)
        if current_default is None:
            if my_output is not None:
                my_output.default('- already not default')
            return True
            
        if current_default != name:
            if my_output is not None:
                my_output.error('Different storage class is default one: %s' % (current_default))
            return False
        
        body = self.get_storage_class_default_body(current_default, False)
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        success = self.patch_storage_class_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False
        
        if my_output is not None:
            my_output.default('- storage class default unset')

        return True
