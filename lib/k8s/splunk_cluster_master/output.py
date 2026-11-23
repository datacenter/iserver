class K8sSplunkClusterMasterOutput():
    def __init__(self):
        pass

    def print_splunk_cluster_masters_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Splunk Cluster Master', 'namespace_nameT']
            ]
        )