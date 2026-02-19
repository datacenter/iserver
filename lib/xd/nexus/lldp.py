import copy
from lib import ip_helper
from lib.nexus import nxapi
from lib.nexus import helper as nexus_helper


class NexusLldp():
    def __init__(self):
        self.nexus_lldp = None

    def load_pre_nexus_lldp(self):
        self.nexus_lldp = self.get_pre_cache('nexus', 'lldp')
        if self.nexus_lldp is None:
            return False
        return True

    def set_post_nexus_lldp(self):
        return self.set_post_cache('nexus-lldp', self.nexus_lldp)

    def load_post_nexus_lldp(self):
        self.nexus_lldp = self.get_post_cache('nexus-lldp')
        if self.nexus_lldp is None:
            return False
        return True

    def get_nexus_device_names(self):
        names = []
        for key in self.nexus_lldp:
            names.append(key)

        names = sorted(names)
        return names

    def get_nexus_lldp(self):
        info = copy.deepcopy(self.nexus_lldp)
        return info

    def prepare_nexus_lldp(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_lldp = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus lldp: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_lldp:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-lldp' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_lldp[nexus_device['name']] = cache
                    self.my_output.debug('L3 Cache hit')
                    continue

            self.my_output.debug('Cache miss')

            if 'handler' in nexus_device:
                nexus_handler = nexus_device['handler']
            else:
                nexus_handler = nxapi.NxApi(
                    nexus_device['ip'],
                    nexus_device['username'],
                    nexus_device['password'],
                    nexus_device['nxapi'],
                    name=nexus_device['name'],
                    log_id=self.log_id,
                    cache_enabled=False,
                    debug=True,
                    paranoid=self.paranoid
                )

            self.nexus_lldp[nexus_device['name']] = []

            neighbors = nexus_handler.get_lldps()
            if neighbors is None:
                self.my_output.error('LLDP failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.my_output.debug('Data collected')

            for neighbor in neighbors:
                neighbor['device_name'] = nexus_device['name']

                self.nexus_lldp[nexus_device['name']].append(
                    neighbor
                )

            self.set_cache(
                'nexus-%s-lldp' % (nexus_device['name']),
                self.nexus_lldp[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def run_nexus_lldp(self):
        for key in self.nexus_lldp:
            for item in self.nexus_lldp[key]:
                item['xd'] = copy.deepcopy(self.xd)

        for key in self.nexus_lldp:
            for item in self.nexus_lldp[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['nexus_name'],
                        item['l_port_id']
                    )
                )

                item['l_port_hash'] = nexus_helper.get_nexus_interface_hash(
                    item['nexus_name'],
                    item['l_port_id']
                )

                if item['port_desc'] is not None and item['port_desc'] == 'null':
                    item['port_desc'] = None

                if item['sys_name'] is not None and item['sys_name'] == 'null':
                    item['sys_name'] = None

                if item['sys_desc'] is None:
                    continue

                if item['sys_desc'].startswith('Cisco Nexus Operating System'):
                    item['xd']['DeviceType'] = 'Nexus'
                    item['xd']['DeviceSysName'] = item['sys_name']
                    item['xd']['NexusDevice'] = self.get_nexus_device_by_hostname(
                        item['sys_name']
                    )
                    if item['xd']['NexusDevice'] is None:
                        item['xd']['FI'] = self.get_fi_by_mac(
                            item['chassis_id']
                        )
                        if item['xd']['FI'] is not None:
                            item['xd']['DeviceType'] = 'FI'

                if item['sys_desc'].startswith('topology') and len(item['sys_desc'].split('/')) == 3:
                    item['xd']['DeviceType'] = 'ACI'
                    item['xd']['DeviceSysName'] = item['sys_name']
                    node_info = self.get_aci_node_by_id(
                        item['sys_desc'].split('/')[2].split('-')[1]
                    )
                    if node_info is not None:
                        item['xd']['AciApicName'] = node_info['apic']
                        item['xd']['AciNodeName'] = node_info['node']
                        item['xd']['AciNodeId'] = self.get_aci_node_id_by_name(node_info['node'])
                        item['xd']['AciNodeRef'] = '%s-%s' % (node_info['apic'], node_info['node'])

        for key in self.nexus_lldp:
            for item in self.nexus_lldp[key]:
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

        if not self.set_post_nexus_lldp():
            return False

        return True
