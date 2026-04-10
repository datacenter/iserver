import time


class K8sDaemonSetWait():
    def __init__(self):
        pass

    def wait_daemon_set(self, namespace, name, my_output=None, prompt='DaemonSet', max_time=60):
        return self.wait_managed_object(
            'daemon_set',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
    
    def wait_daemon_set_ready_state(self, namespace, name, max_time=600, my_output=None, optional=False, log_on_error=False):
        if my_output is not None:
            my_output.default('Wait for daemonset %s/%s ready (optional: %s, timeout: %ss)...' % (namespace, name, optional, max_time))

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
                    if my_output is not None:
                        my_output.default('Success with optional condition')

                    if log_on_error:
                        self.log.debug(
                            'k8s.wait_daemon_set_ready_state',
                            'Max time reached but ds optional: %s/%s' % (namespace, name)
                        )
                    return True

                if my_output is not None:
                    my_output.default(my_output.add_color('timed out', 'Red'))

                if log_on_error:
                    self.log.error(
                        'k8s.wait_daemon_set_ready_state',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)

    def wait_daemon_sets_ready_state(self, daemon_sets, max_time=600, my_output=None, optional=False, log_on_error=False, break_on_error=True):
        all_ready = True
        for daemon_set in daemon_sets:
            success = self.wait_daemon_set_ready_state(
                daemon_set['namespace'],
                daemon_set['name'],
                my_output=my_output,
                max_time=max_time,
                optional=optional,
                log_on_error=log_on_error
            )
            if not success:
                all_ready = False
                if break_on_error:
                    break

        return all_ready

    def wait_no_daemon_set(self, namespace, name, max_time=180, prompt='DaemonSet', my_output=None, optional=False, log_error_on_timeout=False):
        return self.wait_no_managed_object(
            'daemon_set',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time,
            optional=optional,
            log_error_on_timeout=log_error_on_timeout
        )

    def wait_no_daemon_sets(self, daemon_sets, max_time=180, my_output=None, optional=False, log_error_on_timeout=False, break_on_error=True):
        all_gone = True
        for daemon_set in daemon_sets:
            success = self.wait_no_daemon_set(
                daemon_set['namespace'],
                daemon_set['name'],
                my_output=my_output,
                max_time=max_time,
                optional=optional,
                log_error_on_timeout=log_error_on_timeout
            )
            if not success:
                all_gone = False
                if break_on_error:
                    break

        return all_gone
