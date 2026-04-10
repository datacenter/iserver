class K8sBfdProfileUpdate():
    def __init__(self):
        pass

    def update_bfd_profile(
            self, 
            body, 
            replace=True,
            confirmation=False, 
            my_output=None
        ):
        if replace:
            if not self.replace_resource(body, object_name='bfd_profile', my_output=my_output, confirmation=confirmation):
                return False
        else:
            if not self.patch_resource(body, object_name='bfd_profile', my_output=my_output, confirmation=confirmation):
                return False

        return True    