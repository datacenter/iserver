import time


class K8sRouteWait():
    def __init__(self):
        pass

    def wait_route_ready(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_route(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_route_ready',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)