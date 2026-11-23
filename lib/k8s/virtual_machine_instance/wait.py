import time


class K8sVirtualMachineInstanceWait():
    def __init__(self):
        pass
           
    def wait_virtual_machine_instance(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_virtual_machine_instance(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_virtual_machine_instance',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_virtual_machine_instance(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_virtual_machine_instance(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_virtual_machine_instance',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
