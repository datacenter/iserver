import time
from lib import filter_helper


class K8sStorageClassLvm():
    def __init__(self):
        pass

    def is_storage_class_lvm(self, cache_enabled=True):
        storage_class = self.get_storage_class_lvm(cache_enabled=cache_enabled)
        if storage_class is None:
            return False
        return True
    
    def get_storage_class_lvm(self, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'provisioner:topolvm.io'
        )

        storage_classes = self.get_storage_classes(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if storage_classes is None:
            return None

        if len(storage_classes) == 1:
            return storage_classes[0]

        return None

    def delete_lvm_storage_class(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete LVM Storage Class', before_newline=True, underline=True)

        info = self.get_storage_class_lvm(cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if my_output is not None:
            my_output.default('- namespace: %s' % (info['namespace']))
            my_output.default('- name: %s' % (info['name']))

        if not self.delete_storage_class_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('Failed to delete storage class')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no storage class')

            if not self.wait_no_storage_class(info['namespace'], info['name']):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True

    def wait_storage_class_lvm(self, max_time=180):
        start_time = int(time.time())
        while True:
            if self.is_storage_class_lvm(cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_storage_class_lvm',
                    'Max time reached'
                )
                return False

            time.sleep(5)