class K8sVastDriverWait():
    def __init__(self):
        pass

    def wait_vast_driver(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='VastCSIDriver', max_time=60):
        return self.wait_managed_object(
            'vast_driver',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_vast_driver(self, namespace, name, max_time=60, my_output=None, prompt='VastCSIDriver'):
        return self.wait_no_managed_object(
            'vast_driver',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_vast_driver_resources(self, resources, my_output=None, max_time=180):
        for resource in resources:
            if resource['kind'] == 'DaemonSet':
                if my_output is not None:
                    my_output.default(
                        '- wait for DaemonSet %s/%s ready [timeout:%ss]' % (
                            resource['namespace'],
                            resource['name'],
                            max_time
                        )
                    )

                success = self.wait_daemon_set_ready_state(
                    resource['namespace'],
                    resource['name'],
                    max_time=max_time
                )
                if not success:
                    if my_output is not None:
                        my_output.error('timed out')
                    return False

            if resource['kind'] == 'Deployment':
                if my_output is not None:
                    my_output.default(
                        '- wait for Deployment %s/%s ready [timeout:%ss]' % (
                            resource['namespace'],
                            resource['name'],
                            max_time
                        )
                    )

                success = self.wait_deployment_ready_state(
                    resource['namespace'],
                    resource['name'],
                    max_time=max_time
                )
                if not success:
                    if my_output is not None:
                        my_output.error('timed out')
                    return False

        return True
    
    def wait_no_vast_driver_resources(self, resources, my_output=None, max_time=60):
        for resource in resources:
            if resource['kind'] == 'DaemonSet':
                if my_output is not None:
                    my_output.default(
                        '- wait for no DaemonSet %s/%s [timeout:%ss]' % (
                            resource['namespace'],
                            resource['name'],
                            max_time
                        )
                    )

                success = self.wait_no_daemon_set(
                    resource['namespace'],
                    resource['name'],
                    max_time=max_time
                )
                if not success:
                    if my_output is not None:
                        my_output.error('timed out')
                    return False

            if resource['kind'] == 'Deployment':
                if my_output is not None:
                    my_output.default(
                        '- wait for no Deployment %s/%s [timeout:%ss]' % (
                            resource['namespace'],
                            resource['name'],
                            max_time
                        )
                    )

                success = self.wait_no_deployment(
                    resource['namespace'],
                    resource['name'],
                    max_time=max_time
                )
                if not success:
                    if my_output is not None:
                        my_output.error('timed out')
                    return False

        return True
