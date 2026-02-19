import time


class K8sProviderWait():
    def __init__(self):
        pass

    def wait_provider(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_provider(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_provider',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)


    def wait_provider_ready(self, namespace, name, max_time=60, break_on_connection_failed=True):
        start_time = int(time.time())
        while True:
            info = self.get_provider(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if break_on_connection_failed and info['phase'] == 'ConnectionFailed':
                    return False
                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_provider',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_provider(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_provider(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_provider',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
