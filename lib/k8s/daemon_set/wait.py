import time


class K8sDaemonSetWait():
    def __init__(self):
        pass

    def wait_daemon_set_ready_state(self, namespace, name, max_time=600, optional=False):
        start_time = int(time.time())
        while True:
            daemon_set = self.get_daemon_set(
                namespace,
                name,
                cache_enabled=False
            )
            if daemon_set is not None:
                if daemon_set['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional and daemon_set is None:
                    self.log.debug(
                        'k8s.wait_daemon_set_ready_state',
                        'Max time reached but ds optional: %s/%s' % (namespace, name)
                    )
                    return True

                self.log.error(
                    'k8s.wait_daemon_set_ready_state',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_daemon_set(self, namespace, name, max_time=600, optional=False):
        start_time = int(time.time())
        while True:
            daemon_set = self.get_daemon_set(
                namespace,
                name,
                cache_enabled=False
            )
            if daemon_set is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional and daemon_set is not None:
                    self.log.debug(
                        'k8s.wait_no_daemon_set',
                        'Max time reached but ds optional: %s/%s' % (namespace, name)
                    )
                    return True

                self.log.error(
                    'k8s.wait_no_daemon_set',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_daemon_sets_ready_state(self, daemon_sets, max_time=600, my_output=None, optional=False):
        if my_output is not None:
            my_output.default('Wait for deamon sets ready...')

        for daemon_set in daemon_sets:
            if my_output is not None:
                my_output.default('- %s/%s' % (daemon_set['namespace'], daemon_set['name']))

            if not self.wait_daemon_set_ready_state(daemon_set['namespace'], daemon_set['name'], max_time=max_time, optional=optional):
                if my_output is not None:
                    my_output.error('Daemon set did not reach ready state')
                return False

        return True

    def wait_no_daemon_sets(self, daemon_sets, max_time=600, my_output=None, optional=False):
        if my_output is not None:
            my_output.default('Wait for deamon sets deleted...')

        for daemon_set in daemon_sets:
            if my_output is not None:
                my_output.default('- %s/%s' % (daemon_set['namespace'], daemon_set['name']))

            if not self.wait_no_daemon_set(daemon_set['namespace'], daemon_set['name'], max_time=max_time, optional=optional):
                if my_output is not None:
                    my_output.error('Daemon set still there...')
                return False

        return True
