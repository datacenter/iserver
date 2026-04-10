class K8sNodeFeatureDiscoveryOutput():
    def __init__(self):
        pass

    def print_node_feature_discoverys(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Node Feature Discovery', 'namespace_nameT']
            ]
        )