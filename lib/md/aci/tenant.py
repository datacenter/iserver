import json


class MdAciTenantOutput():
    def __init__(self):
        pass

    def print_aci_tenant_details(self, info):
        self.print_page_header('ACI Tenant')
        self.my_output.print_stream('- Controller: [%s](../%s-tenant.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')

        self.my_output.print_stream('\n## Debug\n', 'output')
        self.my_output.print_stream('```', 'output')
        self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/tenant')

    def print_aci_tenant(self, info, controller):
        self.print_page_header('Tenant (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'tenant')
        self.print_aci_global_table_bar(controller, 'tenant')

        order = [
            'Name',
            'Health',
            'EP',
            'AP',
            'EPG',
            'BD',
            'VRF',
            'L2Out',
            'L3Out',
            'SR-MPLS L3Out',
            'Contract',
            'Taboo',
            'Filter'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./tenant/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['health'])
            line = self.add_column(
                line,
                '[%s](./%s-%s-ep.md)' % (
                    item['endpointCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-ap.md)' % (
                    item['apCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-epg.md)' % (
                    item['aEpgCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-bd.md)' % (
                    item['bdCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-vrf.md)' % (
                    item['vrfCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-l2out.md)' % (
                    item['l2OutCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-l3out.md)' % (
                    item['l3OutCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-l3mpls.md)' % (
                    item['mplsL3OutCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-contract-standard.md)' % (
                    item['contractStandardCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-contract-taboo.md)' % (
                    item['contractTabooCount'],
                    controller,
                    item['name']
                )
            )
            line = self.add_column(
                line,
                '[%s](./%s-%s-contract-filter.md)' % (
                    item['contractFilterCount'],
                    controller,
                    item['name']
                )
            )
            self.my_output.print_stream(line, 'output')

            self.aci_tenant_count[controller] = self.aci_tenant_count[controller] + 1

        self.save_output('%s-tenant' % (controller), subdir='apic')

        for item in info:
            self.print_aci_tenant_details(item)
