class K8sPrivateNetworkEndpointSliceOutput():
    def __init__(self):
        pass

    def print_private_network_endpoint_slices_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Private Network Endpoint Slice', 'namespace_nameT'],
                ['Network', 'endpointT.network'],
                ['Endpoint', 'endpointT.name'],
                ['POD IP', 'endpointT.pod_ip'],
                ['IP', 'endpointT.ip'],
                ['MAC', 'endpointT.mac'],
                ['When', 'endpointT.when']
            ]
        )