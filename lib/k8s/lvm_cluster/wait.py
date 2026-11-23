import time


class K8sLvmClusterWait():
    def __init__(self):
        pass

    def wait_lvm_cluster_ready(self, max_time=180):
        start_time = int(time.time())
        while True:
            if self.is_lvm_cluster_ready(cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_lvm_cluster_ready',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_lvm_cluster_states(self, states, max_time=180):
        start_time = int(time.time())
        while True:
            state = self.get_lvm_cluster_state(cache_enabled=False)
            if state is not None:
                if state in states:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_lvm_cluster_states',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_no_lvm_cluster(self, max_time=300):
        start_time = int(time.time())
        while True:
            lvm_cluster_info = self.get_lvm_cluster(
                cache_enabled=False
            )
            if lvm_cluster_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_lvm_cluster',
                    'Max time reached'
                )
                return False

            time.sleep(5)