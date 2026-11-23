class K8sClusterUserDefinedNetworkDelete():
    def __init__(self):
        pass

    def delete_cluster_user_defined_network(self, name, my_output=None, wait=True):
        success, deleted = self.delete_resource(
            'ClusterUserDefinedNetwork', 
            'k8s.ovn.org/v1',
            name, 
            object_name='cluster_user_defined_network',
            my_output=my_output
        )
        if not success:
            return False

        if not deleted:
            return True
                
        if not wait:
            return True
        
        success = self.wait_no_cluster_user_defined_network(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return success            
