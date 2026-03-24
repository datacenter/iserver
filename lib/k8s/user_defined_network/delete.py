class K8sUserDefinedNetworkDelete():
    def __init__(self):
        pass

    def delete_user_defined_network(self, namespace, name, my_output=None, wait=True):
        info = self.get_user_defined_network(
            namespace,
            name,
            cache_enabled=False
        )

        success = self.delete_resource(
            'UserDefinedNetwork', 
            'k8s.ovn.org/v1',
            name, 
            namespace=namespace, 
            object_name='user_defined_network',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_user_defined_network(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        if info is None:
            return True

        return success            
