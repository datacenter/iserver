class K8sSplunkSearchHeadClusterOutput():
    def __init__(self):
        pass

    def print_splunk_search_head_clusters_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Splunk Search Head Cluster', 'namespace_nameT']
            ]
        )