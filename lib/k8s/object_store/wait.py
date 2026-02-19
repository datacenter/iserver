import time


class K8sObjectStoreWait():
    def __init__(self):
        pass

    def wait_object_store(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_object_store(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_object_store',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_object_store(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_object_store(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_object_store',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
