import json


class ImcCliNet():
    def __init__(self):
        self.net_mo = None
        self.net_mac_mo = {}

    def get_net_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.net_mo is not None:
                return self.net_mo

            self.net_mo = self.get_icm_cli_cache_entry(
                'net'
            )
            if self.net_mo is not None:
                return self.net_mo

        # Network Adapter:
        #     Slot: 1
        #     Product Name: Cisco(R) Ethernet Converged NIC XXV710-DA2
        #     No Of Interfaces: 2

        self.net_mo = self.show_list(
            'show network-adapter detail',
            'Network Adapter',
            None,
            scope='chassis'
        )

        if self.net_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'net',
            self.net_mo
        )

        self.log.debug(
            'get_net_mo',
            json.dumps(self.net_mo, indent=4)
        )
        return self.net_mo

    def get_net_mac_mo(self, slot_id, cache_enabled=True):
        if cache_enabled:
            if slot_id in self.net_mac_mo and self.net_mac_mo[slot_id] is not None:
                return self.net_mac_mo[slot_id]

            self.net_mac_mo[slot_id] = self.get_icm_cli_cache_entry(
                'net_mac_%s' % (slot_id)
            )
            if self.net_mac_mo[slot_id] is not None:
                return self.net_mac_mo[slot_id]

        commands = [
            'top',
            'scope chassis',
            'scope network-adapter %s' % (slot_id),
            'show mac-list detail'
        ]

        success, output = self.run_commands(
            commands
        )

        if not success:
            return None

        # Interface ID: 1
        # MAC Address: 5c:71:0d:26:37:b2
        # Interface ID: 2
        # MAC Address: 5c:71:0d:26:37:b3

        self.net_mac_mo[slot_id] = []
        for line in output['show mac-list detail'].split('\n'):
            self.net_mac_mo[slot_id].append(
                line
            )

        self.set_imc_cli_cache_entry(
            'net_mac_%s' % (slot_id),
            self.net_mac_mo[slot_id]
        )

        self.log.debug(
            'get_net_mac_mo',
            json.dumps(self.net_mac_mo[slot_id], indent=4)
        )
        return self.net_mac_mo[slot_id]

    def get_net_info(self, net_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in net_mo:
            info[key] = net_mo[key]

        info['__Key'] = 'Slot'
        info['__Value'] = info[info['__Key']]

        return info

    def get_net_mac_info(self, net_mac_mo):
        macs_info = []
        mac_info = {}

        for item in net_mac_mo:
            key = item.split(':')[0]
            value = ':'.join(item.split(':')[1:])

            if key == 'MAC Address':
                mac_info['MAC Address'] = value
                macs_info.append(mac_info)
            else:
                mac_info = {}
                mac_info['Interface ID'] = value

        return macs_info

    def get_net(self, cache_enabled=True):
        nets_mo = self.get_net_mo(cache_enabled=cache_enabled)
        if nets_mo is None:
            return None

        nets_info = []

        for net_mo in nets_mo:
            nets_info.append(
                self.get_net_info(
                    net_mo
                )
            )

        for net_info in nets_info:
            net_info['Interfaces'] = self.get_net_mac_info(
                self.get_net_mac_mo(
                    net_info['Slot'],
                    cache_enabled=cache_enabled
                )
            )

        self.log.debug(
            'get_net_info',
            json.dumps(nets_info, indent=4)
        )
        return nets_info
