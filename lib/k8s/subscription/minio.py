class K8sSubscriptionMinio():
    def __init__(self):
        self.subscription_minio_deployments = [
            {'namespace': 'aistor', 'name': 'adminjob-operator'},
            {'namespace': 'aistor', 'name': 'object-store-operator'}
        ]

    def create_minio_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_minio_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_minio_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_minio(my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_minio_ready(self):
        for deployment in self.subscription_minio_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False

        return True
    
    def wait_subscription_minio_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(
            self.subscription_minio_deployments, 
            my_output=my_output, 
            optional=True
        )
        if not success:
            return False

        return True

    def wait_no_subscription_minio(self, my_output=None):
        pods = self.get_pods(
            object_filter=['namespace:aistor']
        )
        if pods is None:
            return False
        
        success = self.wait_no_deployments(
            self.subscription_minio_deployments, 
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