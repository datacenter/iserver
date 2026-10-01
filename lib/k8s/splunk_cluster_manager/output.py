class K8sSplunkClusterManagerOutput():
    def __init__(self):
        pass

    def print_splunk_cluster_managers_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Splunk Cluster Manager', 'namespace_nameT']
            ]
        )