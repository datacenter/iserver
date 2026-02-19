import time


class K8sSecretWait():
    def __init__(self):
        pass
    
    def wait_secret(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            secret_info = self.get_secret(
                namespace,
                name,
                cache_enabled=False
            )
            if secret_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_secret',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_secret(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            secret_info = self.get_secret(
                namespace,
                name,
                cache_enabled=False
            )
            if secret_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_secret',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
