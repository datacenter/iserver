class K8sSubscriptionWebTerminal():
    def __init__(self):
        self.subscription_web_terminal_deployments = [
            {'namespace': 'openshift-operators', 'name': 'web-terminal-controller'},
            {'namespace': 'openshift-operators', 'name': 'devworkspace-controller-manager'},
            {'namespace': 'openshift-operators', 'name': 'devworkspace-webhook-server'},
        ]

    def create_web_terminal_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_web_terminal_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_web_terminal_subscription(self, namespace, name, workspace_package_name, service='devworkspace-webhookserver', my_output=None, wait=True):
        if not self.delete_dev_workspace_templates(my_output=my_output, wait=wait):
            return False

        success = self.delete_subscription(
            namespace, 
            workspace_package_name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
                                
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        for deployment in self.subscription_web_terminal_deployments:
            if self.is_deployment(deployment['namespace'], deployment['name'], cache_enabled=False):
                success = self.delete_deployment(deployment['namespace'], deployment['name'], my_output=my_output, wait=wait)
                if not success:
                    return False
                
        deployments = self.get_deployments(object_filter=['namespace:openshift-terminal'])
        if deployments is not None:
            for deployment in deployments:
                success = self.delete_deployment(deployment['namespace'], deployment['name'], my_output=my_output, wait=wait)
                if not success:
                    return False
   
        services = self.get_services(object_filter=['namespace:openshift-terminal'])
        if services is not None:
            for service in services:
                success = self.delete_service(service['namespace'], service['name'], my_output=my_output, wait=wait)
                if not success:
                    return False
                
        if wait:
            success = self.wait_no_subscription_web_terminal(my_output=my_output)
            if not success:
                return False
        
        if service is not None:
            if self.is_service(namespace, service, cache_enabled=False):
                success = self.delete_service(namespace, service, my_output=my_output, wait=wait)
                if not success:
                    return False
                
        return True

    def is_subscription_web_terminal_ready(self):
        for deployment in self.subscription_web_terminal_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False

        return True
    
    def wait_subscription_web_terminal_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(
            self.subscription_web_terminal_deployments, 
            my_output=my_output, 
            optional=True
        )
        if not success:
            return False

        return True

    def wait_no_subscription_web_terminal(self, my_output=None):
        pods = []

        for deployment in self.subscription_web_terminal_deployments:
            replica_set = self.get_replica_set_deployment(deployment['namespace'], deployment['name'], cache_enabled=False)
            if replica_set is None:
                # probably already deleted
                continue
        
            rs_pods = self.get_pods_replica_set(deployment['namespace'], replica_set['name'], cache_enabled=False)
            if rs_pods is None:
                # probably already deleted
                continue
                
            for pod in rs_pods:
                pods.append(pod)

        success = self.wait_no_deployments(
            self.subscription_web_terminal_deployments, 
            my_output=my_output, 
            optional=False
        )
        if not success:
            return False
        
        if my_output is not None:
            my_output.default('Wait for pods deleted...')
            
        for pod in pods:
            if my_output is not None:
                my_output.default('- %s/%s' % (pod['namespace'], pod['name']))

            success = self.wait_no_pod(
                pod['namespace'],
                pod['name'],
                max_time=180
            )
            if not success:
                return False
            
        return True