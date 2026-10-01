import json


class K8sTetragonNetworkPolicyOutput():
    def __init__(self):
        pass

    def print_tetragon_network_policys_state(self, info):
        for item in info:
            item['specT'] = json.dumps(item['spec'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Tetragon Network Policy', 'name'],
                ['Spec', 'specT']
            ]
        )