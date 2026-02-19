class K8sSubscriptionNfd():
    def __init__(self):
        pass

    def create_nfd_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            name, 
            'Automatic',
            name,
            'redhat-operators', 
            'openshift-marketplace', 
            channel=channel,
            confirmation=confirmation,
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_subscription_nfd_ready(my_output=my_output, with_instance=False)
            if not success:
                return False
        
        return True

    def delete_nfd_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_nfd(my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_nfd_ready(self, with_instance=False):
        deployments = [
            {'namespace': 'openshift-nfd', 'name': 'nfd-master'}
        ]

        instance_deployments = [
            {'namespace': 'openshift-nfd', 'name': 'nfd-master'}
        ]

        if with_instance:
            deployments.extend(instance_deployments)

        for deployment in deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False

        return True
    
    def wait_subscription_nfd_ready(self, my_output=None, with_instance=False):
        deployments = [
            {'namespace': 'openshift-nfd', 'name': 'nfd-controller-manager'}
        ]
        instance_deployments = [
            {'namespace': 'openshift-nfd', 'name': 'nfd-master'}
        ]

        if with_instance:
            deployments.extend(instance_deployments)

        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        if with_instance:
            daemon_sets = [
                {'namespace': 'openshift-nfd', 'name': 'nfd-worker'}
            ]
            success = self.wait_daemon_sets_ready_state(daemon_sets, my_output=my_output, optional=True)
            if not success:
                return False

        return True

    def wait_no_subscription_nfd(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-nfd', 'name': 'nfd-controller-manager'},
            {'namespace': 'openshift-nfd', 'name': 'nfd-master'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        daemon_sets = [
            {'namespace': 'openshift-nfd', 'name': 'nfd-worker'}
        ]
        success = self.wait_no_daemon_sets(daemon_sets, my_output=my_output, optional=False)
        if not success:
            return False

        return True