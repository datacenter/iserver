import time


class K8sConfigMapWait():
    def __init__(self):
        pass

    def wait_config_map(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            config_map_info = self.get_config_map(
                namespace,
                name,
                cache_enabled=False
            )
            if config_map_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_config_map',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_config_map(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            config_map_info = self.get_config_map(
                namespace,
                name,
                cache_enabled=False
            )
            if config_map_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_config_map',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
