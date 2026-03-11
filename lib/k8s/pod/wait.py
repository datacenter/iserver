import time


class K8sPodWait():
    def __init__(self):
        pass
           
    def wait_pod_phase(self, namespace, name, target_phase, max_time=60, log_error_on_timeout=True):
        start_time = int(time.time())
        while True:
            pod_info = self.get_pod(
                namespace,
                name,
                cache_enabled=False
            )
            if pod_info is not None:
                if pod_info['phase'] in target_phase:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_pod_phase',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)

    def wait_no_pod(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            pod_info = self.get_pod(
                namespace,
                name,
                cache_enabled=False
            )
            if pod_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_pod',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_pods(self, pods, max_time=60, prompt='Pod', my_output=None):
        for pod in pods:
            success = self.wait_no_managed_object(
                'pod',
                pod['name'],
                namespace=pod['namespace'],
                my_output=my_output,
                prompt='- wait for no %s %s/%s [timeout:%ss]' % (prompt, pod['namespace'], pod['name'], max_time),
                max_time=max_time
            )
            if not success:
                return False

        return True

    def wait_pods_count(self, object_filter, count, max_time=60):
        start_time = int(time.time())
        while True:
            pod_info = self.get_pods(
                object_filter=object_filter,
                cache_enabled=False
            )
            if pod_info is not None and len(pod_info) == count:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_pod',
                    'Max time reached'
                )
                return False

            time.sleep(5)
