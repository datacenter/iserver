class K8sSubscriptionIntersight():
    def __init__(self):
        self.subscription_intersight_resources = [
            {'type': 'deployment', 'namespace': 'cisco-intersight', 'name': 'cisco-intersight-operator'}
        ]

        self.instance_intersight_resources = [
            {'type': 'deployment', 'namespace': 'cisco-intersight', 'name': 'cisco-intersight-api'},
            {'type': 'deployment', 'namespace': 'cisco-intersight', 'name': 'intersight-plugin-console-plugin'},
            {'type': 'daemonset', 'namespace': 'cisco-intersight', 'name': 'ucs-serial-discover'}
        ]

        self.ucs_tool_intersight_resources = [
            {'type': 'daemonset', 'namespace': 'cisco-intersight', 'name': 'ucs-tool'}
        ]

    def create_intersight_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_intersight_ready(my_output=my_output, with_instance=False)
            if not success:
                return False
        
        return True

    def delete_intersight_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_intersight(my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_intersight_ready(self, with_instance=False, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.subscription_intersight_resources
        if with_instance:
            resources.extend(self.instance_intersight_resources)

        return self.is_subscription_ready('intersight', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)
    
    def wait_subscription_intersight_ready(self, with_instance=False, ucs_tool=False, my_output=None):
        resources = self.subscription_intersight_resources
        if with_instance:
            resources.extend(self.instance_intersight_resources)
        if ucs_tool:
            resources.extend(self.ucs_tool_intersight_resources)

        return self.wait_subscription_resources_ready('intersight', resources, my_output=my_output)

    def wait_no_subscription_intersight(self, my_output=None):
        resources = self.subscription_intersight_resources
        resources.extend(self.instance_intersight_resources)
        for item in self.ucs_tool_intersight_resources:
            item['optional'] = True
            resources.append(item)
        return self.wait_no_subscription_resources('intersight', resources, my_output=my_output)

    def wait_no_subscription_intersight_instance(self, my_output=None):
        resources = self.instance_intersight_resources
        return self.wait_no_subscription_resources('intersight', resources, my_output=my_output)    