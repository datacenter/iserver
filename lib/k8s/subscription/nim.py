class K8sSubscriptionNim():
    def __init__(self):
        self.subscription_nim_deployments = [
            {'namespace': 'openshift-operators', 'name': 'k8s-nim-operator'}
        ]

    def create_nim_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_nim_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_nim_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_nim(my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_nim_ready(self):
        for deployment in self.subscription_nim_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False

        return True
    
    def wait_subscription_nim_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(
            self.subscription_nim_deployments, 
            my_output=my_output, 
            optional=True
        )
        if not success:
            return False

        return True

    def wait_no_subscription_nim(self, my_output=None):
        pods = []

        for deployment in self.subscription_nim_deployments:
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
            self.subscription_nim_deployments, 
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