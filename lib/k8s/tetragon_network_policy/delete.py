class K8sTetragonNetworkPolicyDelete():
    def __init__(self):
        pass

    def delete_tetragon_network_policy(self, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'TetragonNetworkPolicy', 
            'cilium.io/v1alpha1',
            name, 
            'tetragon_network_policy',
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        return success
    
    def delete_tetragon_network_policys(self, my_output=None, wait=True):
        items = self.get_tetragon_network_policys(
            cache_enabled=False
        )
        if items is None:
            if my_output is not None:
                my_output.error('Failed to get tetragon network policy')
            return False
        
        for item in items:
            success = self.delete_tetragon_network_policy(
                item['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True