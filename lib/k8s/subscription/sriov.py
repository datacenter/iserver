class K8sSubscriptionSriov():
    def __init__(self):
        pass

    def is_sriov_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)
    
    def create_sriov_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_sriov_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_sriov_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_sriov(my_output=my_output)
            if not success:
                return False
        
        return True

    def wait_subscription_sriov_ready(self, configured=False, my_output=None):
        deployments = [
            {'namespace': 'openshift-sriov-network-operator', 'name': 'sriov-network-operator'}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        if configured:
            daemon_sets = [
                {'namespace': 'openshift-sriov-network-operator', 'name': 'network-resources-injector'},
                {'namespace': 'openshift-sriov-network-operator', 'name': 'operator-webhook'},
                {'namespace': 'openshift-sriov-network-operator', 'name': 'sriov-network-config-daemon'}
            ]
            success = self.wait_daemon_sets_ready_state(daemon_sets, my_output=my_output, optional=True)
            if not success:
                return False

        return True

    def wait_no_subscription_sriov(self, configured=False, my_output=None):
        deployments = [
            {'namespace': 'openshift-sriov-network-operator', 'name': 'sriov-network-operator'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True
    
    def wait_no_subscription_sriov_configuration(self, my_output=None):
        daemon_sets = [
            {'namespace': 'openshift-sriov-network-operator', 'name': 'network-resources-injector'},
            {'namespace': 'openshift-sriov-network-operator', 'name': 'operator-webhook'},
            {'namespace': 'openshift-sriov-network-operator', 'name': 'sriov-network-config-daemon'}
        ]
        success = self.wait_no_daemon_sets(daemon_sets, my_output=my_output, optional=False)
        if not success:
            return False

        return True