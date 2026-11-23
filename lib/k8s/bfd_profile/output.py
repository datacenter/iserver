import json


class K8sBfdProfileOutput():
    def __init__(self):
        pass

    def print_bfd_profiles(self, info):
        for item in info:
            item['specT'] = json.dumps(item['spec'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['BGP Peer', 'namespace_nameT'],
                ['Spec', 'specT']
            ]
        )