class K8sDataScienceClusterInitializationOutput():
    def __init__(self):
        pass

    def print_data_science_cluster_initializations(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Data Science Cluster Initialization', 'name'],
                ['Version', 'release'],
                ['Ready', 'readyTick'],
                ['Components', 'componentT']
            ]
        )
