import json


class MdAciVrfOutput():
    def __init__(self):
        pass

    def print_aci_vrf_details(self, info):
        self.print_page_header('ACI VRF')
        self.my_output.print_stream('- Controller: %s' % (info['apic']), 'output')
        self.my_output.print_stream('- Tenant: %s' % (info['tenant']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')
        self.my_output.print_stream('- Health: %s' % (info['health']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        self.my_output.print_stream('- Segment: %s' % (info['seg']), 'output')
        self.my_output.print_stream('- pcTag: %s' % (info['pcTag']), 'output')
        self.my_output.print_stream('- Policy Control Enforcement Preference: %s' % (info['pcEnfPref']), 'output')
        self.my_output.print_stream('- Policy Control Enforcement Direction: %s' % (info['pcEnfDir']), 'output')
        self.my_output.print_stream('- BD Enforcement Status: %s' % (info['bdEnforcedEnable']), 'output')
        names = []
        for item in info['l3out']:
            names.append(
                '[%s](../l3out/%s.md)' % (
                    item['nameTenant'],
                    item['hash']
                )
            )
        if len(names) == 0:
            self.my_output.print_stream('- L3Out: ---', 'output')
        else:
            self.my_output.print_stream('- L3Out: %s' % (','.join(names)), 'output')

        self.my_output.print_stream('## References\n', 'output')
        self.my_output.print_stream('- Bridge Domain: %s' % (info['bdCount']), 'output')
        self.my_output.print_stream('- Subnet: %s' % (info['subnetCount']), 'output')
        self.my_output.print_stream('- L3Out: %s' % (info['l3outCount']), 'output')
        self.my_output.print_stream('- Endpoint: %s' % (info['endpointCount']), 'output')
        self.my_output.print_stream('- EPG: %s' % (info['epgCount']), 'output')
        self.my_output.print_stream('- Node: %s' % (info['nodeCount']), 'output')
        self.my_output.print_stream('- Route: %s' % (info['routeCount']), 'output')

        self.print_aci_epg_addon(info['fvAEPg'])
        self.print_aci_bd_addon(info['fvBD'])
        self.print_aci_bd_subnet_addon(info['fvSubnet'])
        self.print_aci_phy_state_addon(info['interfacePhy'])

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/vrf')

    def print_aci_tenant_vrf(self, info, tenant, controller):
        self.print_page_header('VRF (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'vrf')
        self.print_aci_tenant_table_bar(controller, tenant, 'vrf')

        order = [
            'Name',
            'EPG',
            'BD',
            'Subnet',
            'L3Out',
            'Node',
            'Route'
        ]
        self.print_table_header(order)

        for item in info:
            if item['tenant'] != tenant:
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./vrf/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['bdCount'])
            line = self.add_column(line, item['subnetCount'])
            line = self.add_column(line, item['epgCount'])
            line = self.add_column(line, item['l3outCount'])
            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['routeCount'])
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-vrf' % (controller, tenant), subdir='apic')

    def print_aci_vrf(self, info, controller):
        self.print_page_header('VRF (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'vrf')
        self.print_aci_global_table_bar(controller, 'vrf')

        order = [
            'Name',
            'EPG',
            'BD',
            'Subnet',
            'L3Out',
            'Node',
            'Route'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./vrf/%s.md)' % (
                    item['nameTenant'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['bdCount'])
            line = self.add_column(line, item['subnetCount'])
            line = self.add_column(line, item['epgCount'])
            line = self.add_column(line, item['l3outCount'])
            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['routeCount'])
            self.my_output.print_stream(line, 'output')

            self.aci_vrf_count[controller] = self.aci_vrf_count[controller] + 1

        self.save_output('%s-vrf' % (controller), subdir='apic')

        for item in info:
            self.print_aci_vrf_details(item)
