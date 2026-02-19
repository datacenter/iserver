class MdK8sClusterOutput():
    def __init__(self):
        pass

    def print_k8s_cluster(self, cluster_name):
        self.print_page_header('Kubernetes Cluster')

        self.my_output.print_stream('## Overview', 'output')
        self.my_output.print_stream('', 'output')
        self.my_output.print_stream('- Cluster: %s' % (cluster_name), 'output')
        self.my_output.print_stream('- OCP Versions: %s' % (self.xd_handler.get_k8s_version_ocp(cluster_name)), 'output')
        self.my_output.print_stream('- Kube Versions: %s' % (self.xd_handler.get_k8s_version_kube(cluster_name)), 'output')
        self.my_output.print_stream(
            '- CNI Type: [%s](./cni-%s.md)' % (
                self.xd_handler.get_k8s_cni_type(cluster_name),
                cluster_name
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Nodes: [#%s](./nodes-%s.md)' % (
                self.xd_handler.k8s_node_counts[cluster_name],
                cluster_name
            ),
            'output'
        )

        operators = self.xd_handler.get_k8s_co(cluster_name)
        if operators is not None and len(operators) > 0:
            self.my_output.print_stream('## Operators', 'output')
            self.my_output.print_stream('', 'output')

            order = [
                'Name',
                'Available',
                'Progressing',
                'Degraded',
                'Upgradeable',
                'Version',
                'Age'
            ]
            self.print_table_header(order)

            for item in operators:
                line = ''
                line = self.add_column(line, item['name'])
                line = self.add_column_tick_bool(line, item['available'])
                line = self.add_column_tick_bool(line, item['progressing'])
                line = self.add_column_tick_bool(line, item['degraded'])
                line = self.add_column_tick_bool(line, item['upgradeable'])
                line = self.add_column(line, item['version'])
                line = self.add_column(line, item['age'])
                self.my_output.print_stream(line, 'output')

        subs = self.xd_handler.get_k8s_sub(cluster_name)
        if subs is not None and len(subs) > 0:
            self.my_output.print_stream('## Subscriptions', 'output')
            self.my_output.print_stream('', 'output')

            order = [
                'Namespace',
                'Name',
                'Version',
                'Plan',
                'Channel',
                'Latest',
                'Age'
            ]
            self.print_table_header(order)

            for item in subs:
                line = ''
                line = self.add_column(line, item['namespace'])
                line = self.add_column(line, item['name'])
                line = self.add_column(line, item['installed_csv'])
                line = self.add_column(line, item['install_plan_name'])
                line = self.add_column(line, item['channel'])
                line = self.add_column_tick_bool(line, item['is_latest_csv'])
                line = self.add_column(line, item['age'])
                self.my_output.print_stream(line, 'output')

        self.save_output('cluster-%s' % (cluster_name), subdir='ocp')
