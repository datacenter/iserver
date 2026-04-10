class K8sBgpAdvertisementUpdate():
    def __init__(self):
        pass

    def update_bgp_advertisement(
            self, 
            body, 
            replace=True,
            confirmation=False, 
            my_output=None
        ):
        if replace:
            if not self.replace_resource(body, object_name='bgp_advertisement', my_output=my_output, confirmation=confirmation):
                return False
        else:
            if not self.patch_resource(body, object_name='bgp_advertisement', my_output=my_output, confirmation=confirmation):
                return False

        return True    