import time


class K8sClusterPolicyWait():
    def __init__(self):
        pass

    def wait_cluster_policy(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_cluster_policy(
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_cluster_policy',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def wait_cluster_policy_ready(self, name, max_time=180):
        start_time = int(time.time())
        while True:
            info = self.get_cluster_policy(
                name,
                cache_enabled=False
            )
            if info is not None:
                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_cluster_policy_ready',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def wait_no_cluster_policy(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_cluster_policy(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_cluster_policy',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)