class K8sServiceAccountDelete():
    def __init__(self):
        pass

    def delete_service_account(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'ServiceAccount', 
            'v1',
            name, 
            namespace=namespace, 
            object_name='service_account',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_service_account(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
        return True
