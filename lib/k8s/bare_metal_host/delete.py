class K8sBareMetalHostDelete():
    def __init__(self):
        pass

    def delete_bare_metal_host(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'BareMetalHost', 
            'metal3.io/v1alpha1',
            name, 
            namespace=namespace, 
            object_name='bare_metal_host',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True

        success = self.wait_no_bare_metal_host(
            namespace,
            name,
            max_time=180,
            my_output=my_output
        )
        if not success:
            return False

        return True
