class K8sStorageClassWait():
    def __init__(self):
        pass

    def wait_storage_class(self, name, max_time=180, my_output=None, prompt='StorageClass'):
        return self.wait_managed_object(
            'storage_class',
            name,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_storage_class(self, name, max_time=180, my_output=None, prompt='StorageClass'):
        return self.wait_no_managed_object(
            'storage_class',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )