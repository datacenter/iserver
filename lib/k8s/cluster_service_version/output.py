class K8sClusterServiceVersionOutput():
    def __init__(self):
        pass

    def print_cluster_service_versions(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Cluster Service Version', 'namespace_nameT'],
                ['Type', 'display_name'],
                ['Provider', 'provider_name'],
                ['Version', 'version'],
                ['Maturity', 'maturityT'],
                ['Phase', 'phase'],
                ['Age', 'age']
            ]
        )

    def print_cluster_service_version(self, item):
        self.my_output.dictionary_ng(
            'Cluster Service Version',
            item,
            [
                ['Namespace', 'namespace'],
                ['Name', 'name'],
                ['Type', 'display_name'],
                ['Provider', 'provider_name'],
                ['Version', 'version'],
                ['Maturity', 'maturityT'],
                ['Phase', 'phase'],
                ['Age', 'age']
            ]
        )