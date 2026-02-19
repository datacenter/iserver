import copy
from lib import file_helper
from lib.nexus import nxapi
from lib.nexus import helper as nexus_helper


class NexusConfiguration():
    def __init__(self):
        self.nexus_configuration = None

        self.nexus_hostname = None
        self.nexus_configuration_interface_eth = None
        self.nexus_configuration_interface_pc = None
        self.nexus_configuration_interface_vlan = None
        self.nexus_configuration_interface_mgmt = None
        self.nexus_configuration_vpc_domain = None

    def load_pre_nexus_configuration(self):
        self.nexus_configuration = self.get_pre_cache('nexus', 'configuration')
        if self.nexus_configuration is None:
            return False

        self.analyze_nexus_configuration()
        return True

    def set_post_nexus_configuration(self):
        return self.set_post_cache('nexus-configuration', self.nexus_configuration)

    def load_post_nexus_configuration(self):
        self.nexus_configuration = self.get_post_cache('nexus-configuration')
        if self.nexus_configuration is None:
            return False

        self.analyze_nexus_configuration()
        return True

    def get_nexus_configuration_vpc_domain(self):
        info = copy.deepcopy(self.nexus_configuration_vpc_domain)
        file_helper.set_file_json(
            '/tmp/nexus_configuration_vpc_domain.json',
            info
        )
        return info

    def is_nexus_device_name(self, name):
        if name in self.nexus_hostname:
            return True
        return False

    def get_nexus_device_by_hostname(self, hostname):
        for device_name in self.nexus_hostname:
            for item in self.nexus_hostname[device_name]:
                if item == hostname:
                    return device_name
        return None

    def get_nexus_configuration(self):
        info = copy.deepcopy(self.nexus_configuration)
        return info

    def prepare_nexus_hostname(self, device_name, configuration):
        hostname = None
        for line in configuration.split('\n'):
            if line.startswith('hostname '):
                hostname = line.split('hostname ')[1]

        if hostname is None:
            return

        domain_name = None
        for line in configuration.split('\n'):
            if line.startswith('ip domain-name '):
                domain_name = line.split('ip domain-name ')[1]

        self.nexus_hostname[device_name].append(
            hostname
        )

        if domain_name is not None:
            self.nexus_hostname[device_name].append(
                '%s.%s' % (hostname, domain_name)
            )

    def analyze_nexus_configuration(self):
        self.nexus_hostname = {}
        self.nexus_configuration_interface_eth = {}
        self.nexus_configuration_interface_pc = {}
        self.nexus_configuration_interface_vlan = {}
        self.nexus_configuration_interface_mgmt = {}
        self.nexus_configuration_vpc_domain = {}

        for nexus_device_name in self.nexus_configuration:
            self.nexus_configuration_interface_eth[nexus_device_name] = {}
            self.nexus_configuration_interface_pc[nexus_device_name] = {}
            self.nexus_configuration_interface_vlan[nexus_device_name] = {}
            self.nexus_configuration_interface_mgmt[nexus_device_name] = {}
            self.nexus_configuration_vpc_domain[nexus_device_name] = {}

            if self.nexus_configuration[nexus_device_name] is None:
                continue

            configuration = self.nexus_configuration[nexus_device_name]

            ids = nexus_helper.get_config_interface_ethernet_ids(configuration)
            for interface_id in ids:
                self.nexus_configuration_interface_eth[nexus_device_name][interface_id] = nexus_helper.get_config_interface_ethernet(configuration, interface_id)

            ids = nexus_helper.get_config_interface_pc_ids(configuration)
            for interface_id in ids:
                self.nexus_configuration_interface_pc[nexus_device_name][interface_id] = nexus_helper.get_config_interface_pc(configuration, interface_id)

            ids = nexus_helper.get_config_interface_vlan_ids(configuration)
            for interface_id in ids:
                self.nexus_configuration_interface_vlan[nexus_device_name][interface_id] = nexus_helper.get_config_interface_vlan(configuration, interface_id)

            self.nexus_configuration_vpc_domain[nexus_device_name] = nexus_helper.get_config_vpc_domain(configuration)
            self.nexus_configuration_interface_mgmt[nexus_device_name] = nexus_helper.get_config_interface_mgmt(configuration)

            self.nexus_hostname[nexus_device_name] = []
            if self.nexus_configuration[nexus_device_name] is not None:
                self.prepare_nexus_hostname(
                    nexus_device_name,
                    configuration['configuration']
                )

    def prepare_nexus_configuration(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_configuration = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus configuration: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_configuration:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-configuration' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_configuration[nexus_device['name']] = cache
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

            self.nexus_configuration[nexus_device['name']] = nexus_handler.get_config()
            if self.nexus_configuration[nexus_device['name']] is None:
                self.my_output.error('Configuration failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-configuration' % (nexus_device['name']),
                self.nexus_configuration[nexus_device['name']]
            )

        self.analyze_nexus_configuration()
        return success

    def run_nexus_configuration(self):
        if not self.set_post_nexus_configuration():
            return False

        return True
