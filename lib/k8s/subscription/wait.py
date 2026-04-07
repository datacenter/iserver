import time


class K8sSubscriptionWait():
    def __init__(self):
        pass

    def wait_subscription_install_plan(self, namespace, name, max_time=360):
        start_time = int(time.time())
        while True:
            subscription = self.get_subscription(
                namespace,
                name,
                cache_enabled=False
            )
            if subscription is not None:
                if subscription['install_plan_name'] is not None:
                    return subscription['install_plan_name']

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_subscription_install_plan',
                    'Max time reached'
                )
                return None

            time.sleep(5)

    def wait_no_subscription(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            subscription_info = self.get_subscription(
                namespace,
                name,
                cache_enabled=False
            )
            if subscription_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_subscription',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_subscription_resources_ready(self, subscription_name, resources, my_output=None, break_on_error=True):
        for resource in resources:
            if resource['type'] not in ['deployment', 'daemonset']:
                if my_output is not None:
                    my_output.error('Unsupported resource type: %s' % (resource['type']))                    
                return False

        ready = True
        for resource in resources:
            if 'optional' not in resource:
                resource['optional'] = False

            if resource['type'] == 'deployment':
                if 'allow_zero_replicas' not in resource:
                    resource['allow_zero_replicas'] = False

            if resource['type'] == 'deployment':
                success = self.wait_deployment_ready_state(
                    resource['namespace'], 
                    resource['name'], 
                    my_output=my_output, 
                    optional=resource['optional'], 
                    allow_zero_replicas=resource['allow_zero_replicas']
                )

            if resource['type'] == 'daemonset':
                success = self.wait_daemon_set_ready_state(
                    resource['namespace'], 
                    resource['name'], 
                    my_output=my_output, 
                    optional=resource['optional']
                )

            if not success:
                ready = False

                if break_on_error:
                    break

        if not ready:
            if my_output is not None:
                my_output.default(
                    'Subscription %s %s' % (
                        subscription_name,
                        my_output.add_color('not ready', 'Red')
                    )
                )
        
        if my_output is not None:
            my_output.default(
                'Subscription %s %s' % (
                    subscription_name,
                    my_output.add_color('ready', 'Green')
                )

            )

        return ready

    def wait_no_subscription_resources(self, subscription_name, resources, my_output=None, break_on_error=True):
        for resource in resources:
            if resource['type'] not in ['deployment', 'daemonset']:
                if my_output is not None:
                    my_output.error('Unsupported resource type: %s' % (resource['type']))                    
                return False

        gone = True
        for resource in resources:
            if 'optional' not in resource:
                resource['optional'] = False

            if 'log_on_error' not in resource:
                resource['log_on_error'] = False

            if 'max_time' not in resource:
                resource['max_time'] = 180

            if resource['type'] == 'deployment':
                success = self.wait_no_deployment(
                    resource['namespace'], 
                    resource['name'], 
                    my_output=my_output, 
                    optional=resource['optional'], 
                    max_time=resource['max_time'],
                    log_on_error=resource['log_on_error']
                )

            if resource['type'] == 'daemonset':
                success = self.wait_no_daemon_set(
                    resource['namespace'], 
                    resource['name'], 
                    my_output=my_output, 
                    optional=resource['optional'], 
                    max_time=resource['max_time'],
                    log_on_error=resource['log_on_error']
                )

            if not success:
                gone = False

                if break_on_error:
                    break

        if not gone:
            if my_output is not None:
                my_output.default(
                    'Subscription %s resource %s' % (
                        subscription_name,
                        my_output.add_color('still found', 'Red')
                    )
                )
        
        if my_output is not None:
            my_output.default(
                'Subscription %s resources %s' % (
                    subscription_name,
                    my_output.add_color('gone', 'Green')
                )

            )

        return gone
