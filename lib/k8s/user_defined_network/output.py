import json


class K8sUserDefinedNetworkOutput():
    def __init__(self):
        pass

    def print_user_defined_networks_state(self, info):
        for item in info:
            item['nadT'] = None
            if item['nad'] is not None:
                item['nadT'] = json.dumps(
                    item['nad'],
                    indent=2
                ).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['UDN', 'namespace_nameT'],
                ['C', 'createdTick'],
                ['A', 'allocatedTick'],
                ['P', 'primaryTick'],
                ['Topology', 'topology'],
                ['Subnet', 'subnetT'],
                ['Errors', 'reasonT'],
                ['Net Attach Def', 'nadT'],
                ['Workload', 'app']
            ],
            remove_empty=['reasonT']
        )

