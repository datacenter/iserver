class OcpClusterKubeconfigOutput():
    def __init__(self):
        pass

    def print_ocp_cluster_kubeconfig(self, info):
        order = [
            'name',
            'kubeconfigFileTick',
            'apiFqdn',
            'apiVip'
        ]

        headers = [
            'Name',
            'Kubeconfig',
            'API FQDN',
            'API VIP'
        ]

        if 'kubeApiTick' in info:
            order.append('kubeApiTick')
            headers.append('K8s API')

        self.my_output.dictionary(
            info,
            title='OCP Kubeconfig',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_ocp_clusters_kubeconfig(self, clusters, title=False):
        if title:
            self.my_output.default(
                'OCP Kubeconfig [#%s]' % (len(clusters)),
                underline=True,
                before_newline=True
            )

        if len(clusters) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'kubeconfigFilename',
            'apiFqdn',
            'apiVip',
            'kubeApiTick'
        ]

        headers = [
            'Cluster Name',
            'Kubeconfig',
            'API FQDN',
            'API VIP',
            'K8s API'
        ]

        self.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            table=True
        )
