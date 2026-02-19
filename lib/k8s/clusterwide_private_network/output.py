class K8sClusterwidePrivateNetworkOutput():
    def __init__(self):
        pass

    def print_clusterwide_private_networks(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Clusterwide Private Network', 'name'],
                ['CIDRv4', 'cidrv4'],
                ['CIDRv6', 'cidrv6'],
                ['Route', 'destT'],
                ['Via', 'gatewayT'],
                ['POD', 'podT'],
                ['Bridge', 'inb']
            ]
        )
    
    def print_clusterwide_private_network_endpoints_db(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Clusterwide Private Network', 'network'],
                ['Endpoint IP', 'private_ip'],
                ['Endpoint MAC', 'private_mac'],
                ['Cluster', 'cluster'],
                ['Node', 'node_name'],
                ['Namespace', 'namespace'],
                ['Name', 'name'],
                ['POD IP', 'pod_ip'],
                ['Since', 'since'],
            ]
        )
