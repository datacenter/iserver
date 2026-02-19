class K8sSubscriptionCnv():
    def __init__(self):
        self.subscription_cnv_deployments = [
            {'namespace': 'openshift-cnv', 'name': 'aaq-operator'},
            {'namespace': 'openshift-cnv', 'name': 'cdi-operator'},
            {'namespace': 'openshift-cnv', 'name': 'cluster-network-addons-operator'},
            {'namespace': 'openshift-cnv', 'name': 'hco-operator'},
            {'namespace': 'openshift-cnv', 'name': 'hco-webhook'},
            {'namespace': 'openshift-cnv', 'name': 'hostpath-provisioner-operator'},
            {'namespace': 'openshift-cnv', 'name': 'hyperconverged-cluster-cli-download'},
            {'namespace': 'openshift-cnv', 'name': 'ssp-operator'},
            {'namespace': 'openshift-cnv', 'name': 'virt-operator'}
        ]

    def is_cnv_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)
    
    def create_cnv_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_cnv_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_cnv_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_cnv(my_output=my_output)
            if not success:
                return False
        
        return True

    def is_subscription_cnv_ready(self):
        for deployment in self.subscription_cnv_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False
        return True
    
    def wait_subscription_cnv_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(self.subscription_cnv_deployments, my_output=my_output, optional=True)
        if not success:
            return False
        return True

    def wait_no_subscription_cnv(self, my_output=None):
        success = self.wait_no_deployments(self.subscription_cnv_deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True