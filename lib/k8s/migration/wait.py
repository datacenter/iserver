import copy
import time


class K8sMigrationWait():
    def __init__(self):
        pass

    def wait_migration_finished(self, namespace, name, my_output=None, max_time=600):
        start_time = int(time.time())
        last_events = []
        while True:
            info = self.get_migration(
                namespace,
                name,
                vm_info=True, 
                vmi_info=True, 
                pvc_info=True, 
                dv_info=True, 
                pod_info=True,
                cache_enabled=False
            )
            if info is not None:
                if my_output is not None:
                    for event in info['event']:
                        if event not in last_events:
                            my_output.default(event)

                    last_events = copy.deepcopy(info['event'])

                if info['finished']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_migration',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_migration(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_migration(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_migration',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_migration(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_migration(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_migration',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
