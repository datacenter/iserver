class K8sFrrConfigurationUpdate():
    def __init__(self):
        pass

    def update_frr_configuration(self, body, confirmation=False, my_output=None, wait=True):
        if not self.replace_resource(body, object_name='frr_configuration', my_output=my_output, confirmation=confirmation):
            return False

        return True
