import json
from lib import filter_helper


class K8sBgpAdvertisementOutput():
    def __init__(self):
        pass

    def print_bgp_advertisements(self, info):
        for item in info:
            item['specT'] = json.dumps(filter_helper.get(item, 'spec', on_error={}, on_none={}), indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['BGP Advertisement', 'namespace_nameT'],
                ['Spec', 'specT']
            ]
        )