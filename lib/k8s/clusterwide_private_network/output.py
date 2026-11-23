import json


class K8sClusterwidePrivateNetworkOutput():
    def __init__(self):
        pass

    def print_clusterwide_private_networks_state(self, info):
        for item in info:
            item['subnetT'] = json.dumps(
                item['subnet'],
                indent=2
            ).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Clusterwide Private Network', 'name'],
                ['Subnet', 'subnet.name'],
                ['DHCP', 'subnet.dhcp.mode'],
                ['CIDRv4', 'subnet.cidrv4'],
                ['CIDRv6', 'subnet.cidrv6'],
                ['POD', 'podT'],
                ['Bridge', 'inb'],
                ['Multus Namespace', 'ns'],
                ['NAD', 'nad']
            ],
            cast_zero=True
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
