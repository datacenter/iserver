import time


class K8sPvcWait():
    def __init__(self):
        pass

    def wait_pvc(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_pvc(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_pvc',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_pvc_phase(self, namespace, name, target_phase, max_time=60, log_error_on_timeout=True):
        start_time = int(time.time())
        while True:
            pvc_info = self.get_pvc(
                namespace,
                name,
                cache_enabled=False
            )
            if pvc_info is not None:
                if pvc_info['phase'] in target_phase:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_pvc_phase',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)

    def wait_no_pvc(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_pvc(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_pvc',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
