class K8sFrrConfigurationDelete():
    def __init__(self):
        pass

    def delete_frr_configuration(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'FRRConfiguration', 
            'frrk8s.metallb.io/v1beta1',
            name, 
            namespace=namespace, 
            object_name='frr_configuration',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_frr_configuration(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
        return True
