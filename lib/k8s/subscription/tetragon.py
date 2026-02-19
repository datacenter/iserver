import time


class K8sSubscriptionTetragon():
    def __init__(self):
        pass

    def is_tetragon_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)
    
    def create_tetragon_subscription(self, namespace, name, catalog_namespace, catalog_name, channel, confirmation=False, my_output=None, wait=True):
        labels = {}
        labels['operators.coreos.com/%s.%s' % (name, namespace)] = ''

        success = self.create_subscription(
            namespace, 
            name, 
            'Automatic',
            name,
            catalog_name, 
            catalog_namespace, 
            channel=channel,
            labels=labels,
            confirmation=confirmation,
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            info = self.get_subscription(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                success = self.wait_subscription_tetragon_ready(my_output=my_output)
                if not success:
                    return False
        
        return True

    def delete_tetragon_subscription(self, namespace, name, my_output=None, wait=True):
        info = self.get_subscription(
            namespace,
            name,
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
        
        if wait and info is not None:
            success = self.wait_no_subscription_tetragon(my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)

        return True

    def wait_subscription_tetragon_ready(self, my_output=None):
        deployments = [
            {'namespace': 'tetragon', 'name': 'tetragon-operator'}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        return True

    def wait_no_subscription_tetragon(self, my_output=None):
        deployments = [
            {'namespace': 'tetragon', 'name': 'tetragon-operator'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        return True