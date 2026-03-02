import time


class K8sSubscriptionVast():
    def __init__(self):
        self.subscription_vast_deployments = [
            {'namespace': 'vast-csi', 'name': 'vast-csi-operator-controller-manager'}
        ]

    def check_vast_subscription(self, name, my_output=None, check_ready=True, before_newline=True):
        if my_output is not None:
            my_output.default('VAST CSI Operator Subscription', underline=True, before_newline=before_newline)

        subscription = self.get_subscription_by_package(
            name,
            return_mo=False,
            cache_enabled=False
        )
        if subscription is None:
            if my_output is not None:
                my_output.default('Operator %s %s' % (name, my_output.add_color('not found', 'Red')))

            return False
        
        if my_output is not None:
            my_output.default('- subscription: %s' % (subscription['namespace_name']))
            my_output.default('- package: %s' % (name))
            my_output.default('- csv: %s' % (subscription['installed_csv']))

        csv = self.get_cluster_service_version_optimized(
            subscription['namespace'],
            subscription['installed_csv'],
            return_mo=False,
            cache_enabled=False
        )
        if csv is None:
            if my_output is not None:
                my_output.error('Cluster service version not found: %s/%s' % (subscription['namespace'], subscription['installed_csv']))
            return False

        if check_ready:
            return self.is_subscription_vast_ready(my_output=my_output)
        
        return True    

    def create_vast_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            name, 
            'Automatic', 
            name, 
            'certified-operators', 
            'openshift-marketplace', 
            channel=channel,
            confirmation=confirmation, 
            my_output=my_output, 
            wait=wait
        )
        if not success:
            return False
        
        if wait:
            success = self.wait_subscription_vast_ready(my_output=my_output)
            if not success:
                return False
        
        return True
    
    def delete_vast_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_vast(my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)

        return True

    def is_subscription_vast_ready(self, my_output=None):
        ready = True
        if my_output is not None:
            my_output.default('VAST CSI Operator Resources', before_newline=True, underline=True)

        for deployment in self.subscription_vast_deployments:
            if self.is_deployment_ready(deployment['namespace'], deployment['name']):
                if my_output is not None:
                    my_output.default(
                        '- deployment %s/%s %s' % (
                            deployment['namespace'], 
                            deployment['name'],
                            my_output.add_color('ready', 'Green')
                        )
                    )
            else:
                if my_output is not None:
                    my_output.default(
                        '- deployment %s/%s %s' % (
                            deployment['namespace'], 
                            deployment['name'],
                            my_output.add_color('not ready', 'Red')
                        )
                    )
                ready = False

        return ready

    def wait_subscription_vast_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(self.subscription_vast_deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True

    def wait_no_subscription_vast(self, my_output=None):
        success = self.wait_no_deployments(self.subscription_vast_deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True
