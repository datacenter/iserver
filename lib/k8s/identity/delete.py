class K8sIdentityDelete():
    def __init__(self):
        pass

    def delete_identity(
            self, 
            name, 
            my_output=None,
            wait=True
        ):
        if my_output is not None:
            my_output.default('Delete Identity', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        info = self.get_identity(name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        success = self.delete_resource(
            'Identity', 
            'user.openshift.io/v1',
            name, 
            object_name='identity',
            my_output=my_output
        )
        if not success:
            return False
        
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
    