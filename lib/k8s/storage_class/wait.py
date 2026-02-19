import time


class K8sStorageClassWait():
    def __init__(self):
        pass

    def wait_storage_class(self, name, max_time=180):
        start_time = int(time.time())
        while True:
            if self.is_storage_class(name, cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_storage_class',
                    'Max time reached'
                )
                return False

            time.sleep(5)
    