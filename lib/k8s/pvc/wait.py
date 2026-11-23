import time


class K8sPvcWait():
    def __init__(self):
        pass

    def wait_pvc(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='PersistentVolumeClaim', max_time=60):
        return self.wait_managed_object(
            'pvc',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_pvc(self, namespace, name, max_time=60, my_output=None, prompt='PersistentVolumeClaim'):
        return self.wait_no_managed_object(
            'pvc',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

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