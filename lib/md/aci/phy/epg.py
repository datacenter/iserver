from lib import ip_helper


class MdAciPhyEpgOutput():
    def __init__(self):
        pass

    def print_aci_node_phy_epg(self, controller, node_name, info, servers):
        self.print_page_header('Interface Phy - EPG (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'phy:epg')
        self.print_aci_node_table_bar(controller, node_name, 'phy:epg')

        order = [
            'Intf',
            'EPG',
            'Encap',
            'Id',
            'HwId',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            if item['epg_stats'] is None or len(item['epg_stats']) == 0:
                continue

            for epg in item['epg_stats']:
                line = ''
                line = self.add_phy_interface(line, item, add_oper=True)

                line = self.add_column(
                    line,
                    '[%s](./epg/%s.md)' % (
                        epg['nameApTenant'],
                        epg['hash']
                    )
                )

                if 'vlan' in epg and epg['vlan'] is not None:
                    line = self.add_column(line, epg['vlan']['encap'].split('vlan-')[1])
                    line = self.add_column(line, epg['vlan']['id'])
                    line = self.add_column(line, epg['vlan']['hwId'])
                else:
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---')

                line = self.add_aci_connected_device_name(line, item)
                line = self.add_aci_connected_device_interface(line, item, last=True)
                self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-phy-epg' % (controller, node_name), subdir='apic')
