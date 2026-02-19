import time


class K8sSubscriptionTrident():
    def __init__(self):
        pass

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
        
        if wait:
            success = self.wait_subscription_trident(my_output=my_output)
            if not success:
                return False
        
        return True
    
    def delete_trident_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_trident(my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)

        return True

    def wait_subscription_trident(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-operators', 'name': 'trident-operator'}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        return True

    def wait_no_subscription_trident(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-operators', 'name': 'trident-operator'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        return True
