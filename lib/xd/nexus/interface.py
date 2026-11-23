import copy
from lib import ip_helper
from lib.nexus import nxapi
from lib.nexus import helper as nexus_helper


class NexusInterface():
    def __init__(self):
        self.nexus_interface = None
        self.nexus_interface_state = None
        self.nexus_interface_brief = None
        self.nexus_transceiver = None

    def load_pre_nexus_transceiver(self):
        self.nexus_transceiver = self.get_pre_cache('nexus', 'transceiver')
        if self.nexus_transceiver is None:
            return False
        return True

    def set_post_nexus_transceiver(self):
        return self.set_post_cache('nexus-transceiver', self.nexus_transceiver)

    def load_post_nexus_transceiver(self):
        self.nexus_transceiver = self.get_post_cache('nexus-transceiver')
        if self.nexus_transceiver is None:
            return False
        return True

    def load_pre_nexus_interface_state(self):
        self.nexus_interface_state = self.get_pre_cache('nexus', 'interface')
        if self.nexus_interface_state is None:
            return False
        return True

    def set_post_nexus_interface_state(self):
        return self.set_post_cache('nexus-interface-state', self.nexus_interface_state)

    def load_post_nexus_interface_state(self):
        self.nexus_interface_state = self.get_post_cache('nexus-interface-state')
        if self.nexus_interface_state is None:
            return False
        return True

    def load_pre_nexus_interface_brief(self):
        self.nexus_interface_brief = self.get_pre_cache('nexus', 'interface-brief')
        if self.nexus_interface_brief is None:
            return False
        return True

    def set_post_nexus_interface_brief(self):
        return self.set_post_cache('nexus-interface-brief', self.nexus_interface_brief)

    def load_post_nexus_interface_brief(self):
        self.nexus_interface_brief = self.get_post_cache('nexus-interface-brief')
        if self.nexus_interface_brief is None:
            return False
        return True

    def set_post_nexus_interface(self):
        return self.set_post_cache('nexus-interface', self.nexus_interface)

    def load_post_nexus_interface(self):
        self.nexus_interface = self.get_post_cache('nexus-interface')
        if self.nexus_interface is None:
            return False
        return True

    def map_nexus_interface_reason(self, reason):
        if reason.lower() == 'xcvr not inserted':
            return 'No XCVR'

        if reason.lower() == 'link not connected':
            return 'No link'

        if reason.lower() == 'administratively down':
            return 'Admin down'

        return reason

    def get_nexus_interface(self):
        info = copy.deepcopy(
            self.nexus_interface
        )
        return info

    def get_nexus_interface_mgmt(self):
        info = []

        # Select management interface
        for nexus_name in self.nexus_interface:
            for item in self.nexus_interface[nexus_name]:
                if item['type'] == 'mgmt':
                    item['_index'] = int(item['interface'].split('mgmt')[1])
                    info.append(
                        item
                    )

        info = sorted(
            info,
            key = lambda i: (
                i['nexus_name'],
                i['_index']
            )
        )

        return info

    def get_nexus_interface_eth(self, nexus_name):
        info = []

        if nexus_name not in self.nexus_interface:
            return info

        # Select eth interface
        for item in self.nexus_interface[nexus_name]:
            if item['type'] == 'eth':
                info.append(
                    item
                )

        info = sorted(
            info,
            key = lambda i: (
                i['_index']
            )
        )

        return info

    def get_nexus_interfaces_pc(self):
        info = []

        for nexus_name in self.nexus_interface:
            for item in self.nexus_interface[nexus_name]:
                if item['type'] == 'pc':
                    info.append(
                        item
                    )

        info = sorted(
            info,
            key = lambda i: (
                i['_index']
            )
        )

        return info

    def get_nexus_interface_pc(self, nexus_name):
        info = []

        if nexus_name not in self.nexus_interface:
            return info

        # Select eth interface
        for item in self.nexus_interface[nexus_name]:
            if item['type'] == 'pc':
                info.append(
                    item
                )

        info = sorted(
            info,
            key = lambda i: (
                i['_index']
            )
        )

        return info

    def get_nexus_interface_vlan(self, nexus_name):
        info = []

        if nexus_name not in self.nexus_interface:
            return info

        # Select eth interface
        for item in self.nexus_interface[nexus_name]:
            if item['type'] == 'vlan':
                info.append(
                    item
                )

        info = sorted(
            info,
            key = lambda i: (
                i['_index']
            )
        )

        return info

    def prepare_nexus_interface_state(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_interface_state = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus interface: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_interface_state:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-interface' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_interface_state[nexus_device['name']] = cache
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

            interface = nexus_handler.get_interfaces()
            if interface is None:
                self.my_output.error('Interface failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_interface_state[nexus_device['name']] = interface

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-interface' % (nexus_device['name']),
                self.nexus_interface_state[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def prepare_nexus_interface_brief(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_interface_brief = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus interface: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_interface_brief:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-interface-brief' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_interface_brief[nexus_device['name']] = cache
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

            interface = nexus_handler.get_interfaces_brief()
            if interface is None:
                self.my_output.error('Interface brief failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_interface_brief[nexus_device['name']] = interface

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-interface-brief' % (nexus_device['name']),
                self.nexus_interface_brief[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def prepare_nexus_transceiver(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_transceiver = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus transceiver: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_transceiver:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-transceiver' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_transceiver[nexus_device['name']] = cache
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

            transceiver = nexus_handler.get_interfaces_trans()
            if transceiver is None:
                self.my_output.error('Interface trans failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_transceiver[nexus_device['name']] = transceiver

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-transceiver' % (nexus_device['name']),
                self.nexus_transceiver[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def run_nexus_interface_independent(self):
        # Merge all structures into one
        self.nexus_interface = {}
        for nexus_name in self.nexus_interface_brief:
            self.nexus_interface[nexus_name] = []
            for item in self.nexus_interface_brief[nexus_name]:
                for item_state in self.nexus_interface_state[nexus_name]:
                    if nexus_helper.is_nexus_interface_equal(item['interface'], item_state['interface']):
                        for key in item_state:
                            item[key] = item_state[key]

                item['transceiver'] = {}
                item['transceiver']['type'] = None
                for item_trans in self.nexus_transceiver[nexus_name]:
                    if item['interface'] == item_trans['interface']:
                        for key in item_trans:
                            item['transceiver'][key] = item_trans[key]

                self.nexus_interface[nexus_name].append(
                    item
                )

        # Add extra data in common structure
        for nexus_name in self.nexus_interface:
            for item in self.nexus_interface[nexus_name]:
                item['interface_id'] = nexus_helper.get_nexus_interface_id(item['interface'])
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        nexus_name,
                        item['interface']
                    )
                )

                if item['type'] == 'vlan':
                    item['configuration'] = self.nexus_configuration_interface_vlan[nexus_name][item['interface_id']]
                    item['vn_segment'] = None
                    if item['configuration'] is not None:
                        for line in item['configuration'].split('\n'):
                            if len(line.strip().split('vn-segment')) == 2:
                                item['vn_segment'] = line.strip().split('vn-segment')[1]

                    item['vlan_name'] = None
                    if item['configuration'] is not None:
                        for line in item['configuration'].split('\n'):
                            if len(line.strip().split('name')) == 2:
                                item['vlan_name'] = line.strip().split('name')[1]

                    if 'svi_desc' not in item:
                        item['svi_desc'] = None

                    if item['svi_rsn_desc'] is not None and item['svi_rsn_desc'].lower() == 'none':
                        item['svi_rsn_desc'] = None

                    item['_reason'] = None
                    if item['svi_rsn_desc'] is not None:
                        item['_reason'] = self.map_nexus_interface_reason(
                            item['svi_rsn_desc']
                        )

                    item['_index'] = int(nexus_helper.get_nexus_interface_id(item['interface']))

                if item['type'] == 'mgmt':
                    item['configuration'] = self.nexus_configuration_interface_mgmt[nexus_name]
                    item['_index'] = int(nexus_helper.get_nexus_interface_id(item['interface']))

                if item['type'] == 'eth':
                    item['configuration'] = self.nexus_configuration_interface_eth[nexus_name][item['interface_id']]

                    if 'desc' not in item:
                        item['desc'] = None

                    if item['state_rsn_desc'] is not None and item['state_rsn_desc'].lower() == 'none':
                        item['state_rsn_desc'] = None

                    item['_reason'] = None
                    if item['state_rsn_desc'] is not None:
                        item['_reason'] = self.map_nexus_interface_reason(
                            item['state_rsn_desc']
                        )

                    if 'eth_bundle' not in item:
                        item['eth_bundle'] = None

                    if len(item['interface'].split('/')) == 2:
                        item['_index'] = int(item['interface'].split('/')[1].split('.')[0])
                    else:
                        item['_index'] = int(item['interface'].split('/')[1]) * 1000 + int(item['interface'].split('/')[2])

        return True

    def run_nexus_interface_xd(self):
        for nexus_name in self.nexus_interface:
            for item in self.nexus_interface[nexus_name]:
                if item['type'] == 'pc':
                    item['configuration'] = self.nexus_configuration_interface_pc[nexus_name][item['interface_id']]

                    item['pc'] = None
                    if nexus_name in self.nexus_pc:
                        for pitem in self.nexus_pc[nexus_name]:
                            if nexus_helper.is_nexus_interface_equal(item['interface'], pitem['port-channel']):
                                item['pc'] = copy.deepcopy(
                                    pitem
                                )

                    if 'desc' not in item:
                        item['desc'] = None

                    if 'eth_hw_addr' not in item:
                        item['eth_hw_addr'] = None

                    if 'eth_members' not in item:
                        item['eth_members'] = None

                    if item['state_rsn_desc'] is not None and item['state_rsn_desc'].lower() == 'none':
                        item['state_rsn_desc'] = None

                    item['_reason'] = None
                    if item['state_rsn_desc'] is not None:
                        item['_reason'] = self.map_nexus_interface_reason(
                            item['state_rsn_desc']
                        )

                    if item['proto'] is not None and item['proto'].lower() == 'none':
                        item['proto'] = None

                    item['_index'] = int(nexus_helper.get_nexus_interface_id(item['interface']))

                if item['type'] in ['eth', 'mgmt']:
                    item['nei_device_type'] = None
                    item['nei_device_name'] = None
                    item['nei_device_id'] = None
                    item['nei_interface_name'] = None
                    item['nei_interface_hash'] = None
                    item['nei_is_vmware'] = False
                    item['nei_is_ocp'] = False
                    item['nei_index'] = 0
                    item['cdp_hash'] = None
                    item['lldp_hash'] = None

                    if nexus_name in self.nexus_cdp:
                        for citem in self.nexus_cdp[nexus_name]:
                            if nexus_helper.is_nexus_interface_equal(citem['intf_id'], item['interface']):
                                item['nei_device_type'] = citem['xd']['DeviceType']
                                item['nei_device_name'] = self.get_short_name(citem['sysname'])
                                if item['nei_device_name'] is None:
                                    item['nei_device_name'] = self.get_short_name(citem['device_id'])
                                item['nei_interface_name'] = citem['port_id']
                                if item['nei_device_type'] == 'Nexus':
                                    item['nei_interface_hash'] = ip_helper.get_string_md5(
                                        '%s %s' % (
                                            item['nei_device_name'],
                                            item['nei_interface_name']
                                        )
                                    )

                                if item['nei_device_type'] == 'FI':
                                    item['nei_interface_hash'] = self.get_fi_interface_hash(
                                        item['nei_device_name'],
                                        item['nei_interface_name']
                                    )
                                    if item['nei_interface_hash'] is None:
                                        self.log.error(
                                            'run_aci_phy',
                                            'Unexpected no fi intf hash for %s %s' % (item['nei_device_name'], item['nei_interface_name'])
                                        )

                                item['cdp_hash'] = citem['hash']

                    if nexus_name in self.nexus_lldp:
                        for litem in self.nexus_lldp[nexus_name]:
                            if nexus_helper.is_nexus_interface_equal(litem['l_port_id'], item['interface']):
                                if item['nei_device_name'] is None and litem['xd']['DeviceType'] is not None:
                                    if litem['xd']['DeviceType'] == 'Nexus':
                                        item['nei_device_type'] = litem['xd']['DeviceType']
                                        item['nei_device_name'] = litem['xd']['NexusDevice']
                                        if item['nei_device_name'] is None:
                                            item['nei_device_name'] = litem['xd']['DeviceSysName']

                                        if litem['port_type'] == 'Interface Name':
                                            item['nei_interface_name'] = litem['port_id']

                                    if litem['xd']['DeviceType'] == 'FI':
                                        item['nei_device_type'] = litem['xd']['DeviceType']
                                        item['nei_device_name'] = litem['xd']['FI']
                                        if litem['port_type'] == 'Interface Name':
                                            item['nei_interface_name'] = litem['port_id']

                                if item['nei_device_name'] is None and litem['xd']['DeviceType'] is None:
                                    item['nei_device_name'] = self.get_short_name(litem['sys_name'])
                                    if item['nei_device_name'] is None:
                                        if litem['sys_desc'] is not None:
                                            item['nei_device_name'] = ' '.join(litem['sys_desc'].split(' ')[:2])

                                item['lldp_hash'] = litem['hash']

                    if item['nexus_name'] in self.nexus_server:
                        for interface_id in self.nexus_server[item['nexus_name']]:
                            if nexus_helper.is_nexus_interface_equal(item['interface'], interface_id):
                                if item['nei_device_type'] is None:
                                    item['nei_device_type'] = 'Server'
                                    item['nei_device_name'] = self.nexus_server[item['nexus_name']][interface_id]['ServerName']
                                    item['nei_device_id'] = self.nexus_server[item['nexus_name']][interface_id]['ServerMoid']
                                    item['nei_interface_name'] = self.nexus_server[item['nexus_name']][interface_id]['ServerInterface']
                                    if self.get_server_vc_by_moid(item['nei_device_id']) is not None:
                                        item['nei_is_vmware'] = True
                    try:
                        item['nei_index'] = int(item['nei_interface_name'].split('Ethernet')[1].split('/')[1])
                    except BaseException:
                        pass

                    item['xd'] = copy.deepcopy(self.xd)

                    xd_completed = False
                    if nexus_name in self.nexus_cdp:
                        for citem in self.nexus_cdp[nexus_name]:
                            if nexus_helper.is_nexus_interface_equal(citem['intf_id'], item['interface']):
                                item['xd'] = copy.deepcopy(citem['xd'])
                                item['xd']['CdpHash'] = citem['hash']
                                item['cdp'] = copy.deepcopy(citem)
                                xd_completed = True

                    if nexus_name in self.nexus_lldp:
                        for litem in self.nexus_lldp[nexus_name]:
                            if nexus_helper.is_nexus_interface_equal(litem['l_port_id'], item['interface']):
                                if not xd_completed:
                                    item['xd'] = copy.deepcopy(litem['xd'])
                                item['xd']['LldpHash'] = litem['hash']

                if item['type'] == 'eth':
                    item['pc_state'] = None
                    item['vpc_state'] = None
                    if item['eth_bundle'] is not None:
                        item['pc_state'] = {}
                        for pitem in self.nexus_pc_state[nexus_name]:
                            match = False
                            for member in pitem['member']:
                                if member['port'] == item['interface']:
                                    match = True

                            if match:
                                item['pc_state'] = copy.deepcopy(
                                    pitem
                                )
                                break

                        if 'vpc' in self.nexus_vpc_state[nexus_name]:
                            match = False
                            for member in self.nexus_vpc_state[nexus_name]['vpc']:
                                if member['ifindex'] == item['eth_bundle']:
                                    match = True

                            if match:
                                item['vpc_state'] = copy.deepcopy(
                                    self.nexus_vpc_state[nexus_name]
                                )

                    item['vlans'] = []
                    for vlan in self.nexus_vlan[nexus_name]:
                        if item['interface'] in vlan['interfaces']:
                            item['vlans'].append(
                                vlan
                            )

        if not self.set_post_nexus_interface():
            return False

        if not self.set_post_nexus_interface_state():
            return False

        if not self.set_post_nexus_interface_brief():
            return False

        if not self.set_post_nexus_transceiver():
            return False

        return True