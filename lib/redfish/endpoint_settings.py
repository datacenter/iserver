import os
import time
import json

from progress.bar import Bar

from lib import ip_helper
from lib import log_helper

from lib.settings_helper import Settings
from lib.redfish import endpoint


class RedfishEndpointSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        self.redfish_settings_filename = os.path.join(
            self.settings_dir,
            'redfish'
        )

        self.endpoint_directory = os.path.join(
            self.settings_dir,
            'endpoint'
        )

        if not self.initialize_endpoint_directory():
            raise ValueError('Endpoints initialization failed')

    def initialize_endpoint_directory(self):
        try:
            if not os.path.isdir(self.endpoint_directory):
                os.makedirs(self.endpoint_directory)

            for filename in os.listdir(self.endpoint_directory):
                filename_path = os.path.join(
                    self.endpoint_directory,
                    filename
                )
                if os.path.isdir(filename_path):
                    continue

                try:
                    with open(filename_path, 'r', encoding='utf-8') as file_handler:
                        settings = json.loads(file_handler.read())

                except BaseException:
                    self.log.error(
                        'initialize_endpoint_directory',
                        'File read failed: %s' % (filename_path)
                    )
                    continue

                os.remove(filename_path)
                os.makedirs(filename_path, exist_ok=True)

                settings_filename = os.path.join(
                    filename_path,
                    'settings'
                )

                try:
                    with open(settings_filename, 'w', encoding='utf-8') as file_handler:
                        file_handler.write(
                            json.dumps(
                                settings,
                                indent=4
                            )
                        )

                except BaseException:
                    self.log.error(
                        'initialize_endpoint_directory',
                        'File write failed: %s' % (settings_filename)
                    )

        except BaseException:
            return False
        return True

    def get_endpoint_ids(self):
        return os.listdir(self.endpoint_directory)

    def get_endpoint_settings(self, endpoint_id, filename='settings'):
        endpoint_directory = os.path.join(
            self.endpoint_directory,
            endpoint_id
        )
        endpoint_filename = os.path.join(
            endpoint_directory,
            filename
        )
        if not os.path.isfile(endpoint_filename):
            return None

        try:
            with open(endpoint_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error(
                'get_endpoint_settings',
                'File read failed: %s' % (endpoint_filename)
            )
            return None

        return settings

    def set_endpoint_settings(self, endpoint_id, settings, filename='settings'):
        endpoint_directory = os.path.join(
            self.endpoint_directory,
            endpoint_id
        )
        if not os.path.isdir(endpoint_directory):
            os.makedirs(endpoint_directory, exist_ok=True)

        endpoint_filename = os.path.join(
            endpoint_directory,
            filename
        )

        try:
            with open(endpoint_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(
                    json.dumps(
                        settings,
                        indent=4
                    )
                )

        except BaseException:
            self.log.error(
                'set_endpoint_settings',
                'File write failed: %s' % (endpoint_filename)
            )
            return False

        return True

    def get_redfish_endpoint_id(self, identity):
        if 'SerialNumber' not in identity:
            self.log.error(
                'get_redfish_endpoint_id',
                'No serial in endpoint identity: %s' % (identity)
            )
            return None

        return identity['SerialNumber']

    def is_redfish_endpoint(self, endpoint_id):
        if self.get_redfish_endpoint_settings(endpoint_id) is None:
            return False
        return True

    def get_redfish_endpoint_settings(self, endpoint_id):
        endpoint_settings = self.get_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return None

        if 'redfish' in endpoint_settings:
            return endpoint_settings['redfish']

        return None

    def set_redfish_endpoint_access(self, access, endpoint_id):
        endpoint_settings = {}
        endpoint_settings['endpoint_id'] = endpoint_id
        endpoint_settings['redfish'] = {}
        endpoint_settings['redfish']['endpoint_id'] = endpoint_id
        endpoint_settings['redfish']['endpoint'] = access

        if not self.set_endpoint_settings(endpoint_id, endpoint_settings):
            self.log.error(
                'set_redfish_endpoint_access',
                'Failed: %s' % (endpoint_id)
            )
            return False

        return True

    def set_redfish_endpoint_settings(self, redfish_endpoint_configuration, redfish_endpoint_identity):
        endpoint_id = self.get_redfish_endpoint_id(
            redfish_endpoint_identity
        )

        if endpoint_id is None:
            self.log.error(
                'set_redfish_endpoint_settings',
                'Failed on no endpoint id: %s' % (redfish_endpoint_identity)
            )
            return False

        endpoint_settings = {}
        endpoint_settings['endpoint_id'] = endpoint_id
        endpoint_settings['redfish'] = {}
        endpoint_settings['redfish']['endpoint_id'] = endpoint_id
        endpoint_settings['redfish']['endpoint'] = redfish_endpoint_configuration

        if not self.set_endpoint_settings(endpoint_id, endpoint_settings):
            self.log.error(
                'set_redfish_endpoint_settings',
                'Failed: %s' % (endpoint_id)
            )
            return False

        data = {}
        data['timestamp'] = int(time.time())
        data['data'] = redfish_endpoint_identity
        if not self.set_endpoint_settings(endpoint_id, data, filename='identity'):
            self.log.error(
                'set_redfish_endpoint_settings',
                'Identity failed: %s' % (endpoint_id)
            )
            return False

        return True

    def match_redfish_endpoint(self, redfish_endpoint, endpoint_type, endpoint_ip, serial_number):
        if endpoint_type is not None and len(endpoint_type) > 0 and endpoint_type != 'any':
            if redfish_endpoint['endpoint']['type'] != endpoint_type:
                return False

        if endpoint_ip is not None and len(endpoint_ip) > 0:
            if ip_helper.is_valid_ipv4_address(endpoint_ip):
                if redfish_endpoint['endpoint']['ip'] != endpoint_ip:
                    return False

            if ip_helper.is_valid_ipv4_cidr(endpoint_ip):
                if not ip_helper.is_ipv4_in_cidr(redfish_endpoint['endpoint']['ip'], endpoint_ip):
                    return False

        if serial_number is not None and len(serial_number) > 0:
            if redfish_endpoint['identity']['SerialNumber'] != serial_number:
                return False

        return True

    def get_redfish_endpoints_settings(self, endpoint_type=None, endpoint_ip=None, serial_number=None, include=[]):
        endpoint_ids = self.get_endpoint_ids()

        endpoints = []
        for endpoint_id in endpoint_ids:
            redfish_endpoint = self.get_redfish_endpoint_settings(endpoint_id)
            if redfish_endpoint is None:
                continue

            match = self.match_redfish_endpoint(
                redfish_endpoint,
                endpoint_type,
                endpoint_ip,
                serial_number
            )

            if not match:
                continue

            for key in include:
                data = self.get_endpoint_settings(
                    endpoint_id,
                    filename=key
                )
                if data is not None:
                    redfish_endpoint[key] = data['data']

            endpoints.append(
                redfish_endpoint
            )

        endpoints = sorted(
            endpoints,
            key=lambda i: i['identity']['HostName'].lower()
        )

        return endpoints

    def get_endpoint_id_with_ip(self, endpoint_ip):
        endpoint_ids = self.get_endpoint_ids()

        for endpoint_id in endpoint_ids:
            redfish_settings = self.get_redfish_endpoint_settings(endpoint_id)
            if redfish_settings is None:
                continue

            if redfish_settings['endpoint']['ip'] == endpoint_ip:
                return endpoint_id

        return None

    def get_servers_redfish_settings(self, servers_mo, verify=False, bar_enabled=False):
        redfish_endpoints_settings = self.get_redfish_endpoints_settings()
        if redfish_endpoints_settings is None:
            return None

        for server_mo in servers_mo:
            server_mo['redfish_capable'] = True
            if server_mo['ManagementMode'] == 'UCSM':
                server_mo['redfish_capable'] = False
            server_mo['redfish_enabled'] = False
            server_mo['redfish_endpoint'] = None
            server_mo['redfish_verified'] = ''

            if server_mo['redfish_capable']:
                for redfish_endpoint in redfish_endpoints_settings:
                    if server_mo['Serial'] == redfish_endpoint['identity']['SerialNumber']:
                        server_mo['redfish_enabled'] = True
                        server_mo['redfish_verified'] = False
                        server_mo['redfish_endpoint_id'] = redfish_endpoint['endpoint_id']
                        for key in redfish_endpoint['endpoint']:
                            server_mo['redfish_endpoint_%s' % (key)] = redfish_endpoint['endpoint'][key]

        if verify:
            if bar_enabled:
                bar_handler = Bar('Progress', max=len(servers_mo))
                bar_handler.goto(0)

            for server_mo in servers_mo:
                if server_mo['redfish_enabled']:
                    server_mo['redfish_verified'] = self.verify_redfish_endpoint_authentication(
                        server_mo['redfish_endpoint_id']
                    )
                if bar_enabled:
                    bar_handler.next()

            if bar_enabled:
                bar_handler.finish()

        return servers_mo

    def delete_redfish_endpoint_settings(self, endpoint_id):
        endpoint_settings = self.get_endpoint_settings(endpoint_id)
        if 'redfish' in endpoint_settings:
            del endpoint_settings['redfish']

        return self.set_endpoint_settings(endpoint_id, endpoint_settings)

    def verify_redfish_endpoint_authentication(self, endpoint_id):
        endpoint_settings = self.get_redfish_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return False

        redfish_handler = endpoint.RedfishEndpoint(
            endpoint_settings['endpoint']['type'],
            endpoint_settings['endpoint']['ip'],
            endpoint_settings['endpoint']['port'],
            endpoint_settings['endpoint']['username'],
            endpoint_settings['endpoint']['password'],
            log_id=self.log_id
        )

        if not redfish_handler.is_connected():
            return False

        return True
