class K8sGroupDelete():
    def __init__(self):
        pass

    def delete_group(
            self, 
            name, 
            my_output=None,
            wait=True
        ):
        success = self.delete_resource(
            'Group', 
            'user.openshift.io/v1',
            name, 
            object_name='group',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_group(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True