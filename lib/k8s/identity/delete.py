class K8sIdentityDelete():
    def __init__(self):
        pass

    def delete_identity(
            self, 
            name, 
            my_output=None,
            wait=True
        ):
        success, deleted = self.delete_resource(
            'Identity', 
            'user.openshift.io/v1',
            name, 
            object_name='identity',
            my_output=my_output
        )
        if not success:
            return False
        
        if not deleted:
            return True
        
        if not wait:
            return True
        
        success = self.wait_no_identity(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    