import time


class K8sServiceWait():
    def __init__(self):
        pass

    def wait_service(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            service = self.get_service(
                namespace,
                name,
                cache_enabled=False
            )
            if service is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_service',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_service(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            service = self.get_service(
                namespace,
                name,
                cache_enabled=False
            )
            if service is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_service',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
