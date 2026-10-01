import time


class K8sVolumeSnapshotWait():
    def __init__(self):
        pass

    def wait_no_volume_snapshot(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            volume_snapshot_info = self.get_volume_snapshot(
                namespace,
                name,
                cache_enabled=False
            )
            if volume_snapshot_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_volume_snapshot',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)