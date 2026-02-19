import time


class K8sNetworkMapWait():
    def __init__(self):
        pass

    def wait_network_map(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_network_map(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_network_map',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)


    def wait_network_map_ready(self, namespace, name, max_time=60, break_on_invalid=True):
        start_time = int(time.time())
        while True:
            info = self.get_network_map(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if break_on_invalid and info['invalid']:
                    return False
                
                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_network_map',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_network_map(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_network_map(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_network_map',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
