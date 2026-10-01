class K8sSubscriptionLvm():
    def __init__(self):
        self.subscription_lvm_resources = [
            {'type': 'deployment', 'namespace': 'openshift-storage', 'name': 'lvms-operator'}
        ]

        self.cluster_lvm_resources = [
            {'type': 'daemonset', 'namespace': 'openshift-storage', 'name': 'vg-manager'}
        ]

    def is_lvm_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)

    def create_lvm_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            'lvms', 
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
            success = self.wait_subscription_lvm_ready(my_output=my_output, with_lvm_cluster=False)
            if not success:
                return False
        
        return True
    
    def delete_lvm_subscription(self, namespace, name, my_output=None, wait=True):
        resources = self.get_subscription_resources(
            self.subscription_lvm_resources + self.cluster_lvm_resources,
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

        success = self.wait_no_subscription_resources('lvm', resources, my_output=my_output)
        if not success:
            return False

        return True

    def is_subscription_lvm_ready(self, with_instance=False, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.subscription_lvm_resources
        if with_instance:
            resources.extend(self.cluster_lvm_resources)

        return self.is_subscription_ready('lvm', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)
    
    def wait_subscription_lvm_ready(self, with_lvm_cluster=True, my_output=None):
        resources = self.subscription_lvm_resources
        if with_lvm_cluster:
            resources.extend(self.cluster_lvm_resources)

        return self.wait_subscription_resources('lvm', resources, my_output=my_output)

    def wait_no_subscription_lvm(self, my_output=None):
        resources = self.subscription_lvm_resources
        resources.extend(self.cluster_lvm_resources)
        return self.wait_no_subscription_resources('lvm', resources, my_output=my_output)