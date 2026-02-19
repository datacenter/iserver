import copy
from lib import ip_helper
from lib.aci import apic
from lib.aci import helper as aci_helper


class AciLldp():
    def __init__(self):
        self.aci_lldp = None

    def load_pre_aci_lldp(self):
        self.aci_lldp = self.get_pre_cache('aci', 'lldp')
        if self.aci_lldp is None:
            return False
        return True

    def set_post_aci_lldp(self):
        return self.set_post_cache('aci-lldp', self.aci_lldp)

    def load_post_aci_lldp(self):
        self.aci_lldp = self.get_post_cache('aci-lldp')
        if self.aci_lldp is None:
            return False
        return True

    def get_aci_lldp(self):
        info = copy.deepcopy(self.aci_lldp)
        return info

    def prepare_aci_lldp(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_lldp = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci lldp: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_lldp:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-lldp' % (aci_controller['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.aci_lldp[aci_controller['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=self.log_id
            )

            nodes = apic_handler.get_nodes(
                node_filter=['role:!controller']
            )
            if nodes is None:
                self.log.error(
                    'prepare_aci_lldp',
                    'Failed to get nodes: %s' % (aci_controller['name'])
                )
                continue

            self.aci_lldp[aci_controller['name']] = []
            for node in nodes:
                node_lldp_info = apic_handler.get_protocol_lldp(
                    node['podId'],
                    node['id'],
                    instance_info=False,
                    stats_info=False,
                    adjacency_info=True
                )
                if 'adjacency' not in node_lldp_info or node_lldp_info['adjacency'] is None:
                    self.log.error(
                        'prepare_aci_lldp',
                        'Failed to get node lldp: %s' % (node['id'])
                    )
                    continue

                for item in node_lldp_info['adjacency']:
                    item['apic'] = aci_controller['name']
                    item['node_id'] = node['id']
                    self.aci_lldp[aci_controller['name']].append(
                        item
                    )

            self.set_cache(
                'aci-%s-lldp' % (aci_controller['name']),
                self.aci_lldp[aci_controller['name']]
            )

        return True

    def run_aci_lldp(self):
        for key in self.aci_lldp:
            for item in self.aci_lldp[key]:
                item['xd'] = copy.deepcopy(self.xd)

        for key in self.aci_lldp:
            for item in self.aci_lldp[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['dn']
                    )
                )

                item['_index'] = aci_helper.get_aci_interface_id(
                    item['interface_id']
                )

                item['node_name'] = self.get_aci_node_name_by_id(
                    item['node_id']
                )

                if item['sysDesc'].startswith('Cisco Nexus Operating System'):
                    item['xd']['DeviceType'] = 'Nexus'
                    item['xd']['DeviceSysName'] = item['sysName']
                    item['xd']['NexusDevice'] = self.get_nexus_device_by_hostname(
                        item['sysName']
                    )
                    if item['xd']['NexusDevice'] is None:
                        item['xd']['FI'] = self.get_fi_by_mac(
                            item['chassisIdV']
                        )
                        if item['xd']['FI'] is not None:
                            item['xd']['DeviceType'] = 'FI'

                if item['sysDesc'].startswith('topology') and len(item['sysDesc'].split('/')) == 3:
                    item['xd']['DeviceType'] = 'ACI'
                    item['xd']['DeviceSysName'] = item['sysName']
                    node_info = self.get_aci_node_by_id(
                        item['sysDesc'].split('/')[2].split('-')[1]
                    )
                    if node_info is None:
                        if self.is_aci_node_name(item['sysName']):
                            item['xd']['AciApicName'] = node_info['apic']
                            item['xd']['AciNodeName'] = item['sysName']
                            item['xd']['AciNodeId'] = self.get_aci_node_id_by_name(item['sysName'])
                            item['xd']['AciNodeRef'] = '%s-%s' % (node_info['apic'], item['sysName'])
                    else:
                        item['xd']['AciApicName'] = node_info['apic']
                        item['xd']['AciNodeName'] = node_info['node']
                        item['xd']['AciNodeId'] = self.get_aci_node_id_by_name(node_info['node'])
                        item['xd']['AciNodeRef'] = '%s-%s' % (node_info['apic'], node_info['node'])

        for key in self.aci_lldp:
            for item in self.aci_lldp[key]:
                if item['xd']['DeviceType'] is not None:
                    continue

                if self.server_macs is None:
                    continue

                for server_mac in self.server_macs:
                    if item['mac'] is not None:
                        if ip_helper.is_mac_equal(item['mac'], server_mac['MacAddress']):
                            item['xd']['DeviceType'] = 'Server'
                            item['xd']['ServerName'] = server_mac['ServerName']
                            item['xd']['ServerMoid'] = server_mac['ServerMoid']
                            item['xd']['ServerInterface'] = server_mac['InterfaceDn']

        if not self.set_post_aci_lldp():
            return False

        return True
