from lib.ocp.cluster.kubeconfig.output import OcpClusterKubeconfigOutput
from lib.ocp.cluster.vcenter.output import OcpClusterVcenterOutput


class OcpClusterOutput(
        OcpClusterKubeconfigOutput,
        OcpClusterVcenterOutput
        ):
    def __init__(self):
        OcpClusterKubeconfigOutput.__init__(self)
        OcpClusterVcenterOutput.__init__(self)

    def print_ocp_clusters(self, clusters):
        order = [
            'name',
            'kubeconfig',
            'virtctl.descr',
            'helm.descr',
            'tools.descr'
        ]

        headers = [
            'Name',
            'Kubeconfig',
            'Virtctl',
            'Helm',
            'Tools'
        ]

        for cluster in clusters:
            for key in ['virtctl', 'helm', 'tools']:
                if cluster[key] is None:
                    cluster[key] = {}
                    cluster[key]['descr'] = '--'
                else:
                    if cluster[key]['password'] is not None:
                        cluster[key]['descr'] = '%s@%s w/pass' % (
                            cluster[key]['username'],
                            cluster[key]['ip']
                        )
                    else:
                        cluster[key]['descr'] = '%s@%s w/key' % (
                            cluster[key]['username'],
                            cluster[key]['ip']
                        )

        self.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )

    def print_ocp_clusters_state(self, info):
        order = [
            'name',
            'online',
            'ocp',
            'version',
            'cni',
            'cluster.cidr',
            'cluster.hostPrefix',
            'service'
        ]

        headers = [
            'Name',
            'Online',
            'OCP',
            'Kubernetes',
            'CNI',
            'Cluster CIDR',
            'Prefix',
            'Service'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['cluster', 'service']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )
