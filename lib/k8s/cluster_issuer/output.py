class K8sClusterIssuerOutput():
    def __init__(self):
        pass

    def print_cluster_issuers_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Cluster Issuer', 'name'],
                ['Secret', 'secretT'],
                ['Certificate', 'crtT'],
                ['Ready', 'readyT']
            ]
        )