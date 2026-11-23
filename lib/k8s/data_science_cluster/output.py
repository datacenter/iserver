class K8sDataScienceClusterOutput():
    def __init__(self):
        pass

    def print_data_science_clusters(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Data Science Cluster', 'name'],
                ['Version', 'release'],
                ['Ready', 'readyTick'],
                ['Components', 'componentT'],
                ['Disabled', 'disabled'],
                ['Release Name', 'release_name'],
                ['Release Version', 'release_version'],
            ]
        )
