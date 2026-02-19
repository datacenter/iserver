class MdVcClusterOutput():
    def __init__(self):
        pass

    def print_vc_cluster_hosts(self, cluster, clusters, hosts):
        self.print_vc_cluster_page_header(
            'Host',
            cluster,
            clusters
        )

        self.my_output.print_stream('## vCenter', 'output')

        order = [
            'Host',
            'Power',
            'Connection',
            'CPU',
            'Memory',
            'Uptime'
        ]
        self.print_table_header(order)

        for item in hosts:
            if item['name'] not in cluster['hosts']:
                continue

            line = ''
            line = self.add_vc_host(line, item)
            line = self.add_vc_host_power_state(line, item)
            line = self.add_vc_host_connection_state(line, item)
            line = self.add_column(line, item['stats']['overallCpuUsagePct'])
            line = self.add_column(line, item['stats']['overallMemoryUsagePct'])
            line = self.add_column(line, item['_uptime'], last=True)
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Hardware', 'output')

        order = [
            'Host',
            'Hypervisor',
            'Model',
            'Compute',
            'Inv',
            'Net',
            'Info'
        ]
        self.print_table_header(order)

        for item in hosts:
            if item['name'] not in cluster['hosts']:
                continue

            line = ''
            line = self.add_vc_host(line, item)
            line = self.add_column(line, item['_hypervisor'])
            line = self.add_column(line, item['model'])
            if item['ServerName'] is None:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['ServerName'])
                line = self.add_column(
                    line,
                    '[Link](../compute/%s-inv.md)' % (
                        item['ServerMoid']
                    )
                )
                line = self.add_column(
                    line,
                    '[Link](../compute/%s-net.md)' % (
                        item['ServerMoid']
                    )
                )

            line = self.add_column(
                line,
                '[Link](./hw/%s.md)' % (item['hash'])
            )

            self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(cluster['hash'], subdir='vc/cluster')
