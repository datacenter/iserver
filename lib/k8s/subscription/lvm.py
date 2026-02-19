import time


class K8sSubscriptionLvm():
    def __init__(self):
        pass

    def is_lvm_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)

    def create_lvm_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            'lvms', 
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
            success = self.wait_subscription_lvm_ready(my_output=my_output, with_lvm_cluster=False)
            if not success:
                return False
        
        return True
    
    def delete_lvm_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False

        if wait:        
            success = self.wait_no_subscription_lvm(my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)
                    
        return True

    def is_subscription_lvm_ready(self):
        deployments = [
            {'namespace': 'openshift-storage', 'name': 'lvms-operator'}
        ]

        for deployment in deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name'], cache_enabled=False):
                return False

        daemon_sets = [
            {'namespace': 'openshift-storage', 'name': 'vg-manager'}
        ]
        for daemon_set in daemon_sets:
            if self.is_daemon_set(daemon_set['namespace'], daemon_set['name'], cache_enabled=False):
                if not self.is_daemon_set_ready(daemon_set['namespace'], daemon_set['name'], cache_enabled=False):
                    return False
            
        return True

    def wait_subscription_lvm_ready(self, my_output=None, with_lvm_cluster=True):
        deployments = [
            {'namespace': 'openshift-storage', 'name': 'lvms-operator'}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        if with_lvm_cluster:
            daemon_sets = [
                {'namespace': 'openshift-storage', 'name': 'vg-manager'}
            ]
            success = self.wait_daemon_sets_ready_state(daemon_sets, my_output=my_output, optional=False)
            if not success:
                return False
        
        return True

    def wait_no_subscription_lvm(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-storage', 'name': 'lvms-operator'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        daemon_sets = [
            {'namespace': 'openshift-storage', 'name': 'vg-manager'}
        ]
        success = self.wait_no_daemon_sets(daemon_sets, my_output=my_output, optional=False)
        if not success:
            return False

        return True