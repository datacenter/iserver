class K8sSubscriptionNmstate():
    def __init__(self):
        self.subscription_nmstate_resources = [
            {'type': 'deployment', 'namespace': 'openshift-nmstate', 'name': 'nmstate-operator'}
        ]

        self.instance_nmstate_resources = [
            {'type': 'deployment', 'namespace': 'openshift-nmstate', 'name': 'nmstate-console-plugin'},
            {'type': 'deployment', 'namespace': 'openshift-nmstate', 'name': 'nmstate-metrics'},
            {'type': 'deployment', 'namespace': 'openshift-nmstate', 'name': 'nmstate-webhook'},
            {'type': 'daemonset', 'namespace': 'openshift-nmstate', 'name': 'nmstate-handler'}
        ]

    def create_nmstate_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_nmstate_ready(my_output=my_output, with_instance=False)
            if not success:
                return False
        
        return True

    def delete_nmstate_subscription(self, namespace, name, my_output=None, wait=True):
        resources = self.get_subscription_resources(
            self.subscription_nmstate_resources + self.instance_nmstate_resources,
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
        
        if not wait:
            return True

        success = self.wait_no_subscription_resources('nmstate', resources, my_output=my_output)
        if not success:
            return False

        return True

    def is_subscription_nmstate_ready(self, with_instance=False, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.subscription_nmstate_resources
        if with_instance:
            resources.extend(self.instance_nmstate_resources)

        return self.is_subscription_ready('nmstate', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)
    
    def wait_subscription_nmstate_ready(self, my_output=None, with_instance=False):
        resources = self.subscription_nmstate_resources
        if with_instance:
            resources.extend(self.instance_nmstate_resources)

        return self.wait_subscription_resources('nmstate', resources, my_output=my_output)
        
    def wait_no_subscription_nmstate(self, my_output=None, instance_only=False, with_instance=True):
        resources = []
        if not instance_only:
            resources.extend(self.subscription_nmstate_resources)
        if with_instance:
            resources.extend(self.instance_nmstate_resources)

        if len(resources) == 0:
            return True
            
        return self.wait_no_subscription_resources('nmstate', resources, my_output=my_output)