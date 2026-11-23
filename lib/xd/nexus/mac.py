import copy
from lib import ip_helper
from lib.nexus import nxapi


class NexusMac():
    def __init__(self):
        self.nexus_mac_table = None

    def load_pre_nexus_mac(self):
        self.nexus_mac_table = self.get_pre_cache('nexus', 'mac')
        if self.nexus_mac_table is None:
            return False
        return True

    def set_post_nexus_mac(self):
        return self.set_post_cache('nexus-mac', self.nexus_mac_table)

    def load_post_nexus_mac(self):
        self.nexus_mac_table = self.get_post_cache('nexus-mac')
        if self.nexus_mac_table is None:
            return False
        return True

    def get_nexus_mac_table(self):
        info = copy.deepcopy(self.nexus_mac_table)
        return info

    def prepare_nexus_mac_table(self, leaf_ports_only=False, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_mac_table = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus mac: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_mac_table:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-mac' % (nexus_device['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.nexus_mac_table[nexus_device['name']] = cache
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

            self.nexus_mac_table[nexus_device['name']] = []
            macs = nexus_handler.get_macs()
            if macs is None:
                self.my_output.error('MAC failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.my_output.debug('Data collected')

            all_macs = []
            for mac in macs:
                mac['device_name'] = nexus_device['name']
                all_macs.append(
                    mac
                )

            self.set_cache(
                'nexus-%s-mac' % (nexus_device['name']),
                all_macs
            )

            self.my_output.debug('Cache set')

        return success

    def get_nexus_mac_info(self, mac_address):
        info = {}

        info['src'] = []
        info['intf'] = []
        info['lldp'] = []
        info['mac'] = []

        for device_name in self.nexus_lldp:
            for item in self.nexus_lldp[device_name]:
                if item['chassis_type'] == 'Mac Address':
                    if ip_helper.is_mac_equal(item['chassis_id'], mac_address):
                        found = False
                        for sitem in info['lldp']:
                            equal = True
                            for key in ['chassis_type', 'chassis_id', 'port_type', 'port_id', 'port_desc', 'l_port_id', 'mac', 'sys_name', 'sys_desc']:
                                if sitem[key] != item[key]:
                                    equal = False
                                    break

                            if equal:
                                found = True
                                break

                        if found:
                            continue

                        info['lldp'].append(
                            item
                        )

                        iinfo = '%s:%s' % (
                            item['device_name'],
                            item['l_port_id']
                        )

                        if iinfo not in info['intf']:
                            info['intf'].append(
                                iinfo
                            )

                        if 'lldp' not in info['src']:
                            info['src'].append('lldp')

                if item['port_type'] == 'Mac Address':
                    if ip_helper.is_mac_equal(item['port_id'], mac_address):
                        found = False
                        for sitem in info['lldp']:
                            equal = True
                            for key in ['chassis_type', 'chassis_id', 'port_type', 'port_id', 'port_desc', 'l_port_id', 'mac', 'sys_name', 'sys_desc']:
                                if sitem[key] != item[key]:
                                    equal = False
                                    break

                            if equal:
                                found = True
                                break

                        if found:
                            continue

                        info['lldp'].append(
                            item
                        )

                        iinfo = '%s:%s' % (
                            item['device_name'],
                            item['l_port_id']
                        )

                        if iinfo not in info['intf']:
                            info['intf'].append(
                                iinfo
                            )

                        if 'lldp' not in info['src']:
                            info['src'].append('lldp')

        for device_name in self.nexus_mac_table:
            for item in self.nexus_mac_table[device_name]:
                if ip_helper.is_mac_equal(item['mac_addr'], mac_address):
                    if item['port'].startswith('Eth'):
                        info['mac'].append(
                            item
                        )

                        iinfo = '%s:%s' % (
                            item['device_name'],
                            item['port']
                        )

                        if iinfo not in info['intf']:
                            info['intf'].append(
                                iinfo
                            )

                        if 'mac-table' not in info['src']:
                            info['src'].append('mac-table')

        return info

    def filter_mac_table(self, device_name, table):
        items = []
        for item in table:
            if self.is_switch(device_name, item['port']):
                continue

            items.append(
                item
            )

        return items

    def run_nexus_mac_table(self, leaf_ports_only=True):
        if leaf_ports_only:
            for nexus_device_name in self.nexus_mac_table:
                self.nexus_mac_table[nexus_device_name] = self.filter_mac_table(
                    nexus_device_name,
                    self.nexus_mac_table[nexus_device_name]
                )

        for nexus_device_name in self.nexus_mac_table:
            for item in self.nexus_mac_table[nexus_device_name]:
                item['ServerMoid'] = None
                item['ServerName'] = None
                item['ServerInterface'] = None
                if self.server_macs is None:
                    continue

                for server_mac in self.server_macs:
                    if ip_helper.is_mac_equal(item['mac_addr'], server_mac['MacAddress']):
                        item['ServerName'] = server_mac['ServerName']
                        item['ServerMoid'] = server_mac['ServerMoid']
                        item['ServerInterface'] = server_mac['InterfaceDn'].split('/')[-1]

        if not self.set_post_nexus_mac():
            return False

        return True
