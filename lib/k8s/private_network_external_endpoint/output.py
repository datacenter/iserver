class K8sPrivateNetworkExternalEndpointOutput():
    def __init__(self):
        pass

    def print_private_network_external_endpoints_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Private Network External Endpoint', 'namespace_nameT']
            ]
        )