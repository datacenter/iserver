import time


class K8sForkliftControllerWait():
    def __init__(self):
        pass

    def wait_forklift_controller(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_forklift_controller(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_forklift_controller',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)


    def wait_forklift_controller_ready(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_forklift_controller(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None and info['ready']:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_forklift_controller',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_forklift_controller(self, namespace, name, max_time=360):
        start_time = int(time.time())
        while True:
            info = self.get_forklift_controller(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_forklift_controller',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
