import time


class K8sClusterwidePrivateNetworkWait():
    def __init__(self):
        pass

    def wait_clusterwide_private_network_webhook(self, max_time=60):
        return self.wait_mutating_webhook(self.pnet_webhook_name, max_time=max_time)

    def wait_no_clusterwide_private_network_webhook(self, max_time=60):
        return self.wait_no_mutating_webhook(self.pnet_webhook_name, max_time=max_time)

    def wait_clusterwide_private_network(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_clusterwide_private_network(
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_clusterwide_private_network',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def wait_no_clusterwide_private_network(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_clusterwide_private_network(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_clusterwide_private_network',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)
