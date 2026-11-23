import json


class K8sBgpPeerOutput():
    def __init__(self):
        pass

    def print_bgp_peers(self, info):
        for item in info:
            item['specT'] = json.dumps(item['spec'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['BGP Peer', 'namespace_nameT'],
                ['Spec', 'specT']
            ]
        )