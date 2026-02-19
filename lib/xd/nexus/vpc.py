import copy
from lib import ip_helper
from lib.nexus import nxapi
from lib.nexus import helper as nexus_helper


class NexusVpc():
    def __init__(self):
        self.nexus_vpc_keepalive = None
        self.nexus_vpc_role = None
        self.nexus_vpc_state = None

    def load_pre_nexus_vpc_keepalive(self):
        self.nexus_vpc_keepalive = self.get_pre_cache('nexus', 'vpc-keepalive')
        if self.nexus_vpc_keepalive is None:
            return False
        return True

    def set_post_nexus_vpc_keepalive(self):
        return self.set_post_cache('nexus-vpc-keepalive', self.nexus_vpc_keepalive)

    def load_post_nexus_vpc_keepalive(self):
        self.nexus_vpc_keepalive = self.get_post_cache('nexus-vpc-keepalive')
        if self.nexus_vpc_keepalive is None:
            return False
        return True

    def load_pre_nexus_vpc_role(self):
        self.nexus_vpc_role = self.get_pre_cache('nexus', 'vpc-role')
        if self.nexus_vpc_role is None:
            return False
        return True

    def set_post_nexus_vpc_role(self):
        return self.set_post_cache('nexus-vpc-role', self.nexus_vpc_role)

    def load_post_nexus_vpc_role(self):
        self.nexus_vpc_role = self.get_post_cache('nexus-vpc-role')
        if self.nexus_vpc_role is None:
            return False
        return True

    def load_pre_nexus_vpc_state(self):
        self.nexus_vpc_state = self.get_pre_cache('nexus', 'vpc-state')
        if self.nexus_vpc_state is None:
            return False
        return True

    def set_post_nexus_vpc_state(self):
        return self.set_post_cache('nexus-vpc-state', self.nexus_vpc_state)

    def load_post_nexus_vpc_state(self):
        self.nexus_vpc_state = self.get_post_cache('nexus-vpc-state')
        if self.nexus_vpc_state is None:
            return False
        return True

    def map_vpc_peer_state(self, state):
        if state == 1:
            return 'Up'

        if state == 0:
            return 'Down'

        return 'Unknown (%s)' % (state)

    def map_vpc_member_state(self, state):
        if state == 1:
            return 'Up'

        if state == 0:
            return 'Down'

        return 'Unknown (%s)' % (state)

    def map_vpc_peer_operational_role(self, role):
        if role == 'primary':
            return 'Primary'

        if role == 'secondary-primary':
            return 'Primary'

        return 'Secondary'

    def get_nexus_vpc_domain(self, nexus_name):
        if nexus_name in self.nexus_vpc_state:
            info = copy.deepcopy(
                self.nexus_vpc_state[nexus_name]
            )
            return info

        return None

    def get_nexus_vpc_domains(self):
        info = copy.deepcopy(
            self.nexus_vpc_state
        )
        return info

    def get_nexus_vpc_keepalive(self):
        info = copy.deepcopy(self.nexus_vpc_keepalive)
        return info

    def prepare_nexus_vpc_keepalive(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_vpc_keepalive = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus vpc keepalive: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_vpc_keepalive:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-vpc-keepalive' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_vpc_keepalive[nexus_device['name']] = cache
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

            if not nexus_handler.is_feature_enabled('vpc'):
                info = {}
                info['__enabled'] = False
            else:
                info = nexus_handler.get_vpc_keepalive()
                if info is None:
                    self.my_output.error('VPC keepalive failed: %s' % (nexus_device['name']))
                    success = False
                    continue
                info['__enabled'] = True

            self.nexus_vpc_keepalive[nexus_device['name']] = info

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-vpc-keepalive' % (nexus_device['name']),
                self.nexus_vpc_keepalive[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def get_nexus_vpc_role(self):
        info = copy.deepcopy(self.nexus_vpc_role)
        return info

    def prepare_nexus_vpc_role(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_vpc_role = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus vpc role: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_vpc_role:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-vpc-role' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_vpc_role[nexus_device['name']] = cache
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

            if not nexus_handler.is_feature_enabled('vpc'):
                info = {}
                info['__enabled'] = False
            else:
                info = nexus_handler.get_vpc_role()
                if info is None:
                    self.my_output.error('VPC role failed: %s' % (nexus_device['name']))
                    success = False
                    continue
                info['__enabled'] = True

            self.nexus_vpc_role[nexus_device['name']] = info

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-vpc-role' % (nexus_device['name']),
                self.nexus_vpc_role[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def get_nexus_vpc_state(self):
        info = copy.deepcopy(self.nexus_vpc_state)
        return info

    def prepare_nexus_vpc_state(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_vpc_state = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus vpc state: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_vpc_state:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-vpc-state' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_vpc_state[nexus_device['name']] = cache
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

            if not nexus_handler.is_feature_enabled('vpc'):
                info = {}
                info['__enabled'] = False
            else:
                info = nexus_handler.get_vpc_state()
                if info is None:
                    self.my_output.error('VPC state failed: %s' % (nexus_device['name']))
                    success = False
                    continue
                info['__enabled'] = True

            self.nexus_vpc_state[nexus_device['name']] = info

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-vpc-state' % (nexus_device['name']),
                self.nexus_vpc_state[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def run_nexus_vpc(self):
        # Augment nexus_vpc_state
        for nexus_name in self.nexus_vpc_state:
            self.nexus_vpc_state[nexus_name]['configuration'] = self.nexus_configuration_vpc_domain[nexus_name]

            if 'peer' not in self.nexus_vpc_state[nexus_name]:
                self.nexus_vpc_state[nexus_name]['peer'] = []
                continue

            if 'vpc-role' not in self.nexus_vpc_state[nexus_name]:
                continue

            for key in self.nexus_vpc_role[nexus_name]:
                self.nexus_vpc_state[nexus_name][key] = self.nexus_vpc_role[nexus_name][key]

            for key in self.nexus_vpc_keepalive[nexus_name]:
                self.nexus_vpc_state[nexus_name][key] = self.nexus_vpc_keepalive[nexus_name][key]

            self.nexus_vpc_state[nexus_name]['_role'] = self.map_vpc_peer_operational_role(
                self.nexus_vpc_state[nexus_name]['vpc-role']
            )
            if self.nexus_vpc_state[nexus_name]['_role'] == 'Primary':
                self.nexus_vpc_state[nexus_name]['_role_flag'] = 'P'
            else:
                self.nexus_vpc_state[nexus_name]['_role_flag'] = 'S'

            for peer in self.nexus_vpc_state[nexus_name]['peer']:
                peer['_state'] = self.map_vpc_peer_state(
                    peer['state']
                )
                peer['port-channel'] = None
                peer['hash'] = None
                if nexus_helper.get_nexus_interface_type(peer['ifindex']) == 'pc':
                    peer['port-channel'] = 'port-channel%s' % (
                        nexus_helper.get_nexus_interface_id(peer['ifindex'])
                    )
                    peer['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        nexus_name,
                        peer['port-channel']
                    )
                )
                if nexus_name in self.nexus_interface:
                    peer['xd'] = []
                    peer['eth'] = []
                    for interface_info in self.nexus_interface[nexus_name]:
                        if interface_info['type'] == 'eth':
                            if interface_info['eth_bundle'] is not None and interface_info['eth_bundle'] == peer['ifindex']:
                                if 'xd' in interface_info:
                                    peer['xd'].append(
                                        interface_info['xd']
                                    )
                                    peer['eth'].append(
                                        interface_info['interface']
                                    )

                    peer['_eth'] = ', '.join(peer['eth'])

            if 'vpc' in self.nexus_vpc_state[nexus_name]:
                for vpc in self.nexus_vpc_state[nexus_name]['vpc']:
                    vpc['_state'] = self.map_vpc_member_state(
                        vpc['state']
                    )
                    vpc['port-channel'] = None
                    vpc['hash'] = None
                    if nexus_helper.get_nexus_interface_type(vpc['ifindex']) == 'pc':
                        vpc['port-channel'] = 'port-channel%s' % (
                            nexus_helper.get_nexus_interface_id(vpc['ifindex'])
                        )
                        vpc['hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            nexus_name,
                            vpc['port-channel']
                        )
                    )

                    if nexus_name in self.nexus_interface:
                        vpc['xd'] = []
                        vpc['eth'] = []
                        for interface_info in self.nexus_interface[nexus_name]:
                            if interface_info['type'] == 'eth':
                                if interface_info['eth_bundle'] is not None and interface_info['eth_bundle'] == vpc['ifindex']:
                                    if 'xd' in interface_info:
                                        vpc['xd'].append(
                                            interface_info['xd']
                                        )
                                        vpc['eth'].append(
                                            interface_info['interface']
                                        )

                        vpc['_eth'] = ', '.join(vpc['eth'])

        for nexus_name in self.nexus_vpc_state:
            self.nexus_vpc_state[nexus_name]['peer_nexus'] = None
            self.nexus_vpc_state[nexus_name]['peer_configuration'] = None
            for peer in self.nexus_vpc_state[nexus_name]['peer']:
                if 'xd' in peer:
                    for peer_xd in peer['xd']:
                        if peer_xd['DeviceType'] is not None and peer_xd['DeviceType'] == 'Nexus':
                            self.nexus_vpc_state[nexus_name]['peer_nexus'] = peer_xd['NexusDevice']
                            if peer_xd['NexusDevice'] in self.nexus_vpc_state:
                                if 'configuration' in self.nexus_vpc_state[peer_xd['NexusDevice']]:
                                    self.nexus_vpc_state[nexus_name]['peer_configuration'] = self.nexus_vpc_state[peer_xd['NexusDevice']]['configuration']

        if not self.set_post_nexus_vpc_keepalive():
            return False

        if not self.set_post_nexus_vpc_role():
            return False

        if not self.set_post_nexus_vpc_state():
            return False

        return True
