class LinuxBondInfo():
    def __init__(self):
        self.bond = None

    def get_bond_info(self):
        if self.bond is not None:
            return self.bond

        bonds_mo = self.get_bond_cmd()

        self.bond = []
        for bond_name in bonds_mo:
            bond_info = {}
            bond_info['__Output'] = {}
            bond_info['server'] = self.server_display_name
            bond_info['name'] = bond_name
            bond_info['driver'] = self.get_line(bonds_mo[bond_name], 'Ethernet Channel Bonding Driver: ', strip=True)
            bond_info['mode'] = self.get_line(bonds_mo[bond_name], 'Bonding Mode: ', strip=True)
            bond_info['transmit_hash_policy'] = self.get_line(bonds_mo[bond_name], 'Transmit Hash Policy: ', strip=True)
            bond_info['mii_status'] = self.get_line(bonds_mo[bond_name], 'MII Status: ', strip=True)
            if bond_info['mii_status'] == 'up':
                bond_info['__Output']['mii_status'] = 'Green'
            else:
                bond_info['__Output']['mii_status'] = 'Red'
            bond_info['mii_polling_ms'] = self.get_line(bonds_mo[bond_name], 'MII Polling Interval (ms): ', strip=True)
            bond_info['up_delay_ms'] = self.get_line(bonds_mo[bond_name], 'Up Delay (ms): ', strip=True)
            bond_info['down_delay_ms'] = self.get_line(bonds_mo[bond_name], 'Down Delay (ms): ', strip=True)
            bond_info['lacp_active'] = self.get_line(bonds_mo[bond_name], 'LACP active: ', strip=True)
            bond_info['lacp_rate'] = self.get_line(bonds_mo[bond_name], 'LACP rate: ', strip=True)
            bond_info['min_links'] = self.get_line(bonds_mo[bond_name], 'Min links: ', strip=True)

            member_interfaces = self.get_lines(bonds_mo[bond_name], begin_pattern='Slave Interface: ', strip=True)
            bond_info['member'] = []
            if member_interfaces is not None:
                for member_interface in member_interfaces:
                    section = self.get_section(
                        bonds_mo[bond_name],
                        'Slave Interface: %s' % (member_interface),
                        'Slave Interface: '
                    )
                    if section is None or len(section) == 0:
                        self.log.error(
                            'get_bond_info',
                            'Section not found: %s' % (member_interface)
                        )
                        continue

                    member_info = {}
                    member_info['__Output'] = {}
                    member_info['name'] = member_interface
                    member_info['mii_status'] = self.get_line(section, 'MII Status: ', strip=True)
                    if member_info['mii_status'] == 'up':
                        member_info['__Output']['mii_status'] = 'Green'
                    else:
                        member_info['__Output']['mii_status'] = 'Red'
                    member_info['speed'] = self.get_line(section, 'Speed: ', strip=True)
                    member_info['duplex'] = self.get_line(section, 'Duplex: ', strip=True)
                    member_info['link_failure_count'] = self.get_line(section, 'Link Failure Count: ', strip=True)
                    member_info['mac'] = self.get_line(section, 'Permanent HW addr: ', strip=True)

                    bond_info['member'].append(
                        member_info
                    )

            self.bond.append(
                bond_info
            )

        return self.bond

    def get_bond(self):
        return self.get_bond_info()
