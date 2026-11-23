import copy
from lib import ip_helper
from lib.nexus import nxapi


class NexusCdp():
    def __init__(self):
        self.nexus_cdp = None

    def load_pre_nexus_cdp(self):
        self.nexus_cdp = self.get_pre_cache('nexus', 'cdp')
        if self.nexus_cdp is None:
            return False
        return True

    def set_post_nexus_cdp(self):
        return self.set_post_cache('nexus-cdp', self.nexus_cdp)

    def load_post_nexus_cdp(self):
        self.nexus_cdp = self.get_post_cache('nexus-cdp')
        if self.nexus_cdp is None:
            return False
        return True

    def get_nexus_cdp(self):
        info = copy.deepcopy(self.nexus_cdp)
        return info

    def prepare_nexus_cdp(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_cdp = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus cdp: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_cdp:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-cdp' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_cdp[nexus_device['name']] = cache
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

            self.nexus_cdp[nexus_device['name']] = []

            neighbors = nexus_handler.get_cdps()
            if neighbors is None:
                self.my_output.error('CDP failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.my_output.debug('Data collected')

            for neighbor in neighbors:
                neighbor['device_name'] = nexus_device['name']

                self.nexus_cdp[nexus_device['name']].append(
                    neighbor
                )

            self.set_cache(
                'nexus-%s-cdp' % (nexus_device['name']),
                self.nexus_cdp[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def run_nexus_cdp(self):
        for key in self.nexus_cdp:
            for item in self.nexus_cdp[key]:
                item['xd'] = copy.deepcopy(self.xd)

        for key in self.nexus_cdp:
            for item in self.nexus_cdp[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['nexus_name'],
                        item['intf_id']
                    )
                )

                if 'sysname' not in item or item['sysname'] is None:
                    item['sysname'] = None
                    continue

                if 'version' not in item or item['version'] is None:
                    continue

                if item['version'].startswith('Cisco Nexus Operating System'):
                    item['xd']['DeviceSysName'] = item['sysname']
                    nexus = self.get_nexus_device_by_hostname(
                        item['sysname']
                    )
                    if nexus is not None:
                        item['xd']['DeviceType'] = 'Nexus'
                        item['xd']['NexusDevice'] = copy.deepcopy(nexus)
                        continue

                    item['xd']['FI'] = self.get_fi_by_mac(
                        item['remote_intf_mac']
                    )
                    if item['xd']['FI'] is not None:
                        item['xd']['DeviceType'] = 'FI'
                        continue

                    if self.get_fi_by_name(item['xd']['DeviceSysName']):
                        item['xd']['DeviceType'] = 'FI'
                        continue

                    aci = self.get_aci_node_by_name(
                        item['sysname']
                    )
                    if aci is not None:
                        item['xd']['DeviceType'] = 'ACI'
                        item['xd']['AciApicName'] = aci['apic']
                        item['xd']['AciNodeName'] = aci['name']
                        item['xd']['AciNodeId'] = self.get_aci_node_id_by_name(aci['name'])
                        item['xd']['AciNodeRef'] = '%s-%s' % (aci['apic'], aci['name'])

                    continue

                if self.server_macs is None:
                    continue

                for server_mac in self.server_macs:
                    if 'remote_intf_mac' in item and item['remote_intf_mac'] is not None:
                        if ip_helper.is_mac_equal(item['remote_intf_mac'], server_mac['MacAddress']):
                            item['xd']['DeviceType'] = 'Server'
                            item['xd']['ServerName'] = server_mac['ServerName']
                            item['xd']['ServerMoid'] = server_mac['ServerMoid']

        if not self.set_post_nexus_cdp():
            return False

        return True
