class K8sNodeNetworkStateDnsInfo():
    def __init__(self):
        pass

    def get_node_network_state_dns_info(self, managed_object):
        info = {}
        info['search'] = self.get(
            managed_object,
            'status:currentState:dns-resolver:running:search'
        )
        info['server'] = self.get(
            managed_object,
            'status:currentState:dns-resolver:running:server'
        )

        return info