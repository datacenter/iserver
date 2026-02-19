import time


class K8sVirtualMachineWait():
    def __init__(self):
        pass
           
    def wait_virtual_machine_status(self, namespace, name, target_status, max_time=60, log_error_on_timeout=True):
        start_time = int(time.time())
        while True:
            info = self.get_virtual_machine(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if info['status'] in target_status:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_virtual_machine_status',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)

    def wait_virtual_machine_up(self, namespace, name, max_time=60, log_error_on_timeout=True):
        return self.wait_virtual_machine_status(namespace, name, ['Running'], max_time=max_time, log_error_on_timeout=log_error_on_timeout)
    
    def wait_virtual_machine_down(self, namespace, name, max_time=60, log_error_on_timeout=True):
        return self.wait_virtual_machine_status(namespace, name, ['Stopped'], max_time=max_time, log_error_on_timeout=log_error_on_timeout)
    
    def wait_virtual_machine_paused(self, namespace, name, max_time=60, log_error_on_timeout=True):
        return self.wait_virtual_machine_status(namespace, name, ['Paused'], max_time=max_time, log_error_on_timeout=log_error_on_timeout)

    def wait_virtual_machine(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_virtual_machine(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_virtual_machine',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_virtual_machine(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_virtual_machine(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_virtual_machine',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
