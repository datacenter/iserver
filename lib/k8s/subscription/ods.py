class K8sSubscriptionOds():
    def __init__(self):
        self.subscription_ods_deployments = [
            {'namespace': 'redhat-ods-operator', 'name': 'rhods-operator'}
        ]

    def create_ods_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_ods_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_ods_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_ods(my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_ods_ready(self):
        for deployment in self.subscription_ods_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False
        return True
    
    def wait_subscription_ods_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(self.subscription_ods_deployments, my_output=my_output, optional=True)
        if not success:
            return False
        return True

    def wait_no_subscription_ods(self, my_output=None):
        success = self.wait_no_deployments(self.subscription_ods_deployments, my_output=my_output, optional=False)
        if not success:
            return False
        return True