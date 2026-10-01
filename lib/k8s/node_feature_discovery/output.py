import json
from lib import filter_helper


class K8sNodeFeatureDiscoveryOutput():
    def __init__(self):
        pass

    def print_node_feature_discoverys(self, info):
        for item in info:           
            item['configT'] = filter_helper.get(item, 'spec:workerConfig:configData', on_error='', on_none='').split('\n')
            spec = item['spec']
            spec['workerConfig'] = dict(configData={})
            item['specT'] = json.dumps(
                spec,
                indent=2
            ).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Node Feature Discovery', 'namespace_nameT'],
                ['Conditions', 'condition'],
                ['Spec', 'specT'],
                ['Config Data', 'configT']
            ]
        )