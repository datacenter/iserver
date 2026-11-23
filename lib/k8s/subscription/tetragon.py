class K8sSubscriptionTetragon():
    def __init__(self):
        self.subscription_tetragon_resources = [
            {'type': 'deployment', 'namespace': 'tetragon', 'name': 'tetragon-operator'},
            {'type': 'daemonset', 'namespace': 'tetragon', 'name': 'tetragon'}
        ]

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
        resources = self.get_subscription_resources(
            self.subscription_tetragon_resources,
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

        success = self.delete_config_map(
            'tetragon',
            'tetragon-operator-config',
            my_output=my_output,
            wait=True
        )
        
        success = self.wait_no_subscription_resources('tetragon', resources, my_output=my_output)
        if not success:
            return False
        
        return True

    def wait_subscription_tetragon_ready(self, my_output=None):
        return self.wait_subscription_resources('tetragon', self.subscription_tetragon_resources, my_output=my_output)

    def wait_no_subscription_tetragon(self, my_output=None):
        return self.wait_no_subscription_resources('tetragon', self.subscription_tetragon_resources, my_output=my_output)