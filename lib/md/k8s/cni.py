class MdK8sCniOutput():
    def __init__(self):
        pass

    def print_k8s_cni(self, cluster_name):
        self.print_page_header('Kubernetes Cluster - CNI')

        self.my_output.print_stream('## Overview', 'output')
        self.my_output.print_stream('', 'output')
        self.my_output.print_stream('- Cluster: [%s](./cluster-%s.md)' % (cluster_name, cluster_name), 'output')
        self.my_output.print_stream('- CNI Type: %s' % (self.xd_handler.get_k8s_cni_type(cluster_name)), 'output')
        self.my_output.print_stream('- POD CIDR: %s' % (self.xd_handler.get_k8s_cni_pod_cidr(cluster_name)), 'output')
        self.my_output.print_stream('- Service CIDR: %s' % (self.xd_handler.get_k8s_cni_service_cidr(cluster_name)), 'output')

        self.save_output('cni-%s' % (cluster_name), subdir='ocp')
