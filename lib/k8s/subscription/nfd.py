class K8sSubscriptionNfd():
    def __init__(self):
        self.subscription_nfd_resources = [
            {'type': 'deployment', 'namespace': 'openshift-nfd', 'name': 'nfd-controller-manager'}
        ]

        self.instance_nfd_resources = [
            {'type': 'deployment', 'namespace': 'openshift-nfd', 'name': 'nfd-master'},
            {'type': 'daemonset', 'namespace': 'openshift-nfd', 'name': 'nfd-worker'}
        ]

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

    def is_subscription_nfd_ready(self, with_instance=False, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.subscription_nfd_resources
        if with_instance:
            resources.extend(self.instance_nfd_resources)

        return self.is_subscription_ready('nfd', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)
    
    def wait_subscription_nfd_ready(self, with_instance=False, my_output=None):
        resources = self.subscription_nfd_resources
        if with_instance:
            resources.extend(self.instance_nfd_resources)

        return self.wait_subscription_resources_ready('nfd', resources, my_output=my_output)

    def wait_no_subscription_nfd(self, my_output=None):
        resources = self.subscription_nfd_resources
        resources.extend(self.instance_nfd_resources)
        return self.wait_no_subscription_resources('nfd', resources, my_output=my_output)
    