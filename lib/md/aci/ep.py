from lib.aci import helper as aci_helper


class MdAciEpOutput():
    def __init__(self):
        pass

    def print_aci_ep_addon(self, info, title=True, vmm_enabled=False):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Endpoint', 'output')

        order = [
            'MAC',
            'IP',
            'Encap',
            'Interface'
        ]
        self.print_table_header(order)

        vmm_count = 0
        for ep in info:
            line = ''
            line = self.add_column(line, ep['mac'])
            line = self.add_column(line, ep['ip'])
            line = self.add_column(line, ep['encapT'])

            fabric = []
            for item in ep['fabric']:
                fabric.append(
                    item['ep']
                )
            line = self.add_column(line, ','.join(fabric))
            self.my_output.print_stream(line, 'output')

            if 'vm' in ep:
                vmm_count += 1

        if vmm_enabled and vmm_count > 0:
            if title:
                self.my_output.print_stream('## VMM Endpoint', 'output')

            order = [
                'MAC',
                'IP',
                'Host',
                'VM',
                'vNIC'
            ]
            self.print_table_header(order)

            for ep in info:
                if 'vm' not in ep:
                    continue

                line = ''
                line = self.add_column(line, ep['mac'])
                line = self.add_column(line, ep['ip'])
                if 'hv' in ep and ep['hv'] is not None and 'name' in ep['hv']:
                    line = self.add_column(line, ep['hv']['name'])
                else:
                    line = self.add_column(line, '---')

                if ep['vm'] is not None and 'name' in ep['vm']:
                    line = self.add_column(line, ep['vm']['name'])
                else:
                    line = self.add_column(line, '---')

                if 'vnic' in ep and ep['vnic'] is not None and 'name' in ep['vnic']:
                    line = self.add_column(line, ep['vnic']['name'])
                else:
                    line = self.add_column(line, '---')

                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def print_aci_ep_details(self, info, controller):
        self.print_page_header('ACI Endpoint')
        self.my_output.print_stream('- Controller: [%s](../%s-ep.md)' % (controller, controller), 'output')
        self.my_output.print_stream('- MAC Address: %s' % (info['mac']), 'output')
        self.my_output.print_stream(
            '- Flags: %s' % (
                ','.join(aci_helper.resolve_ep_flags(info['flags']))
            ),
            'output'
        )
        self.my_output.print_stream('- Type: %s' % (info['lcC']), 'output')
        self.my_output.print_stream('- Encapsulation: %s' % (info['encap']), 'output')

        if len(info['epgNameApTenant']) > 0:
            self.my_output.print_stream(
                '- EPG: [%s](../epg/%s.md)' % (
                    info['epgNameApTenant'],
                    info['epg_hash']
                ),
                'output'
            )

        if len(info['bdNameTenant']) > 0:
            self.my_output.print_stream(
                '- BD: [%s](../bd/%s.md)' % (
                    info['bdNameTenant'],
                    info['bd_hash']
                ),
                'output'
            )

        if len(info['vrfNameTenant']) > 0:
            self.my_output.print_stream(
                '- VRF: [%s](../vrf/%s.md)' % (
                    info['vrfNameTenant'],
                    info['vrf_hash']
                ),
                'output'
            )

        if info['fvRsHyper'] is not None:
            self.my_output.print_stream('- Hypervisor: %s' % (info['fvRsHyper']['tDn']), 'output')
        if info['fvRsToVm'] is not None:
            self.my_output.print_stream('- Virtual Machine: %s' % (info['fvRsHyper']['tDn']), 'output')

        if len(info['fabricPathDn']) > 0:
            self.my_output.print_stream('## Fabric', 'output')
            self.my_output.print_stream('- Dn: %s' % (info['fabricPathDn']), 'output')
            for item in info['fabric']:
                self.my_output.print_stream('- Resolved: %s' % (item['ep']), 'output')
            self.my_output.print_stream('', 'output')

        if len(info['fvIp']) > 0:
            self.my_output.print_stream('## IP Address', 'output')
            for item in info['fvIp']:
                self.my_output.print_stream('- %s (vrf:%s)' % (item['addr'], item['vrfDn']), 'output')
            self.my_output.print_stream('', 'output')

        if 'Server' in info and info['Server'] is not None:
            self.print_server(info['Server'], 'AddOn')
            self.my_output.print_stream('', 'output')
            self.print_server_mac(info['Server'], info['mac'])
            self.print_server_vc(info['Server'], 'AddOn')

        self.save_output(info['hash'], subdir='apic/ep')

    def print_aci_ep(self, info, controller):
        self.print_page_header('Endpoint (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'ep')
        self.print_aci_controller_table_bar(controller, 'ep')

        order = [
            'MAC',
            'IP',
            'VLAN',
            'EPG',
            'VRF',
            'Fabric'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./ep/%s.md)' % (
                    item['mac'],
                    item['hash']
                )
            )

            line = self.add_column(line, item['ip'].split(',')[0])

            line = self.add_column(line, item['encapVlan'])

            if len(item['epgNameApTenant']) > 0:
                line = self.add_column(
                    line,
                    '[%s](./epg/%s.md)' % (
                        item['epgNameApTenant'],
                        item['epg_hash']
                    )
                )
            else:
                line = self.add_column(line, '---')

            if len(item['vrfNameTenant']) > 0:
                line = self.add_column(
                    line,
                    '[%s](./vrf/%s.md)' % (
                        item['vrfNameTenant'],
                        item['vrf_hash']
                    )
                )
            else:
                line = self.add_column(line, '---')

            if len(item['fabric']) > 0:
                line = self.add_column(line, item['fabric'][0]['ep'])
            else:
                line = self.add_column(line, '---')

            self.my_output.print_stream(line, 'output')

            if len(item['fabric']) > 1 or len(item['ip'].split(',')) > 1:
                for i in range(max(len(item['fabric']), len(item['ip'].split(',')))):
                    if i == 0:
                        continue

                    line = ''
                    line = self.add_column(line, '&nbsp;')
                    try:
                        line = self.add_column(line, item['ip'].split(',')[i])
                    except BaseException:
                        line = self.add_column(line, '&nbsp;')

                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')

                    try:
                        line = self.add_column(line, item['fabric'][i]['ep'])
                    except BaseException:
                        line = self.add_column(line, '&nbsp;')

                    self.my_output.print_stream(line, 'output')

            self.aci_ep_count[controller] = self.aci_ep_count[controller] + 1

        self.save_output('%s-ep' % (controller), subdir='apic')

        for item in info:
            self.print_aci_ep_details(item, controller)
