import time


class K8sReplicaSetWait():
    def __init__(self):
        pass

    def wait_replica_set(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            replica_set = self.get_replica_set(
                namespace,
                name,
                cache_enabled=False
            )
            if replica_set is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_replica_set',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_replica_set(self, namespace, name, max_time=600, optional=False):
        start_time = int(time.time())
        while True:
            replica_set = self.get_replica_set(
                namespace,
                name,
                cache_enabled=False
            )
            if replica_set is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional:
                    self.log.error(
                        'k8s.wait_no_replica_set',
                        'Max time reached but replica_set optional: %s/%s' % (namespace, name)
                    )
                    return True

                self.log.error(
                    'k8s.wait_no_replica_set',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
