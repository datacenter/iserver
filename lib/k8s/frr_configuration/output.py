import json


class K8sFrrConfigurationOutput():
    def __init__(self):
        pass

    def print_frr_configurations_state(self, info):
        if info is not None:
            for item in info:
                item['bodyT'] = json.dumps(item['spec'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Config', 'namespace_nameT'],
                ['Route Adv', 'ra'],
                ['Body', 'bodyT']
            ]
        )