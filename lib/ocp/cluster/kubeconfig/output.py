class OcpClusterKubeconfigOutput():
    def __init__(self):
        pass

    def print_ocp_cluster_kubeconfig(self, info):
        order = [
            'name',
            'parameters.ocp.installation',
            'parameters.ocp.release',
            'parameters.cni.type',
            'kubeconfigFileTick',
            'apiFqdn',
            'apiVip',
            'apiDns'
        ]

        headers = [
            'Name',
            'Type',
            'Release',
            'CNI',
            'Kubeconfig',
            'API FQDN',
            'API VIP',
            'API DNS'
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

    def print_ocp_clusters_kubeconfig(self, clusters):
        order = [
            'name',
            'installation',
            'release',
            'cni',
            'kubeconfigFileTick',
            'apiFqdn',
            'apiVip',
            'apiDns',
            'kubeApiTick'
        ]

        headers = [
            'Name',
            'Type',
            'Release',
            'CNI',
            'Kubeconfig',
            'API FQDN',
            'API VIP',
            'API DNS',
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
