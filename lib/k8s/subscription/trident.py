import time


class K8sSubscriptionTrident():
    def __init__(self):
        self.subscription_trident_resources = [
            {'type': 'deployment', 'namespace': 'openshift-operators', 'name': 'trident-operator'}
        ]

        self.instance_trident_resources = [
            {'type': 'deployment', 'namespace': 'trident', 'name': 'trident-controller'},
            {'type': 'daemonset', 'namespace': 'trident', 'name': 'trident-node-linux'}
        ]

    def is_trident_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)

    def create_trident_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
        
        if not wait:
            return True
        
        success = self.wait_subscription_trident(my_output=my_output)
        if not success:
            return False
        
        return True
    
    def delete_trident_subscription(self, namespace, name, my_output=None, wait=True):
        resources = self.get_subscription_resources(
            self.subscription_trident_resources + self.instance_trident_resources,
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

        success = self.wait_no_subscription_resources('trident', resources, my_output=my_output)
        if not success:
            return False

        return True

    def is_subscription_trident_ready(self, with_instance=False, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.subscription_trident_resources
        if with_instance:
            resources.extend(self.instance_trident_resources)

        return self.is_subscription_ready('trident', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)
    
    def wait_subscription_trident(self, with_instance=False, my_output=None):
        resources = self.subscription_trident_resources
        if with_instance:
            resources.extend(self.instance_trident_resources)

        return self.wait_subscription_resources('trident', resources, my_output=my_output)

    def wait_no_subscription_trident(self, my_output=None):
        resources = self.subscription_trident_resources
        resources.extend(self.instance_trident_resources)
        return self.wait_no_subscription_resources('trident', resources, my_output=my_output)