class K8sSubscriptionPortworx():
    def __init__(self):
        self.subscription_portworx_deployments = [
            {'namespace': 'openshift-operators', 'name': 'portworx-operator'}
        ]

    def create_portworx_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            name, 
            'Automatic',
            name,
            'certified-operators', 
            'openshift-marketplace', 
            channel=channel,
            include_starting_csv=True,
            confirmation=confirmation,
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_subscription_portworx_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_portworx_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_portworx(my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_portworx_ready(self):
        for deployment in self.subscription_portworx_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False

        return True
    
    def wait_subscription_portworx_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(
            self.subscription_portworx_deployments, 
            my_output=my_output, 
            optional=True
        )
        if not success:
            return False

        return True

    def wait_no_subscription_portworx(self, my_output=None):
        success = self.wait_no_deployments(
            self.subscription_portworx_deployments, 
            my_output=my_output, 
            optional=False
        )
        if not success:
            return False

        return True