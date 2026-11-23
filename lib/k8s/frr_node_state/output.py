from lib import filter_helper


class K8sFrrNodeStateOutput():
    def __init__(self):
        pass

    def print_frr_node_states(self, info):
        if info is not None:
            for item in info:
                item['configT'] = filter_helper.get(item, 'status:runningConfig', on_error='', on_none='').split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Node', 'name'],
                ['Conversion', 'last_conversionT'],
                ['Reload', 'last_reloadT'],
                ['Config', 'configT']
            ]
        )
