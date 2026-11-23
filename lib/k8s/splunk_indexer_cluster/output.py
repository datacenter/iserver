class K8sSplunkIndexerClusterOutput():
    def __init__(self):
        pass

    def print_splunk_indexer_clusters_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Splunk Indexer Cluster', 'namespace_nameT']
            ]
        )