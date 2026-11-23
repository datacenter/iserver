import copy
from lib import ip_helper
from lib.nexus import nxapi
from lib.nexus import helper as nexus_helper


class NexusPc():
    def __init__(self):
        self.nexus_pc_database = None
        self.nexus_pc_lb = None
        self.nexus_pc_state = None
        self.nexus_pc_traffic = None
        self.nexus_pc = None

    def load_pre_nexus_pc_database(self):
        self.nexus_pc_database = self.get_pre_cache('nexus', 'pc-database')
        if self.nexus_pc_database is None:
            return False
        return True

    def set_post_nexus_pc_database(self):
        return self.set_post_cache('nexus-pc-database', self.nexus_pc_database)

    def load_post_nexus_pc_database(self):
        self.nexus_pc_database = self.get_post_cache('nexus-pc-database')
        if self.nexus_pc_database is None:
            return False
        return True

    def load_pre_nexus_pc_lb(self):
        self.nexus_pc_lb = self.get_pre_cache('nexus', 'pc-lb')
        if self.nexus_pc_lb is None:
            return False
        return True

    def set_post_nexus_pc_lb(self):
        return self.set_post_cache('nexus-pc-lb', self.nexus_pc_lb)

    def load_post_nexus_pc_lb(self):
        self.nexus_pc_lb = self.get_post_cache('nexus-pc-lb')
        if self.nexus_pc_lb is None:
            return False
        return True

    def load_pre_nexus_pc_state(self):
        self.nexus_pc_state = self.get_pre_cache('nexus', 'pc-state')
        if self.nexus_pc_state is None:
            return False
        self.set_post_nexus_pc_state()
        return True

    def set_post_nexus_pc_state(self):
        return self.set_post_cache('nexus-pc-state', self.nexus_pc_state)

    def load_post_nexus_pc_state(self):
        self.nexus_pc_state = self.get_post_cache('nexus-pc-state')
        if self.nexus_pc_state is None:
            return False
        return True

    def load_pre_nexus_pc_traffic(self):
        self.nexus_pc_traffic = self.get_pre_cache('nexus', 'pc-traffic')
        if self.nexus_pc_traffic is None:
            return False
        return True

    def set_post_nexus_pc_traffic(self):
        return self.set_post_cache('nexus-pc-traffic', self.nexus_pc_traffic)

    def load_post_nexus_pc_traffic(self):
        self.nexus_pc_traffic = self.get_post_cache('nexus-pc-traffic')
        if self.nexus_pc_traffic is None:
            return False
        return True

    def set_post_nexus_pc(self):
        return self.set_post_cache('nexus-pc', self.nexus_pc_traffic)

    def load_post_nexus_pc(self):
        self.nexus_pc = self.get_post_cache('nexus-pc')
        if self.nexus_pc is None:
            return False
        return True

    def map_pc_flag(self, flag):
        flags = {}
        flags['D'] = 'Down'
        flags['U'] = 'Up'
        flags['P'] = 'Up'
        flags['p'] = 'Up in delay-lacp mode'

        if flag in flags:
            return flags[flag]

        return flag

    def prepare_nexus_pc_database(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_pc_database = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus pc database: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_pc_database:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-pc-database' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_pc_database[nexus_device['name']] = cache
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

            info = nexus_handler.get_pc_database()
            if info is None:
                self.my_output.error('PC database failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_pc_database[nexus_device['name']] = info

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-pc-database' % (nexus_device['name']),
                self.nexus_pc_database[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def prepare_nexus_pc_lb(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_pc_lb = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus pc lb: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_pc_lb:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-pc-lb' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_pc_lb[nexus_device['name']] = cache
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

            info = nexus_handler.get_pc_lb()
            if info is None:
                self.my_output.error('PC lb failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_pc_lb[nexus_device['name']] = info

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-pc-lb' % (nexus_device['name']),
                self.nexus_pc_lb[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def prepare_nexus_pc_state(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_pc_state = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus pc state: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_pc_state:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-pc-state' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_pc_state[nexus_device['name']] = cache
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

            info = nexus_handler.get_pc_state()
            if info is None:
                self.my_output.error('PC state failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_pc_state[nexus_device['name']] = info

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-pc-state' % (nexus_device['name']),
                self.nexus_pc_state[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def prepare_nexus_pc_traffic(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_pc_traffic = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus pc traffic: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_pc_traffic:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-pc-traffic' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_pc_traffic[nexus_device['name']] = cache
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

            info = nexus_handler.get_pc_traffic()
            if info is None:
                self.my_output.error('PC traffic failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_pc_traffic[nexus_device['name']] = info

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-pc-traffic' % (nexus_device['name']),
                self.nexus_pc_traffic[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def run_nexus_pc(self):
        self.nexus_pc = {}

        for nexus_name in self.nexus_pc_state:
            for item in self.nexus_pc_state[nexus_name]:
                item['configuration'] = self.nexus_configuration_interface_pc[nexus_name][
                    nexus_helper.get_nexus_interface_id(item['port-channel'])
                ]
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        nexus_name,
                        item['port-channel']
                    )
                )
                item['_state'] = self.map_pc_flag(
                    item['status']
                )
                for member in item['member']:
                    member['hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            nexus_name,
                            member['port']
                        )
                    )
                    member['_state'] = self.map_pc_flag(
                        member['status']
                    )

        for nexus_name in self.nexus_pc_state:
            self.nexus_pc[nexus_name] = []

            for item in self.nexus_pc_state[nexus_name]:
                # Traffic
                for member in item['member']:
                    for titem in self.nexus_pc_traffic[nexus_name]:
                        if item['port-channel'] == 'port-channel%s' % (titem['chanId']):
                            if member['port'] == titem['port']:
                                keys = [
                                    'rx-ucst',
                                    'tx-ucst',
                                    'rx-mcst',
                                    'tx-mcst',
                                    'rx-bcst',
                                    'tx-bcst'
                                ]
                                for key in keys:
                                    member[key] = titem[key]

                # Eth
                item['ifs'] = []
                item['ids'] = []

                if nexus_name in self.nexus_interface:
                    for eitem in self.nexus_interface[nexus_name]:
                        for member in item['member']:
                            if nexus_helper.is_nexus_interface_equal(member['port'], eitem['interface']):
                                member['eth'] = copy.deepcopy(
                                    eitem
                                )
                                item['ifs'].append(
                                    eitem['interface']
                                )
                                item['ids'].append(
                                    nexus_helper.get_nexus_interface_id(
                                        eitem['interface']
                                    )
                                )

                item['_ifs'] = ','.join(item['ifs'])
                item['_ids'] = ','.join(item['ids'])

                self.nexus_pc[nexus_name].append(
                    item
                )

        if not self.set_post_nexus_pc_database():
            return False

        if not self.set_post_nexus_pc_lb():
            return False

        if not self.set_post_nexus_pc_state():
            return False

        if not self.set_post_nexus_pc_traffic():
            return False

        if not self.set_post_nexus_pc():
            return False

        return True
