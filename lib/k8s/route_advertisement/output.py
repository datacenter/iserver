import json


class K8sRouteAdvertisementOutput():
    def __init__(self):
        pass

    def print_route_advertisements_state(self, info):
        if info is not None:
            for item in info:
                item['bodyT'] = json.dumps(item['spec'], indent=2).split('\n')
                if 'frr' in item:
                    item['frrT'] = json.dumps(item['frr'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Route Adv', 'name'],
                ['Accepted', 'acceptedTick'],
                ['Config', 'bodyT'],
                ['FRR', 'frrT']
            ]
        )
