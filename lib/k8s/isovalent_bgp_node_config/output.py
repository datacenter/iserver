class K8sIsovalentBGPNodeConfigOutput():
    def __init__(self):
        pass

    def print_isovalent_bgp_node_configs(self, info):
        peers = []
        for item in info:
            peers = peers + item['peer']

        self.my_output.my_table_ng(
            peers,
            [
                ['Node', 'node'],
                ['Instance', 'instance'],
                ['ASN', 'local_asn'],
                ['Peer', 'name'],
                ['Peer IP', 'ip'],
                ['Peer ASN', 'peer_asn'],
                ['State', 'state'],
                ['Keepalive', 'keepalive_time'],
                ['Hold', 'hold_time'],
                ['AFI', 'route.afi'],
                ['SAFI', 'route.safi'],
                ['Adv', 'route.advertised']
            ]
        )
