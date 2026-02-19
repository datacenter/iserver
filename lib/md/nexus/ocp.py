class MdNexusOcpOutput():
    def __init__(self):
        pass

    def print_nexus_servers_ocp(self, info, name):
        self.print_page_header('OpenShift Servers (%s)\n' % (name))
        self.print_nexus_devices_bar(name, 'ocp')
        self.print_nexus_table_bar(name, 'ocp')

        order = [
            'Interface',
            'Server',
            'Inteface',
            'Cluster',
            'Host'
        ]
        self.print_table_header(order)

        for item in sorted(info, key=lambda i: i['_index']):
            ocp_host = self.xd_handler.get_ocp_host_by_serial(
                item['ServerSerial']
            )
            if ocp_host is None:
                continue

            line = '%s |' % (item['InterfaceId'])

            line = '%s [%s](../compute/%s-net.md) |' % (
                line,
                item['ServerName'],
                item['ServerMoid']
            )

            line = '%s %s |' % (line, item['ServerInterface'])
            line = '%s --- |' % (line)
            line = '%s ---' % (line)

            self.my_output.print_stream(line, 'output')
            self.nexus_ocp_count[name] = self.nexus_ocp_count[name] + 1

        self.save_output('%s-ocp' % (name), subdir='nexus')
