import time


class K8sNamespaceWait():
    def __init__(self):
        pass

    def wait_namespace(self, namespace, max_time=60):
        start_time = int(time.time())
        while True:
            namespace_info = self.get_namespace(
                namespace,
                cache_enabled=False
            )
            if namespace_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_namespace',
                    'Max time reached: %s' % (namespace)
                )
                return False

            time.sleep(5)

    def wait_no_namespace(self, namespace, max_time=60):
        start_time = int(time.time())
        while True:
            namespace_info = self.get_namespace(
                namespace,
                cache_enabled=False
            )
            if namespace_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_namespace',
                    'Max time reached: %s' % (namespace)
                )
                return False

            time.sleep(5)