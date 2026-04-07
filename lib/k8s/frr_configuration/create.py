class K8sFrrConfigurationCreate():
    def __init__(self):
        pass

    def create_frr_configuration(self, body, confirmation=False, my_output=None, wait=True):
        namespace = self.get(body, 'metadata:namespace')
        name = self.get(body, 'metadata:name')

        if not self.create_resource(body, object_name='frr_configuration', my_output=my_output, confirmation=confirmation):
            return None

        if not wait:
            return True

        success = self.wait_frr_configuration(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        return True

    def create_or_update_frr_configuration(self, body, confirmation=False, my_output=None, wait=True):
        namespace = self.get(body, 'metadata:namespace')
        name = self.get(body, 'metadata:name')

        if self.is_frr_configuration(namespace, name, cache_enabled=False):
            return self.update_frr_configuration(
                body,
                confirmation=confirmation, 
                my_output=my_output,
                wait=wait
            )

        return self.create_frr_configuration(
            body,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )
