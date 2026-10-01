class K8sSubscriptionServerless():
    def __init__(self):
        self.subscription_serverless_resources = [
            {'type': 'deployment', 'namespace': 'openshift-serverless', 'name': 'knative-openshift'},
            {'type': 'deployment', 'namespace': 'openshift-serverless', 'name': 'knative-openshift-ingress'},
            {'type': 'deployment', 'namespace': 'openshift-serverless', 'name': 'knative-operator-webhook'}
        ]

    def create_serverless_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_serverless_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_serverless_subscription(self, namespace, name, my_output=None, wait=True):
        resources = self.get_subscription_resources(
            self.subscription_serverless_resources,
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
        
        success = self.wait_no_subscription_resources('serverless', resources, my_output=my_output)
        if not success:
            return False
        
        return True

    def is_subscription_serverless_ready(self, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.subscription_serverless_resources
        return self.is_subscription_ready('serverless', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)
    
    def wait_subscription_serverless_ready(self, my_output=None):
        resources = self.subscription_serverless_resources
        return self.wait_subscription_resources('serverless', resources, my_output=my_output)