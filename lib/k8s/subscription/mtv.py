class K8sSubscriptionMtv():
    def __init__(self):
        self.subscription_mtv_deployments = [
            {'namespace': 'openshift-mtv', 'name': 'forklift-operator'}
        ]

        self.instance_mtv_deployments = [
            {'namespace': 'openshift-mtv', 'name': 'forklift-api'},
            {'namespace': 'openshift-mtv', 'name': 'forklift-cli-download'},
            {'namespace': 'openshift-mtv', 'name': 'forklift-controller'},
            {'namespace': 'openshift-mtv', 'name': 'forklift-ova-proxy'},
            {'namespace': 'openshift-mtv', 'name': 'forklift-ui-plugin'},
            {'namespace': 'openshift-mtv', 'name': 'forklift-validation'},
            {'namespace': 'openshift-mtv', 'name': 'forklift-volume-populator-controller'}
        ]

    def is_mtv_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)
    
    def create_mtv_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_mtv_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_mtv_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_mtv(my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_mtv_ready(self):
        for deployment in self.subscription_mtv_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False
        return True
    
    def wait_subscription_mtv_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(self.subscription_mtv_deployments, my_output=my_output, optional=True)
        if not success:
            return False
        return True

    def wait_no_subscription_mtv(self, my_output=None):
        success = self.wait_no_deployments(self.subscription_mtv_deployments, my_output=my_output, optional=False)
        if not success:
            return False
        return True
    
    def is_instance_mtv_ready(self):
        for deployment in self.instance_mtv_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False
        return True
    
    def wait_instance_mtv_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(self.instance_mtv_deployments, my_output=my_output, optional=True)
        if not success:
            return False
        return True

    def wait_no_instance_mtv(self, my_output=None):
        success = self.wait_no_deployments(self.instance_mtv_deployments, my_output=my_output, optional=False)
        if not success:
            return False
        return True