from lib.intersight import helper as intersight_helper
from lib import iaccount_helper
from lib import ip_helper
from lib.aci import helper as aci_helper
from lib.nexus import helper as nexus_helper


class Server():
    def __init__(self):
        self.servers = None
        self.iaccount_servers = {}

        self.server_macs = None
        self.servers_fabric = None
        self.ocp = None
        self.ocp_serial_to_host = None

        self.server_tag_moids = {}

    def load_pre_server(self):
        servers = self.get_pre_cache('server', '')
        self.servers = []
        for key in servers:
            self.servers = self.servers + servers[key]

        for server in self.servers:
            del server['IntersightObject']

        return True

    def set_post_server(self):
        return self.set_post_cache('server', self.servers)

    def load_post_server(self):
        self.servers = self.get_post_cache('server')
        if self.servers is None:
            return False
        return True

    def run_post_load_server(self):
        self.prepare_server_macs()
        self.prepare_server_fabric()
        self.prepare_server_ocp()

    def get_ocp_host_by_serial(self, serial):
        if serial.lower() not in self.ocp_serial_to_host:
            return None
        return self.ocp_serial_to_host[serial.lower()]

    def get_server_moids(self, tag):
        moids = []
        for server in self.servers:
            if tag == 'all':
                moids.append(
                    server['Moid']
                )
                continue

            if tag == 'connected':
                if server['Connected']:
                    moids.append(
                        server['Moid']
                    )
                continue

            if tag == 'disconnected':
                if not server['Connected']:
                    moids.append(
                        server['Moid']
                    )
                continue

            if len(tag.split('-')) == 2:
                if tag.split('-')[0] == 'vc':
                    vc_name = tag.split('-')[1]
                    if vc_name in self.vc_serials:
                        if server['Serial'] in self.vc_serials[vc_name]:
                            moids.append(
                                server['Moid']
                            )

                if tag.split('-')[0] == 'ocp':
                    ocp_name = tag.split('-')[1]
                    if ocp_name in self.ocp:
                        if server['Moid'] in self.ocp[ocp_name]:
                            moids.append(
                                server['Moid']
                            )

                continue

        return moids

    def get_server_by_moid(self, moid):
        if self.servers is None:
            return None

        for server in self.servers:
            if server['Moid'] == moid:
                return server

        return None

    def get_server_mac_info(self, server_info):
        info = []

        if 'MacAddressInfo' not in server_info:
            return info

        for mac_address_info in server_info['MacAddressInfo']:
            mac_address_info['ServerName'] = server_info['Name']
            mac_address_info['ServerMoid'] = server_info['Moid']
            mac_address_info['intfRef'] = []

            mac_address_info['aci'] = self.get_aci_mac_info(
                mac_address_info['MacAddress']
            )
            for intf in mac_address_info['aci']['intf']:
                item = {}
                item['type'] = 'ACI'
                item['fabric'] = intf.split(':')[0]
                item['device'] = intf.split(':')[1]
                item['device_name'] = self.get_aci_node_name_by_id(item['device'])
                item['intf'] = intf.split(':')[2]
                item['intf_hash'] = aci_helper.get_aci_interface_hash(
                    item['fabric'],
                    item['device'],
                    item['intf']
                )
                item['lldp_hash'] = None
                for litem in mac_address_info['aci']['lldp']:
                    item['lldp_hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            litem['apic'],
                            litem['dn']
                        )
                    )

                mac_address_info['intfRef'].append(
                    item
                )

            mac_address_info['nexus'] = self.get_nexus_mac_info(
                mac_address_info['MacAddress']
            )
            for intf in mac_address_info['nexus']['intf']:
                item = {}
                item['type'] = 'Nexus'
                item['fabric'] = 'Nexus'
                item['device'] = intf.split(':')[0]
                item['intf'] = intf.split(':')[1]
                item['intf_hash'] = nexus_helper.get_nexus_interface_hash(
                    item['device'],
                    item['intf']
                )
                item['lldp_hash'] = None
                for litem in mac_address_info['nexus']['lldp']:
                    item['lldp_hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            litem['nexus_name'],
                            litem['l_port_id']
                        )
                    )

                mac_address_info['intfRef'].append(
                    item
                )

            mac_address_info['fi'] = self.get_fi_peer_info(
                mac_address_info['MacAddress']
            )

            mac_address_info['src'] = mac_address_info['aci']['src'] + mac_address_info['nexus']['src'] + mac_address_info['fi']['src']
            mac_address_info['intf'] = mac_address_info['aci']['intf'] + mac_address_info['nexus']['intf'] + mac_address_info['fi']['intf']

            info.append(
                mac_address_info
            )

        return info

    def get_server_vc_by_moid(self, moid):
        for vc_instance in self.vc_instance:
            tag = 'vc-%s' % (vc_instance)
            if tag not in self.server_tag_moids:
                self.server_tag_moids[tag] = self.get_server_moids(tag)

            if moid in self.server_tag_moids[tag]:
                return vc_instance

        return None

    def get_ocp_from_tags(self, tags):
        for tag in tags:
            if tag['Key'] == 'ocp':
                return tag['Value']
        return None

    def get_server_mac_info_by_mac(self, mac_address):
        for server_info in self.servers:
            if 'MacAddressInfo' not in server_info:
                continue

            if server_info['MacAddressInfo'] is None:
                continue

            for mac_info in server_info['MacAddressInfo']:
                if ip_helper.is_mac_equal(mac_info['MacAddress'], mac_address):
                    return mac_info

        return None

    def prepare_server_macs(self):
        self.server_macs = []
        for server in self.servers:
            if 'MacAddressInfo' in server:
                for item in server['MacAddressInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    new_item = {}
                    new_item['ServerName'] = server['Name']
                    new_item['ServerMoid'] = server['Moid']
                    new_item['ManagementIp'] = server['ManagementIp']
                    for key in ['MacAddress', 'AdapterModel', 'InterfaceDn']:
                        new_item[key] = item[key]

                    self.server_macs.append(
                        new_item
                    )

    def prepare_server_fabric(self):
        self.servers_fabric = []
        for server in self.servers:
            server['Fabric'] = self.get_server_mac_info(server)
            self.servers_fabric = self.servers_fabric + server['Fabric']

        self.servers_fabric = sorted(
            self.servers_fabric,
            key=lambda i: i['MacAddress']
        )

    def prepare_server_ocp(self):
        self.ocp = {}
        self.ocp_serial_to_host = {}

        for server in self.servers:
            if server['Tags'] is not None:
                for tag in server['Tags']:
                    if tag['Key'] == 'ocp':
                        if tag['Value'] not in self.ocp:
                            self.ocp[tag['Value']] = []

                        self.ocp[tag['Value']].append(
                            server['Moid']
                        )

                        self.ocp_serial_to_host[server['Serial'].lower()] = server

    def prepare_server(self, cache_enabled=True, allow_partial=False):
        iaccount_handler = iaccount_helper.IntersightAccount()
        iaccounts = iaccount_handler.get_iaccounts(domain=self.domain_name)

        self.servers = []
        for iaccount in iaccounts:
            self.my_output.debug('Servers: %s' % (iaccount['name']))
            if cache_enabled and self.cache_ttl is not None:
                if iaccount['name'] in self.iaccount_servers:
                    self.my_output.debug('L2 Cache hit')
                    self.servers = self.servers + self.iaccount_servers[iaccount['name']]
                    continue

                self.iaccount_servers[iaccount['name']] = self.get_cache('server-%s' % (iaccount['name']))
                if self.iaccount_servers[iaccount['name']] is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.servers = self.servers + self.iaccount_servers[iaccount['name']]
                    continue

            self.my_output.debug('Cache miss')

            self.iaccount_servers[iaccount['name']] = intersight_helper.get_all_servers_hw(
                iaccount['name'],
                self.cache_ttl
            )
            if self.iaccount_servers[iaccount['name']] is None:
                if not allow_partial:
                    return False

            self.set_cache('server-%s' % (iaccount['name']), self.iaccount_servers[iaccount['name']])
            self.servers = self.servers + self.iaccount_servers[iaccount['name']]

        return True

    def run_server_vc(self):
        for server in self.servers:
            server['Vc'] = {}
            server['Vc']['host'] = None
            server['Vc']['vms'] = []

            for vc_name in self.vc_host:
                for vc_host in self.vc_host[vc_name]:
                    if vc_host['serial'].lower() == server['Serial'].lower():
                        server['Vc']['host'] = vc_host
                        server['Vc']['host']['hash'] = ip_helper.get_string_md5(
                            '%s %s' % (
                                vc_name,
                                vc_host['name']
                            )
                        )
                        server['Vc']['host']['vCenter'] = self.vc_instance[vc_name]
                        if vc_name in self.vc_vm:
                            for vc_vm in self.vc_vm[vc_name]:
                                if vc_vm['host'] == vc_host['name']:
                                    server['Vc']['vms'].append(
                                        vc_vm
                                    )

    def update_server_ocp(self, server_moid, cluster_name, host_name, host_hash):
        for server in self.servers:
            if server['Moid'] == server_moid:
                server['Ocp'] = {}
                server['Ocp']['cluster'] = cluster_name
                server['Ocp']['host'] = host_name
                server['Ocp']['hash'] = host_hash

    def run_server(self):
        self.prepare_server_macs()
        self.prepare_server_fabric()
        self.prepare_server_ocp()
        self.run_server_vc()

        if not self.set_post_server():
            return False

        return True

    def run_server_serial(self):
        for server in self.servers:
            item = {}
            item['serial'] = server['Serial']
            item['domain'] = self.domain_name
            item['scope'] = 'server'
            item['type'] = 'Server'
            item['description'] = '%s [%s]' % (
                server['Name'],
                server['Model']
            )
            item['parent'] = None

            self.serial.append(
                item
            )

            parent_sn = server['Serial']
            for inventory in server['Inventory']:
                if inventory['Serial'] is None:
                    continue

                if inventory['Serial'] == '':
                    continue

                if inventory['Serial'].lower() == 'n/a':
                    continue

                if inventory['Serial'] == parent_sn:
                    continue

                item = {}
                item['serial'] = inventory['Serial']
                item['domain'] = self.domain_name
                item['scope'] = 'server'
                item['type'] = inventory['Type']
                item['description'] = '[%s] [%s] [%s]' % (
                    inventory['Model'],
                    inventory['Vendor'],
                    inventory['Pid']
                )
                item['parent'] = parent_sn

                self.serial.append(
                    item
                )

        return True

    def run_server_mac(self):
        return True
