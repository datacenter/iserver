import time


class K8sDeploymentWait():
    def __init__(self):
        pass

    def wait_deployment(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            deployment = self.get_deployment_optimized(
                namespace,
                name,
                cache_enabled=False
            )
            if deployment is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_deployment',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_deployment_ready_state(self, namespace, name, max_time=600, optional=False, allow_zero_replicas=False):
        start_time = int(time.time())
        while True:
            deployment = self.get_deployment_optimized(
                namespace,
                name,
                cache_enabled=False
            )
            if deployment is not None:
                if deployment['ready']:
                    return True
                
                if allow_zero_replicas and deployment['spec_replicas'] == 0:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional and deployment is True:
                    self.log.error(
                        'k8s.wait_deployment_ready_state',
                        'Max time reached but deployment optional: %s/%s' % (namespace, name)
                    )
                    return True

                self.log.error(
                    'k8s.wait_deployment_ready_state',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_deployment(self, namespace, name, max_time=600, optional=False):
        start_time = int(time.time())
        while True:
            deployment = self.get_deployment_optimized(
                namespace,
                name,
                cache_enabled=False
            )
            if deployment is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional:
                    self.log.error(
                        'k8s.wait_no_deployment',
                        'Max time reached but deployment optional: %s/%s' % (namespace, name)
                    )
                    return True

                self.log.error(
                    'k8s.wait_no_deployment',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_deployments_ready_state(self, deployments, max_time=600, my_output=None, optional=False, allow_zero_replicas=False):
        if my_output is not None:
            my_output.default('Wait for deployments ready (optional: %s, allow zero replicas: %s)...' % (optional, allow_zero_replicas))

        for deployment in deployments:
            if my_output is not None:
                my_output.default('- %s/%s' % (deployment['namespace'], deployment['name']))

            if not self.wait_deployment_ready_state(deployment['namespace'], deployment['name'], max_time=max_time, optional=optional, allow_zero_replicas=allow_zero_replicas):
                if my_output is not None:
                    my_output.error('Deployment did not reach ready state')
                return False

        return True

    def wait_no_deployments(self, deployments, max_time=600, my_output=None, optional=False):
        if my_output is not None:
            my_output.default('Wait for deployments deleted (optional: %s)...' % (optional))

        for deployment in deployments:
            if my_output is not None:
                my_output.default('- %s/%s' % (deployment['namespace'], deployment['name']))

            if not self.wait_no_deployment(deployment['namespace'], deployment['name'], max_time=max_time, optional=optional):
                if my_output is not None:
                    my_output.error('Deployment still there...')
                return False

        return True
    