class K8sSubscriptionMetallb():
    def __init__(self):
        self.subscription_metallb_resources = [
            {'type': 'deployment', 'namespace': 'metallb-system', 'name': 'metallb-operator-controller-manager'},
            {'type': 'deployment', 'namespace': 'metallb-system', 'name': 'metallb-operator-webhook-server'}
        ]

        self.instance_metallb_resources = [
            {'type': 'deployment', 'namespace': 'metallb-system', 'name': 'controller'},
            {'type': 'daemonset', 'namespace': 'metallb-system', 'name': 'speaker'}
        ]

    def create_metallb_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_metallb_ready(my_output=my_output, with_instance=False)
            if not success:
                return False
        
        return True

    def delete_metallb_subscription(self, namespace, name, my_output=None, wait=True):
        resources = self.get_subscription_resources(
            self.subscription_metallb_resources,
            cache_enabled=False
        )
        
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_resources('metallb', resources, my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_metallb_ready(self, with_instance=False, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.subscription_metallb_resources
        if with_instance:
            resources.extend(self.instance_metallb_resources)

        return self.is_subscription_ready('metallb', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)
    
    def wait_subscription_metallb_ready(self, with_instance=False, my_output=None):
        resources = self.subscription_metallb_resources
        if with_instance:
            resources.extend(self.instance_metallb_resources)

        return self.wait_subscription_resources_ready('metallb', resources, my_output=my_output)

    def wait_subscription_metallb_instance_ready(self, my_output=None):
        return self.wait_subscription_resources_ready('metallb', self.instance_metallb_resources, my_output=my_output)
