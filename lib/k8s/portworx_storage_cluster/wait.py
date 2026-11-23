import time


class K8sPortworxStorageClusterWait():
    def __init__(self):
        pass

    def wait_portworx_storage_cluster(self, max_time=360):
        start_time = int(time.time())
        while True:
            portworx_storage_cluster_info = self.get_portworx_storage_cluster(
                cache_enabled=False
            )
            if portworx_storage_cluster_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_portworx_storage_cluster',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_portworx_storage_cluster_ready(self, max_time=360):
        start_time = int(time.time())
        while True:
            portworx_storage_cluster_info = self.get_portworx_storage_cluster(
                cache_enabled=False
            )
            if portworx_storage_cluster_info is not None:
                if portworx_storage_cluster_info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_portworx_storage_cluster_ready',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_no_portworx_storage_cluster(self, max_time=60):
        start_time = int(time.time())
        while True:
            portworx_storage_cluster_info = self.get_portworx_storage_cluster(
                cache_enabled=False
            )
            if portworx_storage_cluster_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_portworx_storage_cluster',
                    'Max time reached'
                )
                return False

            time.sleep(5)
