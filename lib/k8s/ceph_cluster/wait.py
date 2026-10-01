import time


class K8sCephClusterWait():
    def __init__(self):
        pass

    def wait_ceph_cluster(self, max_time=360):
        start_time = int(time.time())
        while True:
            if self.is_ceph_cluster(cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_ceph_cluster',
                    'Max time reached'
                )
                return False

            time.sleep(5)