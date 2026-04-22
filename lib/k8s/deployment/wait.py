import time


class K8sDeploymentWait():
    def __init__(self):
        pass

    def wait_deployment(self, namespace, name, my_output=None, prompt='Deployment', max_time=60):
        return self.wait_managed_object(
            'deployment',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
    
    def wait_deployment_ready_state(self, namespace, name, max_time=600, my_output=None, prompt=None, optional=False, allow_zero_replicas=False, log_on_error=False):
        if my_output is not None:
            if prompt is not None:
                my_output.default(prompt)
            else:
                my_output.default('Wait for deployment %s/%s ready (optional: %s, allow zero replicas: %s, timeout: %ss)...' % (namespace, name, optional, allow_zero_replicas, max_time))

        start_time = int(time.time())
        while True:
            deployment = self.get_deployment(
                namespace,
                name,
                cache_enabled=False
            )
            if deployment is not None:
                if deployment['ready']:
                    return True
                
                if allow_zero_replicas and deployment['spec_replicas'] == 0:
                    if my_output is not None:
                        my_output.default('Success with allow zero replicas condition')

                    if log_on_error:
                        self.log.debug(
                            'k8s.wait_deployment_ready_state',
                            'Max time reached but deployment zero replicas: %s/%s' % (namespace, name)
                        )

                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional and deployment is None:
                    if my_output is not None:
                        my_output.default('Success with optional condition')

                    if log_on_error:
                        self.log.debug(
                            'k8s.wait_deployment_ready_state',
                            'Max time reached but deployment optional: %s/%s' % (namespace, name)
                        )
                    return True

                if log_on_error:
                    self.log.error(
                        'k8s.wait_deployment_ready_state',
                        'Max time reached: %s/%s' % (namespace, name)
                    )

                return False

            time.sleep(5)

    def wait_deployments_ready_state(self, deployments, max_time=600, my_output=None, optional=False, allow_zero_replicas=False, log_on_error=False, break_on_error=True):
        all_ready = True
        for deployment in deployments:
            success = self.wait_deployment_ready_state(
                deployment['namespace'],
                deployment['name'],
                my_output=my_output,
                max_time=max_time,
                optional=optional,
                allow_zero_replicas=allow_zero_replicas,
                log_on_error=log_on_error
            )
            if not success:
                all_ready = False
                if break_on_error:
                    break

        return all_ready

    def wait_no_deployment(self, namespace, name, max_time=180, prompt='Deployment', optional=False, my_output=None, log_error_on_timeout=False):
        return self.wait_no_managed_object(
            'deployment',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time,
            optional=optional,
            log_error_on_timeout=log_error_on_timeout
        )

    def wait_no_deployments(self, deployments, max_time=180, my_output=None, optional=False, log_error_on_timeout=False, break_on_error=True):
        all_gone = True
        for deployment in deployments:
            success = self.wait_no_deployment(
                deployment['namespace'],
                deployment['name'],
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
    