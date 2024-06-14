import os
import uuid
import time
import json
import traceback
import logging

from lib.webex_bot.commands import validations
from lib.webex_bot.models.command import Command
from lib.intersight import compute
from lib.intersight import bot_output
from lib.intersight import validations as intersight_validations
from lib.nexus import settings as nexus_settings
from lib.nexus import nxapi
from lib.aci import settings as aci_settings
from lib.aci import apic
from lib import log_helper
from lib import ip_helper
from lib import filter_helper
from lib import file_helper

logger = logging.getLogger(__name__)


class GetServerCommand(Command):
    def __init__(self, my_webex_api_handler, url):
        super().__init__(
            command_keyword="get server",
            help_message="get server",
            card=None,
        )
        self.run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(self.run_id)
        self.log_handler.initialize()
        self.link = 'https://wwwin-github.cisco.com/emear-telcocloud/iserver/blob/master/doc/bot/GetServer.md'
        self.url = url
        logger.info('Command initialized: get server [%s]', self.run_id[4:])

        self.my_webex_api_handler = my_webex_api_handler

    def help(self):
        output = 'Get state and inventory information about the Intersight managed servers.<br><br>'
        output = '%s- get server all<br>' % (output)
        output = '%s- get server name:p2b<br>' % (output)
        output = '%s- get server ip:10.1.1.1<br>' % (output)
        output = '%s- get server serial:WZP666666<br>' % (output)
        output = '%s- get server model:m5sn<br>' % (output)
        output = '%s- get server cpu-vendor:amd view:cpu<br>' % (output)
        output = '%s- get server gpu-slot:gt0 view:gpu<br>' % (output)
        output = '%s- get server pci-model:xxv710 view:pci<br>' % (output)
        output = '%s- get server mac:85ab view:net<br>' % (output)
        output = '%s- get server tag:uc:ocp<br>' % (output)
        output = '%s- get server view:tag<br>' % (output)
        output = '%s<br>Find more examples and documentation <a href="%s">here</a>' % (output, self.link)
        return output

    def doc(self, activity):
        files = []
        files.append(
            os.path.join(
                os.path.join(
                    os.path.join(
                        file_helper.get_main_dir(),
                        'doc'
                    ),
                    'bot'
                ),
                'GetServer.md'
            )
        )
        self.my_webex_api_handler.create_message(
            room_id=activity['target']['globalId'],
            parent_id=activity['id'],
            files=files
        )

    def parse_command(self, message):
        options = {}
        options['success'] = True
        options['error'] = ''
        options['include_rack'] = True
        options['include_blade'] = True
        options['name'] = []
        options['serial'] = []
        options['model'] = []
        options['ip'] = []
        options['tag'] = []
        options['alarm_filter'] = 'any'
        options['mode_filter'] = 'any'
        options['locator_filter'] = 'any'
        options['power_filter'] = 'any'
        options['cpu_filter'] = []
        options['gpu_filter'] = []
        options['memory_filter'] = []
        options['pci_filter'] = []
        options['sc_filter'] = []
        options['pd_filter'] = []
        options['vd_filter'] = []
        options['mac_filter'] = []
        options['fan_filter'] = []
        options['psu_filter'] = []

        words = message.split(' ')
        requested_view = []
        if 'all' not in words:
            for word in words:
                if len(word) == 0:
                    continue

                if len(word.split(':')) == 1:
                    options['success'] = False
                    options['error'] = '<b>Error</b><br><br>Command options must follow type:value syntax.<br><br>Check <a href="%s">documentation</a>' % (self.link)
                    return options

                key = word.split(':')[0]
                value = ':'.join(word.split(':')[1:])

                if key == 'type':
                    if value not in ['rack', 'blade']:
                        options['success'] = False
                        options['error'] = '<b>Error</b><br><br>Unsupported type value %s.<br><br>Check <a href="%s">documentation</a>' % (value, self.link)
                        return options

                    if value == 'rack':
                        options['include_blade'] = False

                    if value == 'blade':
                        options['include_rack'] = False

                if key == 'serial':
                    options['serial'].append('*%s*' % (value))

                if key == 'model':
                    options['model'].append('*%s*' % (value))

                if key == 'tag':
                    options['tag'].append(value)

                if key == 'name':
                    options['name'].append('*%s*' % (value))

                if key == 'ip':
                    if not ip_helper.is_valid_ipv4_cidr(value) and not ip_helper.is_valid_ipv4_address(value):
                        options['success'] = False
                        options['error'] = '<b>Error</b><br><br>Provide value ip or subnet value.<br><br>Check <a href="%s">documentation</a>' % (self.link)
                        return options

                    options['ip'].append(value)

                if key == 'led':
                    if value.lower() not in ['on', 'off']:
                        options['success'] = False
                        options['error'] = '<b>Error</b><br><br>Unsupported led value %s.<br><br>Check <a href="%s">documentation</a>' % (value, self.link)
                        return options

                    options['locator_filter'] = value.lower()

                if key == 'power':
                    if value.lower() not in ['on', 'off']:
                        options['success'] = False
                        options['error'] = '<b>Error</b><br><br>Unsupported power value %s.<br><br>Check <a href="%s">documentation</a>' % (value, self.link)
                        return options

                    options['power_filter'] = value.lower()

                if key == 'mode':
                    if value.lower() not in ['imm', 'ucsm']:
                        options['success'] = False
                        options['error'] = '<b>Error</b><br><br>Unsupported mode value %s.<br><br>Check <a href="%s">documentation</a>' % (value, self.link)
                        return options

                    options['mode_filter'] = value.lower()

                if key == 'alarm':
                    if value.lower() not in ['info', 'warn', 'crit']:
                        options['success'] = False
                        options['error'] = '<b>Error</b><br><br>Unsupported alarm value %s.<br><br>Check <a href="%s">documentation</a>' % (value, self.link)
                        return options

                    options['alarm_filter'] = value.lower()

                if key.startswith('cpu-'):
                    options['cpu_filter'].append(word[4:])

                if key.startswith('gpu-'):
                    options['gpu_filter'].append(word[4:])

                if key.startswith('mem-'):
                    options['memory_filter'].append(word[4:])

                if key.startswith('pci-'):
                    options['pci_filter'].append(word[4:])

                if key.startswith('sc-'):
                    options['sc_filter'].append(word[3:])

                if key.startswith('pd-'):
                    options['pd_filter'].append(word[3:])

                if key.startswith('vd-'):
                    options['vd_filter'].append(word[3:])

                if key == 'mac':
                    options['mac_filter'].append(value)

                if key.startswith('fan-'):
                    options['fan_filter'].append(word[4:])

                if key.startswith('psu-'):
                    options['psu_filter'].append(word[4:])

                if key == 'view':
                    requested_view.append(value)

        if len(requested_view) == 0:
            options['view'] = ['list']
        else:
            options['view'] = validations.validate_view(
                requested_view,
                'list|adv|alarm|board|boot|connector|contract|cpu|green|fan|fw|gpu|hcl|hw|state|kvm|lic|mem|net|pci|power|profile|psu|sc|pd|vd|storage|thermal|sw|tpm|tag',
                'list',
                [
                    'hw:board,cpu,fan,gpu,mem,pci,net,psu,storage,tpm',
                    'green:power,thermal',
                    'sw:fw,boot,kvm',
                    'state:adv,alarm,connector,contract,hcl,lic,profile,workflow'
                ]
            )

        if options['view'] is None:
            options['success'] = False
            options['error'] = '<b>Error</b><br><br>Unsupported view.<br><br>Check <a href="%s">documentation</a>' % (self.link)
            return options

        settings = {}
        settings['alarm'] = 'alarm' in options['view'] or options['alarm_filter'] != 'any'
        settings['advisory'] = 'adv' in options['view']
        settings['board'] = 'board' in options['view'] or 'tpm' in options['view']
        settings['boot'] = 'boot' in options['view']
        settings['connector'] = 'connector' in options['view'] or 'list' in options['view']
        settings['contract'] = 'contract' in options['view']
        settings['cpu'] = 'cpu' in options['view'] or len(options['cpu_filter']) > 0
        settings['fan'] = 'fan' in options['view'] or 'fanm' in options['view'] or len(options['fan_filter'])
        settings['fw'] = 'fw' in options['view']
        settings['gpu'] = 'gpu' in options['view'] or len(options['gpu_filter'])
        settings['hcl'] = 'hcl' in options['view']
        settings['inventory'] = 'inventory' in options['view']
        settings['locator'] = 'list' in options['view'] or options['locator_filter'] != 'any'
        settings['memory'] = 'mem' in options['view'] or len(options['memory_filter']) > 0
        settings['net'] = 'net' in options['view'] or len(options['mac_filter']) > 0
        settings['pci'] = 'pci' in options['view'] or 'gpu' in options['view'] or len(options['pci_filter']) > 0 or len(options['gpu_filter']) > 0
        settings['power'] = 'power' in options['view']
        settings['profile'] = 'profile' in options['view']
        settings['psu'] = 'psu' in options['view'] or len(options['psu_filter']) > 0
        settings['state'] = 'list' in options['view'] or options['locator_filter'] != 'any' or options['power_filter'] != 'any'
        settings['storage'] = 'storage' in options['view'] or 'sc' in options['view'] or 'pd' in options['view'] or 'vd' in options['view'] or len(options['sc_filter']) > 0 or len(options['pd_filter']) > 0 or len(options['vd_filter']) > 0
        settings['thermal'] = 'thermal' in options['view']
        settings['tpm'] = 'tpm' in options['view']

        options['settings'] = settings

        match_rules = {}
        match_rules['locator'] = options['locator_filter']
        match_rules['power'] = options['power_filter']
        match_rules['alarms'] = options['alarm_filter']
        match_rules['ucsm'] = False
        if options['mode_filter'] == 'ucsm':
            match_rules['ucsm'] = True
        match_rules['imm'] = False
        if options['mode_filter'] == 'imm':
            match_rules['imm'] = True
        match_rules['disconnected'] = False

        match_rules['cpu'] = intersight_validations.bot_cpu_filter(options['cpu_filter'])
        if match_rules['cpu'] is None:
            options['success'] = False
            options['error'] = 'unsupported cpu filtering options'
            return options

        match_rules['gpu'] = intersight_validations.bot_gpu_filter(options['gpu_filter'])
        if match_rules['gpu'] is None:
            options['success'] = False
            options['error'] = 'unsupported gpu filtering options'
            return options

        match_rules['memory'] = intersight_validations.bot_memory_filter(options['memory_filter'])
        if match_rules['memory'] is None:
            options['success'] = False
            options['error'] = 'unsupported memory filtering options'
            return options

        match_rules['pci'] = intersight_validations.bot_pci_filter(options['pci_filter'])
        if match_rules['pci'] is None:
            options['success'] = False
            options['error'] = 'unsupported pci filtering options'
            return options

        match_rules['mac'] = options['mac_filter']

        match_rules['sc'] = intersight_validations.bot_sc_filter(options['sc_filter'])
        if match_rules['sc'] is None:
            options['success'] = False
            options['error'] = 'unsupported sc filtering options'
            return options

        match_rules['pd'] = intersight_validations.bot_pd_filter(options['pd_filter'])
        if match_rules['pd'] is None:
            options['success'] = False
            options['error'] = 'unsupported pd filtering options'
            return options

        match_rules['vd'] = intersight_validations.bot_vd_filter(options['vd_filter'])
        if match_rules['vd'] is None:
            options['success'] = False
            options['error'] = 'unsupported vd filtering options'
            return options

        match_rules['fan'] = intersight_validations.bot_fan_filter(options['fan_filter'])
        if match_rules['fan'] is None:
            options['success'] = False
            options['error'] = 'unsupported fan filtering options'
            return options

        match_rules['psu'] = intersight_validations.bot_psu_filter(options['psu_filter'])
        if match_rules['psu'] is None:
            options['success'] = False
            options['error'] = 'unsupported psu filtering options'
            return options

        match_rules['ancestor'] = []

        options['match_rules'] = match_rules

        return options

    def add_fabric_info(self, servers_info, command_run_id):
        for server_info in servers_info:
            for cimc_info in server_info['CimcInfo']:
                cimc_info['FabricDomain'] = ''
                cimc_info['FabricDevice'] = ''
                cimc_info['FabricSource'] = ''
                cimc_info['FabricInterface'] = ''

            for ext_eth_info in server_info['ExtEthInfo']:
                ext_eth_info['FabricDomain'] = ''
                ext_eth_info['FabricDevice'] = ''
                ext_eth_info['FabricSource'] = ''
                ext_eth_info['FabricInterface'] = ''

            for host_eth_info in server_info['HostEthInfo']:
                host_eth_info['FabricDomain'] = ''
                host_eth_info['FabricDevice'] = ''
                host_eth_info['FabricSource'] = ''
                host_eth_info['FabricInterface'] = ''

        servers_info = self.add_aci_info(
            servers_info,
            command_run_id
        )

        servers_info = self.add_nexus_info(
            servers_info,
            command_run_id
        )

        return servers_info

    def add_aci_info(self, servers_info, command_run_id):
        aci_settings_handler = aci_settings.ApicSettings(log_id=command_run_id)
        controllers = aci_settings_handler.get_apic_controllers()
        if controllers is not None:
            for controller in controllers:
                if not aci_settings_handler.is_cache_enabled(controller['name']):
                    continue

                apic_handler = apic.Apic(
                    controller['ip'],
                    controller['port'],
                    controller['username'],
                    controller['password'],
                    apic_name=controller['name'],
                    log_id=command_run_id,
                    debug=False,
                    no_cache=False
                )

                apic_nodes = apic_handler.get_nodes()
                if apic_nodes is None:
                    continue

                for apic_node in apic_nodes:
                    if apic_node['role'] == 'controller':
                        continue

                    proto_info = apic_handler.get_protocol_lacp(
                        apic_node['podId'],
                        apic_node['id'],
                        instance_info=True,
                        interface_info=True,
                        interface_filter=[]
                    )
                    if proto_info is None:
                        continue

                    if 'interfaces' in proto_info and proto_info['interfaces'] is not None:
                        for interface_info in proto_info['interfaces']:
                            for lacp_interface_info in interface_info['lacp']:
                                for server_info in servers_info:
                                    for ext_eth_info in server_info['ExtEthInfo']:
                                        if filter_helper.match_mac(lacp_interface_info['adjacency']['sysId'], ext_eth_info['MacAddress']):
                                            ext_eth_info['FabricDomain'] = 'ACI'
                                            ext_eth_info['FabricDevice'] = apic_node['name']
                                            ext_eth_info['FabricSource'] = 'LACP'
                                            ext_eth_info['FabricInterface'] = interface_info['id']

                                    for host_eth_info in server_info['HostEthInfo']:
                                        if filter_helper.match_mac(lacp_interface_info['adjacency']['sysId'], host_eth_info['MacAddress']):
                                            host_eth_info['FabricDomain'] = 'ACI'
                                            host_eth_info['FabricDevice'] = apic_node['name']
                                            host_eth_info['FabricSource'] = 'LACP'
                                            host_eth_info['FabricInterface'] = interface_info['id']

                                    for cimc_info in server_info['CimcInfo']:
                                        if filter_helper.match_mac(lacp_interface_info['adjacency']['sysId'], cimc_info['MacAddress']):
                                            cimc_info['FabricDomain'] = 'ACI'
                                            cimc_info['FabricDevice'] = apic_node['name']
                                            cimc_info['FabricSource'] = 'LACP'
                                            cimc_info['FabricInterface'] = interface_info['id']

                    proto_info = apic_handler.get_protocol_lldp(
                        apic_node['podId'],
                        apic_node['id'],
                        adjacency_filter=[],
                        instance_info=True,
                        stats_info=True,
                        adjacency_info=True
                    )
                    if proto_info is None:
                        continue

                    if 'adjacency' in proto_info and proto_info['adjacency'] is not None:
                        for adjacency_info in proto_info['adjacency']:
                            for server_info in servers_info:
                                for ext_eth_info in server_info['ExtEthInfo']:
                                    if filter_helper.match_mac(adjacency_info['mac'], ext_eth_info['MacAddress']):
                                        ext_eth_info['FabricDomain'] = 'ACI'
                                        ext_eth_info['FabricDevice'] = apic_node['name']
                                        ext_eth_info['FabricSource'] = 'LLDP'
                                        ext_eth_info['FabricInterface'] = adjacency_info['interface_id']

                                for host_eth_info in server_info['HostEthInfo']:
                                    if filter_helper.match_mac(adjacency_info['mac'], host_eth_info['MacAddress']):
                                        host_eth_info['FabricDomain'] = 'ACI'
                                        host_eth_info['FabricDevice'] = apic_node['name']
                                        host_eth_info['FabricSource'] = 'LLDP'
                                        host_eth_info['FabricInterface'] = adjacency_info['interface_id']

                                for cimc_info in server_info['HostEthInfo']:
                                    if filter_helper.match_mac(adjacency_info['mac'], cimc_info['MacAddress']):
                                        cimc_info['FabricDomain'] = 'ACI'
                                        cimc_info['FabricDevice'] = apic_node['name']
                                        cimc_info['FabricSource'] = 'LLDP'
                                        cimc_info['FabricInterface'] = adjacency_info['interface_id']

        return servers_info

    def add_nexus_info(self, servers_info, command_run_id):
        nexus_settings_handler = nexus_settings.NexusSettings(log_id=command_run_id)
        if nexus_settings_handler.is_nexus_cache_enabled():
            devices = nexus_settings_handler.get_nexus_devices()
            if devices is not None:
                for device in devices:
                    device_handler = nxapi.NxApi(
                        device['ip'],
                        device['username'],
                        device['password'],
                        name=device['name'],
                        log_id=command_run_id,
                        debug=False,
                        cache_enabled=True
                    )

                    device_mac_addresses = device_handler.get_macs()
                    if device_mac_addresses is not None:
                        for device_mac_address in device_mac_addresses:
                            for server_info in servers_info:
                                for ext_eth_info in server_info['ExtEthInfo']:
                                    if filter_helper.match_mac(ext_eth_info['MacAddress'], device_mac_address['mac_addr']):
                                        ext_eth_info['FabricDomain'] = 'Nexus'
                                        ext_eth_info['FabricDevice'] = device_mac_address['nexus_name']
                                        ext_eth_info['FabricSource'] = 'MAC'
                                        ext_eth_info['FabricInterface'] = device_mac_address['port']

                                for host_eth_info in server_info['HostEthInfo']:
                                    if filter_helper.match_mac(host_eth_info['MacAddress'], device_mac_address['mac_addr']):
                                        host_eth_info['FabricDomain'] = 'Nexus'
                                        host_eth_info['FabricDevice'] = device_mac_address['nexus_name']
                                        host_eth_info['FabricSource'] = 'MAC'
                                        host_eth_info['FabricInterface'] = device_mac_address['port']

                                for cimc_info in server_info['CimcInfo']:
                                    if filter_helper.match_mac(cimc_info['MacAddress'], device_mac_address['mac_addr']):
                                        cimc_info['FabricDomain'] = 'Nexus'
                                        cimc_info['FabricDevice'] = device_mac_address['nexus_name']
                                        cimc_info['FabricSource'] = 'MAC'
                                        cimc_info['FabricInterface'] = device_mac_address['port']

                    device_neighbors = device_handler.get_lacps()
                    if device_neighbors is not None:
                        for device_neighbor in device_neighbors:
                            for port_info in device_neighbor['port']:
                                if ip_helper.is_mac_address(port_info['partner_mac']):
                                    for server_info in servers_info:
                                        for ext_eth_info in server_info['ExtEthInfo']:
                                            if filter_helper.match_mac(ext_eth_info['MacAddress'], port_info['partner_mac']):
                                                ext_eth_info['FabricDomain'] = 'Nexus'
                                                ext_eth_info['FabricDevice'] = device_neighbor['nexus_name']
                                                ext_eth_info['FabricSource'] = 'LACP'
                                                ext_eth_info['FabricInterface'] = port_info['port']

                                        for host_eth_info in server_info['HostEthInfo']:
                                            if filter_helper.match_mac(host_eth_info['MacAddress'], port_info['partner_mac']):
                                                host_eth_info['FabricDomain'] = 'Nexus'
                                                host_eth_info['FabricDevice'] = device_neighbor['nexus_name']
                                                host_eth_info['FabricSource'] = 'LACP'
                                                host_eth_info['FabricInterface'] = port_info['port']

                                        for cimc_info in server_info['CimcInfo']:
                                            if filter_helper.match_mac(cimc_info['MacAddress'], port_info['partner_mac']):
                                                cimc_info['FabricDomain'] = 'Nexus'
                                                cimc_info['FabricDevice'] = device_neighbor['nexus_name']
                                                cimc_info['FabricSource'] = 'LACP'
                                                cimc_info['FabricInterface'] = port_info['port']

                    device_neighbors = device_handler.get_lldps()
                    if device_neighbors is not None:
                        for device_neighbor in device_neighbors:
                            if ip_helper.is_mac_address(device_neighbor['port_id']):
                                for server_info in servers_info:
                                    for ext_eth_info in server_info['ExtEthInfo']:
                                        if filter_helper.match_mac(ext_eth_info['MacAddress'], device_neighbor['port_id']):
                                            ext_eth_info['FabricDomain'] = 'Nexus'
                                            ext_eth_info['FabricDevice'] = device_neighbor['nexus_name']
                                            ext_eth_info['FabricSource'] = 'LLDP'
                                            ext_eth_info['FabricInterface'] = device_neighbor['l_port_id']

                                    for host_eth_info in server_info['HostEthInfo']:
                                        if filter_helper.match_mac(host_eth_info['MacAddress'], port_info['partner_mac']):
                                            host_eth_info['FabricDomain'] = 'Nexus'
                                            host_eth_info['FabricDevice'] = device_neighbor['nexus_name']
                                            host_eth_info['FabricSource'] = 'LLDP'
                                            host_eth_info['FabricInterface'] = device_neighbor['l_port_id']

                                    for cimc_info in server_info['CimcInfo']:
                                        if filter_helper.match_mac(cimc_info['MacAddress'], port_info['partner_mac']):
                                            cimc_info['FabricDomain'] = 'Nexus'
                                            cimc_info['FabricDevice'] = device_neighbor['nexus_name']
                                            cimc_info['FabricSource'] = 'LLDP'
                                            cimc_info['FabricInterface'] = device_neighbor['l_port_id']

        return servers_info

    def execute(self, message, attachment_actions, activity):
        command_run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(command_run_id)
        self.log_handler.initialize()

        logger.info('Command execution: get server [%s]', command_run_id[4:])

        try:
            message = message.strip().lower()
            if len(message) == 0 or message in ['help', '?', '--help']:
                if activity['verb'] == 'cardAction':
                    return self.help()

                self.my_webex_api_handler.create_message(
                    room_id=activity['target']['globalId'],
                    markdown=self.help(),
                    parent_id=activity['id']
                )
                self.doc(activity)
                return

            options = self.parse_command(message)
            if not options['success']:
                logger.info(options['error'])
                self.my_webex_api_handler.create_message(
                    room_id=activity['target']['globalId'],
                    markdown=options['error'],
                    parent_id=activity['id']
                )
                self.doc(activity)
                return

            self.my_webex_api_handler.create_message(
                room_id=activity['target']['globalId'],
                text='Processing request...',
                parent_id=activity['id']
            )

        except BaseException:
            output = 'Command execution failed [%s]\n\n%s' % (command_run_id, traceback.format_exc())
            return output

        logger.info(json.dumps(options, indent=4))

        try:
            start_time = int(time.time() * 1000)

            # Hardcode
            cache_ttl = 1800
            mo_cache_ttl = 180

            compute_handler = compute.Compute('isctl', log_id=command_run_id)
            compute_output_handler = bot_output.ComputeBotOutput(log_id=command_run_id)

            mo_match_rules = compute_handler.get_mo_match_rules(
                ip_filter=options['ip'],
                name_filter=options['name'],
                serial_filter=options['serial'],
                model_filter=options['model'],
                tag_filter=options['tag']
            )
            logger.info(mo_match_rules)

            rack_expand = []
            blade_expand = []

            if options['settings']['pci']:
                rack_expand.append('PciDevices')
                blade_expand.append('PciDevices')
            if options['settings']['psu']:
                rack_expand.append('Psus')
            if options['settings']['fan']:
                rack_expand.append('Fanmodules')
            if options['settings']['locator']:
                rack_expand.append('LocatorLed')
                blade_expand.append('LocatorLed')
            if options['settings']['state']:
                rack_expand.append('RegisteredDevice')
                blade_expand.append('RegisteredDevice')

            # Bot is supported with crontab task that runs every minute
            # cache_ttl of 180 should be good compromise between accuracy and efficiency

            servers_mo = compute_handler.get_mo(
                match_rules=mo_match_rules,
                include_rack=options['include_rack'],
                rack_expand=rack_expand,
                include_blade=options['include_blade'],
                blade_expand=blade_expand,
                cache_ttl=mo_cache_ttl
            )
            logger.info('Selected %s servers', len(servers_mo))

            compute_handler.set_cache(
                servers_mo,
                options['settings'],
                cache_ttl,
                ctx=None
            )

            logger.info('Cache populated')

            servers_info = compute_handler.get_info(
                servers_mo,
                options['settings'],
                options['match_rules'],
                cache_ttl,
                prepare_cache=False,
                bar_handler=None
            )

            logger.info('Servers info collected')

            output = ''
            output_file = ''
            output_html = ''
            output_view_html = {}
            output_csvs = []

            if servers_info is None or len(servers_info) == 0:
                self.my_webex_api_handler.create_message(
                    room_id=activity['target']['globalId'],
                    text='No servers found',
                    parent_id=activity['id']
                )
                return

            view_output, view_output_html = compute_output_handler.print_summary_table(servers_info, title=True)
            output_csvs.append('Server')
            if 'list' in options['view']:
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if view_output_html is not None:
                output_view_html['list'] = view_output_html

            # hw

            if 'board' in options['view'] or options['settings']['board']:
                view_output, view_output_html = compute_output_handler.print_board(servers_info, title=True)
                output_csvs.append('Board')
                output_file = output_file + view_output
                if 'board' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['board']:
                    if view_output_html is not None:
                        output_view_html['board'] = view_output_html

            if 'cpu' in options['view'] or options['settings']['cpu']:
                view_output, view_output_html = compute_output_handler.print_cpu(servers_info, title=True)
                output_csvs.append('CPU')
                output_file = output_file + view_output
                if 'cpu' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['cpu']:
                    if view_output_html is not None:
                        output_view_html['cpu'] = view_output_html

            if 'gpu' in options['view'] or options['settings']['gpu']:
                view_output, view_output_html = compute_output_handler.print_gpu(servers_info, title=True)
                output_csvs.append('GPU')
                output_file = output_file + view_output
                if 'gpu' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['gpu']:
                    if view_output_html is not None:
                        output_view_html['gpu'] = view_output_html

            if 'mem' in options['view'] or options['settings']['memory']:
                view_output, view_output_html = compute_output_handler.print_memory(servers_info, title=True)
                output_csvs.append('Memory')
                output_file = output_file + view_output
                if 'mem' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['memory']:
                    if view_output_html is not None:
                        output_view_html['mem'] = view_output_html

            if 'storage' in options['view'] or 'sc' in options['view'] or options['settings']['storage']:
                view_output, view_output_html = compute_output_handler.print_storage_controllers(servers_info, title=True)
                output_csvs.append('StorageController')
                output_file = output_file + view_output
                output_file = output_file + view_output
                if 'storage' in options['view'] or 'sc' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['storage']:
                    if view_output_html is not None:
                        output_view_html['storage controller'] = view_output_html

            if 'storage' in options['view'] or 'pd' in options['view'] or options['settings']['storage']:
                state_view_output, state_view_output_html = compute_output_handler.print_physical_disks_state(servers_info, title=True)
                output_csvs.append('PhysicalDisk')
                output_file = output_file + state_view_output
                inv_view_output, inv_view_output_html = compute_output_handler.print_physical_disks_inventory(servers_info, title=True)

                if 'storage' in options['view'] or 'pd' in options['view']:
                    output = output + state_view_output
                    if state_view_output_html is not None:
                        output_html = output_html + state_view_output_html

                    output = output + inv_view_output
                    if inv_view_output_html is not None:
                        output_html = output_html + inv_view_output_html

                if options['settings']['storage']:
                    output_view_html['physical disk'] = ''
                    if state_view_output_html is not None:
                        output_view_html['physical disk'] = output_view_html['physical disk'] + state_view_output_html

                    if inv_view_output_html is not None:
                        output_view_html['physical disk'] = output_view_html['physical disk'] + inv_view_output_html

            if 'storage' in options['view'] or 'vd' in options['view'] or options['settings']['storage']:
                view_output, view_output_html = compute_output_handler.print_virtual_drives(servers_info, title=True)
                output_csvs.append('VirtualDrive')
                output_file = output_file + view_output
                if 'storage' in options['view'] or 'vd' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['storage']:
                    if view_output_html is not None:
                        output_view_html['virtual drive'] = view_output_html

            if 'net' in options['view'] or options['settings']['net']:
                servers_info = self.add_fabric_info(servers_info, command_run_id)

                cimc_view_output, cimc_view_output_html = compute_output_handler.print_cimc(servers_info, title=True)
                output_csvs.append('IMC')
                output_file = output_file + cimc_view_output
                adapter_view_output, adapter_view_output_html = compute_output_handler.print_adapters(servers_info, title=True)
                output_csvs.append('NetworkAdapter')
                output_file = output_file + adapter_view_output
                ext_view_output, ext_view_output_html = compute_output_handler.print_ext_eth(servers_info, title=True)
                output_csvs.append('MLOM')
                output_file = output_file + ext_view_output
                eth_view_output, eth_view_output_html = compute_output_handler.print_host_eth(servers_info, title=True)
                output_csvs.append('HostEthernet')
                output_file = output_file + eth_view_output
                fc_view_output, fc_view_output_html = compute_output_handler.print_host_fc(servers_info, title=True)
                output_csvs.append('HostFc')
                output_file = output_file + fc_view_output

                if 'net' in options['view']:
                    output = output + cimc_view_output
                    if cimc_view_output_html is not None:
                        output_html = output_html + cimc_view_output_html

                    output = output + adapter_view_output
                    if adapter_view_output_html is not None:
                        output_html = output_html + adapter_view_output_html

                    output = output + ext_view_output
                    if ext_view_output_html is not None:
                        output_html = output_html + ext_view_output_html

                    output = output + eth_view_output
                    if eth_view_output_html is not None:
                        output_html = output_html + eth_view_output_html

                    output = output + fc_view_output
                    if fc_view_output_html is not None:
                        output_html = output_html + fc_view_output_html

                if options['settings']['net']:
                    if cimc_view_output_html is not None:
                        output_view_html['cimc'] = cimc_view_output_html

                    if adapter_view_output_html is not None:
                        output_view_html['net adapter'] = adapter_view_output_html

                    if ext_view_output_html is not None:
                        output_view_html['mlom'] = ext_view_output_html

                    if eth_view_output_html is not None:
                        output_view_html['host eth'] = eth_view_output_html

                    if fc_view_output_html is not None:
                        output_view_html['host fc'] = fc_view_output_html

            if 'pci' in options['view'] or options['settings']['pci']:
                view_output, view_output_html = compute_output_handler.print_pci(servers_info, title=True)
                output_csvs.append('PCI')
                output_file = output_file + view_output
                if 'pci' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['pci']:
                    if view_output_html is not None:
                        output_view_html['pci'] = view_output_html

            if 'fan' in options['view'] or options['settings']['fan']:
                view_output, view_output_html = compute_output_handler.print_fan(servers_info, title=True)
                output_csvs.append('FanModule')
                output_csvs.append('Fan')
                output_file = output_file + view_output
                if 'fan' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['fan']:
                    if view_output_html is not None:
                        output_view_html['fan'] = view_output_html

            if 'psu' in options['view'] or options['settings']['psu']:
                view_output, view_output_html = compute_output_handler.print_psu(servers_info, title=True)
                output_csvs.append('PSU')
                output_file = output_file + view_output
                if 'psu' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['psu']:
                    if view_output_html is not None:
                        output_view_html['psu'] = view_output_html

            if 'tpm' in options['view'] or options['settings']['tpm']:
                view_output, view_output_html = compute_output_handler.print_tpm(servers_info, title=True)
                output_csvs.append('TPM')
                output_file = output_file + view_output
                if 'tpm' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if options['settings']['tpm']:
                    if view_output_html is not None:
                        output_view_html['tpm'] = view_output_html

            # sw:fw,boot,kvm

            if 'fw' in options['view']:
                view_output, view_output_html = compute_output_handler.print_firmware(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'boot' in options['view']:
                view_output, view_output_html = compute_output_handler.print_boot(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'kvm' in options['view']:
                view_output, view_output_html = compute_output_handler.print_kvm(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            # state:adv,alarm,connector,contract,hcl,lic,profile,workflow

            if 'adv' in options['view']:
                view_output, view_output_html = compute_output_handler.print_advisory(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'alarm' in options['view']:
                view_output, view_output_html = compute_output_handler.print_server_alarm(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'connector' in options['view']:
                view_output, view_output_html = compute_output_handler.print_connector(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'contract' in options['view']:
                view_output, view_output_html = compute_output_handler.print_contract(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'hcl' in options['view']:
                view_output, view_output_html = compute_output_handler.print_hcl_summary(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                view_output, view_output_html = compute_output_handler.print_hcl_hardware(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                view_output, view_output_html = compute_output_handler.print_hcl_software(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                view_output, view_output_html = compute_output_handler.print_hcl_component(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'lic' in options['view']:
                view_output, view_output_html = compute_output_handler.print_license(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'profile' in options['view']:
                view_output, view_output_html = compute_output_handler.print_profile(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if 'tag' in options['view']:
                view_output, view_output_html = compute_output_handler.print_tag(servers_info, title=True)
                output = output + view_output
                output_file = output_file + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            logger.info('Commands executed')

            execution_time = int(time.time() * 1000) - start_time

            files = None
            filename = self.log_handler.bot_output(output_file, log_id=command_run_id)
            if filename is not None:
                files = [filename]

            files_xls = None
            filename = self.log_handler.bot_xls(output_csvs, log_id=command_run_id)
            if filename is not None:
                files_xls = [filename]

            output = compute_output_handler.my_output.sanitize_bot_output(
                output,
                output_html,
                self.url,
                execution_time=execution_time
            )

            if len(output_html) > 0:
                self.log_handler.output_html(
                    compute_output_handler.my_output.wrap_bot_html_output(
                        output_view_html['list'],
                        command='get server %s' % (message),
                        view=output_view_html,
                        exclude_view=['list']
                    )
                )

            for key in output_view_html:
                self.log_handler.output_html(
                    compute_output_handler.my_output.wrap_bot_html_output(
                        output_view_html[key],
                        command='get server %s [view:%s]' % (message, key),
                        view=output_view_html,
                        exclude_view=[key]
                    ),
                    filename='%s.html' % (key)
                )

            logger.info('Output prepared')

        except BaseException:
            files = None
            output = 'Command execution failed [%s]\n\n%s' % (command_run_id, traceback.format_exc())

        self.my_webex_api_handler.create_message(
            room_id=activity['target']['globalId'],
            markdown=output,
            parent_id=activity['id']
        )

        self.my_webex_api_handler.create_message(
            room_id=activity['target']['globalId'],
            parent_id=activity['id'],
            files=files
        )

        self.my_webex_api_handler.create_message(
            room_id=activity['target']['globalId'],
            parent_id=activity['id'],
            files=files_xls
        )

        return
