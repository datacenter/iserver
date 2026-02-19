from lib.md.k8s.cluster import MdK8sClusterOutput
from lib.md.k8s.cni import MdK8sCniOutput
from lib.md.k8s.node import MdK8sNodeOutput


class MdK8sOutput(
        MdK8sClusterOutput,
        MdK8sCniOutput,
        MdK8sNodeOutput
    ):
    def __init__(self):
        MdK8sNodeOutput.__init__(self)

    def print_k8s(self):
        self.my_output.default('K8s node')
        for cluster_name in self.xd_handler.k8s_clusters:
            self.print_k8s_cluster(
                cluster_name
            )
            self.print_k8s_cni(
                cluster_name
            )
            self.print_k8s_nodes(
                cluster_name,
                self.xd_handler.k8s_node[cluster_name]
            )
