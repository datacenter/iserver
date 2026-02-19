from lib import ip_helper


class ImcCliIpOutput():
    def __init__(self):
        pass

    def print_imc_ip(self, info):
        new_info = []
        for item in info:
            new_item = {}
            new_item['__IP'] = item['network']['__IP']

            new_item['Hostname'] = item['network']['Hostname']

            new_item['NIC'] = []
            new_item['NIC'].append(
                'Mode: %s' % (item['network']['NIC Mode'])
            )
            new_item['NIC'].append(
                'Auto Negotiate: %s' % (item['network']['Auto Negotiate'])
            )
            new_item['NIC'].append(
                'Speed: %s' % (item['network']['Operational Network Speed'])
            )
            new_item['NIC'].append(
                'Duplex: %s' % (item['network']['Operational Duplex'])
            )

            new_item['VLAN'] = []
            if item['network']['VLAN Enabled'] == 'yes':
                new_item['VLAN'].append(
                    item['network']['VLAN ID']
                )
                new_item['VLAN'].append(
                    'Priority: %s' % (item['network']['VLAN Priority'])
                )
            else:
                new_item['VLAN'].append('--')

            new_item['IPv4'] = []
            if item['network']['IPv4 Enabled'] == 'yes':
                new_item['IPv4'].append(
                    '%s/%s' % (
                        item['network']['IPv4 Address'],
                        ip_helper.netmask_to_prefix(item['network']['IPv4 Netmask'])
                    )
                )
                new_item['IPv4'].append(
                    'GW %s' % (
                        item['network']['IPv4 Gateway']
                    )
                )
                if item['network']['DHCP Enabled'] == 'yes':
                    new_item['IPv4'].append(
                        'DHCP'
                    )
                else:
                    new_item['IPv4'].append(
                        'Static'
                    )
            else:
                new_item['IPv4'].append('--')

            new_item['IPv6'] = []
            if item['network']['IPv6 Enabled'] == 'yes':
                new_item['IPv6'].append(
                   item['network']['IPv6 Prefix']
                )
                if item['IPV6 DHCP Enabled'] == 'yes':
                    new_item['IPv6'].append(
                        'DHCP'
                    )
                else:
                    new_item['IPv6'].append(
                        'Static'
                    )
            else:
                new_item['IPv6'].append('--')

            new_item['DNS'] = []
            if len(item['network']['Preferred DNS']) > 0:
                new_item['DNS'].append(
                    item['network']['Preferred DNS']
                )
            if len(item['network']['Alternate DNS']) > 0:
                new_item['DNS'].append(
                    item['network']['Alternate DNS']
                )

            new_item['ICMP'] = []
            new_item['ICMP'].append(
                'Destination Unreachable: %s' % (
                    item['icmp']['Destination Unreachable Enabled']
                )
            )
            new_item['ICMP'].append(
                'Redirect: %s' % (
                    item['icmp']['Redirect Enabled']
                )
            )

            if item['filtering']['Enabled'] == 'yes':
                new_item['IP Filtering'] = item['filtering']['Filter']
            else:
                new_item['IP Filtering'] = ['--']

            new_item['IP Blocking'] = []
            if item['blocking']['Enabled'] == 'yes':
                for key in ['Fail Count', 'Fail Window', 'Blocking Time']:
                    new_item['IP Blocking'].append(
                        '%s: %s' % (
                            key,
                            item['blocking'][key]
                        )
                    )

            new_info.append(
                new_item
            )

        self.print_list_table(
            new_info,
            title='IMC - Network',
            add_endpoint_ip=True,
            allow_order_subkeys=False,
            expand=['NIC', 'VLAN', 'IPv4', 'IPv6', 'DNS', 'ICMP', 'IP Filtering', 'IP Blocking'],
            row_separator=True
        )
