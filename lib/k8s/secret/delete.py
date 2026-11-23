class K8sSecretDelete():
    def __init__(self):
        pass

    def delete_secret(self, namespace, name, my_output=None, wait=True):
        success, deleted = self.delete_resource(
            'Secret', 
            'v1',
            name, 
            namespace=namespace, 
            object_name='secret',
            my_output=my_output
        )
        if not success:
            return False
        
        if not deleted:
            return True
        
        if not wait:
            return True

        success = self.wait_no_secret(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    