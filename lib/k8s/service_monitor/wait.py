import time


class K8sServiceMonitorWait():
    def __init__(self):
        self.service_monitor = None

    def wait_service_monitor(self, namespace, name, max_time=600, optional=False):
        start_time = int(time.time())
        while True:
            service_monitor = self.get_service_monitor(
                namespace,
                name,
                cache_enabled=False
            )
            if service_monitor is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional and service_monitor is True:
                    self.log.error(
                        'k8s.wait_service_monitor',
                        'Max time reached but service_monitor optional: %s/%s' % (namespace, name)
                    )
                    return True

                self.log.error(
                    'k8s.wait_service_monitor',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_service_monitor_ready(self, namespace, name, max_time=600, my_output=None):
        if my_output is not None:
            my_output.default('Wait for service monitor ready %s/%s...' % (namespace, name))

        start_time = int(time.time())
        while True:
            service_monitor = self.get_service_monitor(
                namespace,
                name,
                target_info=True,
                cache_enabled=False
            )
            if service_monitor is not None:
                if service_monitor['target'] is not None:
                    if service_monitor['target']['ready']:
                        return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_service_monitor',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_service_monitor(self, namespace, name, max_time=600):
        start_time = int(time.time())
        while True:
            service_monitor = self.get_service_monitor(
                namespace,
                name,
                cache_enabled=False
            )
            if service_monitor is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_service_monitor',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_service_monitors(self, service_monitors, max_time=600, my_output=None, optional=False):
        if my_output is not None:
            my_output.default('Wait for service monitors...')

        for service_monitor in service_monitors:
            if my_output is not None:
                my_output.default('- %s/%s' % (service_monitor['namespace'], service_monitor['name']))

            if not self.wait_service_monitor(service_monitor['namespace'], service_monitor['name'], max_time=max_time, optional=optional):
                if my_output is not None:
                    my_output.error('Service monitor not found')
                return False

        return True

    def wait_no_service_monitors(self, service_monitors, max_time=60, my_output=None):
        if my_output is not None:
            my_output.default('Wait for no service monitors...')

        for service_monitor in service_monitors:
            if my_output is not None:
                my_output.default('- %s/%s' % (service_monitor['namespace'], service_monitor['name']))

            if not self.wait_no_service_monitor(service_monitor['namespace'], service_monitor['name'], max_time=max_time):
                if my_output is not None:
                    my_output.error('Service monitor still there')
                return False

        return True
