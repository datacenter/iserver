from lib import ip_helper
from lib.aci import helper as aci_helper
from lib.intersight import helper as intersight_helper
from lib import iaccount_helper
from lib.nexus import helper as nexus_helper


class Fi():
    def __init__(self):
        self.fis = None
        self.iaccount_fis = {}

    def load_pre_fi(self):
        fis = self.get_pre_cache('fi', '')
        self.fis = []
        for key in fis:
            self.fis = self.fis + fis[key]

        return True

    def set_post_fi(self):
        return self.set_post_cache('fi', self.fis)

    def load_post_fi(self):
        self.fis = self.get_post_cache('fi')
        if self.fis is None:
            return False
        return True

    def get_fi_device_names(self):
        names = []
        for item in self.fis:
            names.append(item['Name'])

        names = sorted(
            names,
            key=lambda i: i.lower()
        )

        return names

    def get_fi_device_names_hash(self):
        names = self.get_fi_device_names()
        names_hash = {}

        for name in names:
            for item in self.fis:
                if item['Name'] == name:
                    names_hash[item['Name']] = item['hash']

        return names_hash

    def get_fi_hash(self, fi_name):
        fi_info = self.get_fi_by_name(fi_name)
        if fi_info is not None:
            return fi_info['hash']
        return None

    def is_fi_name(self, fi_name):
        if self.get_fi_by_name(fi_name) is None:
            return False
        return True

    def get_fi_by_name(self, fi_name):
        for item in self.fis:
            if item['Name'] == fi_name:
                return item

        return None

    def get_fi_interface_eth(self, fi_name):
        for item in self.fis:
            if item['Name'] == fi_name:
                return item['Ethernet']

        return None

    def get_fi_interface_pc(self, fi_name):
        for item in self.fis:
            if item['Name'] == fi_name:
                return item['EthernetPortChannel']

        return None

    def get_fi_by_mac(self, mac_address):
        for item in self.fis:
            if ip_helper.is_mac_equal(item['OutOfBandMac'], mac_address):
                return item['Name']

            for eth in item['Ethernet']:
                if ip_helper.is_mac_equal(eth['MacAddress'], mac_address):
                    return item['Name']

        return None

    def get_fi_peer_info(self, mac_address):
        info = {}

        info['src'] = []
        info['intf'] = []
        info['lldp'] = []
        info['mac'] = []

        for item in self.fis:
            for eth in item['Ethernet']:
                if eth['Role'] == 'server' and eth['Peer'] is not None:
                    if ip_helper.is_mac_equal(eth['Peer']['MacAddress'], mac_address):
                        iinfo = '%s:%s' % (
                            item['Name'],
                            eth['Name']
                        )

                        if iinfo not in info['intf']:
                            info['intf'].append(
                                iinfo
                            )

                        if 'fi' not in info['src']:
                            info['src'].append('fi')

        return info

    def get_fi_interface_id(self, interface_name):
        interface_name = interface_name.lower()
        if len(interface_name.split('eth')) == 2:
            return interface_name.split('eth')[1]
        return interface_name

    def get_fi_interface_hash(self, fi_name, interface_name):
        fi_info = self.get_fi_by_name(fi_name)
        if fi_info is None:
            return None

        interface_name = self.get_fi_interface_id(interface_name)
        for eth in fi_info['Ethernet']:
            if eth['Name'] == interface_name:
                return eth['hash']

        return None

    def get_fi_pc_hash(self, fi_name, pcid):
        fi_info = self.get_fi_by_name(fi_name)
        if fi_info is None:
            return None

        for pc_info in fi_info['EthernetPortChannel']:
            if pc_info['PortChannelId'] == pcid:
                return pc_info['hash']

        return None

    def prepare_fi(self, cache_enabled=True, allow_partial=False):
        iaccount_handler = iaccount_helper.IntersightAccount()
        iaccounts = iaccount_handler.get_iaccounts(domain=self.domain_name)

        self.fis = []
        for iaccount in iaccounts:
            self.my_output.debug('FIs %s' % (iaccount['name']))
            if cache_enabled and self.cache_ttl is not None:
                if iaccount['name'] in self.iaccount_fis:
                    self.my_output.debug('L2 Cache hit')
                    self.fis = self.fis + self.iaccount_fis[iaccount['name']]
                    continue

                self.iaccount_fis[iaccount['name']] = self.get_cache('fi-%s' % (iaccount['name']))
                if self.iaccount_fis[iaccount['name']] is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.fis = self.fis + self.iaccount_fis[iaccount['name']]
                    continue

            self.my_output.debug('Cache miss')

            self.iaccount_fis[iaccount['name']] = intersight_helper.get_all_fis(
                iaccount['name'],
                self.cache_ttl
            )
            if self.fis is None:
                if not allow_partial:
                    return False

            self.set_cache('fi-%s' % (iaccount['name']), self.iaccount_fis[iaccount['name']])
            self.fis = self.fis + self.iaccount_fis[iaccount['name']]

        return True

    def run_fi(self):
        for item in self.fis:
            item['hash'] = ip_helper.get_string_md5(item['Moid'])
            for intf_mo in item['Ethernet']:
                intf_mo['hash'] = ip_helper.get_string_md5(intf_mo['Moid'])
                intf_mo['ACI'] = None
                intf_mo['Nexus'] = None

                for apic in self.aci_lldp:
                    for adjacency in self.aci_lldp[apic]:
                        if ip_helper.is_mac_equal(adjacency['mac'], intf_mo['MacAddress']):
                            intf_mo['ACI'] = {}
                            intf_mo['ACI']['apic'] = adjacency['apic']
                            intf_mo['ACI']['node_id'] = adjacency['node_id']
                            intf_mo['ACI']['node_name'] = self.get_aci_node_name_by_id(
                                adjacency['node_id']
                            )
                            intf_mo['ACI']['interface_id'] = adjacency['interface_id']
                            intf_mo['ACI']['hash'] = aci_helper.get_aci_interface_hash(
                                intf_mo['ACI']['apic'],
                                intf_mo['ACI']['node_id'],
                                intf_mo['ACI']['interface_id']
                            )

                for key in self.nexus_lldp:
                    for item in self.nexus_lldp[key]:
                        if item['chassis_type'] == 'Mac Address':
                            if ip_helper.is_mac_equal(item['chassis_id'], intf_mo['MacAddress']):
                                intf_mo['Nexus'] = {}
                                intf_mo['Nexus']['device_name'] = item['device_name']
                                intf_mo['Nexus']['interface_id'] = item['l_port_id']
                                intf_mo['Nexus']['hash'] = nexus_helper.get_nexus_interface_hash(
                                    item['device_name'],
                                    item['l_port_id']
                                )

            if 'EthernetPortChannel' not in item:
                item['EthernetPortChannel'] = []

        for item in self.fis:
            for intf_mo in item['EthernetPortChannel']:
                intf_mo['hash'] = ip_helper.get_string_md5(intf_mo['Moid'])
                for eth_member_mo in intf_mo['Ethernet']:
                    for fi_item in self.fis:
                        for eth_mo in fi_item['Ethernet']:
                            if eth_member_mo['Moid'] == eth_mo['Moid']:
                                eth_member_mo['hash'] = eth_mo['hash']
                                eth_member_mo['ACI'] = eth_mo['ACI']
                                eth_member_mo['Nexus'] = eth_mo['Nexus']

        if not self.set_post_fi():
            return False

        return True

    def run_fi_serial(self):
        for fi in self.fis:
            item = {}
            item['serial'] = fi['Serial']
            item['domain'] = self.domain_name
            item['scope'] = 'fi'
            item['type'] = 'Fabric Interconnect'
            item['description'] = fi['Model']
            item['parent'] = None

            self.serial.append(
                item
            )

        return True

    def run_fi_mac(self):
        return True
