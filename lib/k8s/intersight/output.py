import json


class K8sIntersightOutput():
    def __init__(self):
        pass

    def print_intersights(self, info):
        for item in info:
            item['specT'] = json.dumps(item['spec'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Intersight', 'namespace_nameT'],
                ['Spec', 'specT']
            ]
        )