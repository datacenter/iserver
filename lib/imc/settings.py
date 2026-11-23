import os
import json
import traceback

from lib import file_helper
from lib import ip_helper
from lib import log_helper
from lib.settings_helper import Settings


class ImcEndpointSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        self.endpoint_directory = os.path.join(
            self.settings_dir,
            'imc-endpoint'
        )

        self.imc_settings_filename = os.path.join(
            self.settings_dir,
            'imc'
        )

        if not self.initialize_imc_settings():
            raise ValueError('IMC endpoints initialization failed')

    def get_default_imc_endpoint_settings(self):
        imc_settings = {}
        imc_settings['CacheEnabled'] = True
        imc_settings['CacheTtl'] = 600
        return imc_settings

    def initialize_imc_settings(self):
        try:
            if not os.path.isdir(self.endpoint_directory):
                os.makedirs(self.endpoint_directory)

            if not os.path.isfile(self.imc_settings_filename):
                success = file_helper.set_file_json(
                    self.imc_settings_filename,
                    self.get_default_imc_endpoint_settings()
                )
                if not success:
                    self.log.error(
                        'initialize_imc_settings',
                        'Failed to create file: %s' % (self.imc_settings_filename)
                    )
                    return False

        except BaseException:
            self.log.error(
                'initialize_imc_settings',
                traceback.format_exc()
            )
            return False

        return True

    def get_imc_settings(self):
        return file_helper.get_file_json(self.imc_settings_filename)

    def get_endpoint_ids(self):
        return os.listdir(self.endpoint_directory)

    def get_endpoint_directory(self, endpoint_id):
        return os.path.join(
            self.endpoint_directory,
            endpoint_id

        )

    def is_endpoint(self, endpoint_id):
        if self.get_endpoint_settings(endpoint_id) is None:
            return False
        return True

    def get_endpoint_settings(self, endpoint_id):
        endpoint_directory = os.path.join(
            self.endpoint_directory,
            endpoint_id
        )

        if not os.path.isdir(endpoint_directory):
            return None

        endpoint_settings = {}
        endpoint_settings['id'] = endpoint_id
        for key in ['cli', 'api']:
            endpoint_filename = os.path.join(
                endpoint_directory,
                key
            )
            if not os.path.isfile(endpoint_filename):
                endpoint_settings[key] = None
                settings = {}
                settings['enabled'] = False
            else:
                try:
                    with open(endpoint_filename, 'r', encoding='utf-8') as file_handler:
                        settings = json.loads(file_handler.read())

                    settings['enabled'] = True

                except BaseException:
                    self.log.error(
                        'get_endpoint_settings',
                        'File read failed: %s' % (endpoint_filename)
                    )
                    settings = {}
                    settings['enabled'] = False

            endpoint_settings[key] = settings

        return endpoint_settings

    def get_endpoints(self, ip_address=None, ip_addresses=None, ip_subnet=None):
        endpoint_ids = self.get_endpoint_ids()

        endpoints = []
        if endpoint_ids is not None:
            for endpoint_id in endpoint_ids:
                if ip_address is not None and ip_address != endpoint_id:
                    continue

                if ip_addresses is not None and endpoint_id not in ip_addresses:
                    continue

                if ip_subnet is not None and not ip_helper.is_ipv4_in_cidr(endpoint_id, ip_subnet):
                    continue

                endpoint_settings = self.get_endpoint_settings(endpoint_id)
                if endpoint_settings is not None:
                    endpoints.append(
                        endpoint_settings
                    )

        return endpoints

    def get_cli_endpoint(self, ip_address):
        endpoint_settings = self.get_endpoint_settings(ip_address)
        if endpoint_settings is None:
            return None

        if endpoint_settings['cli']['enabled']:
            return endpoint_settings['cli']

        return None

    def get_cli_endpoints(self, ip_address=None, ip_addresses=None, ip_subnet=None):
        all_endpoints = self.get_endpoints(
            ip_address=ip_address,
            ip_addresses=ip_addresses,
            ip_subnet=ip_subnet
        )
        if all_endpoints is None:
            return None

        cli_endpoints = []
        for endpoint in all_endpoints:
            if endpoint['cli']['enabled']:
                cli_endpoints.append(
                    endpoint['cli']
                )

        return cli_endpoints

    def set_endpoint_settings(self, endpoint_id, filename, settings):
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

    def set_imc_ssh_access(self, ip_address, username, password, port=22):
        endpoint_settings = {}
        endpoint_settings['ip'] = ip_address
        endpoint_settings['port'] = port
        endpoint_settings['username'] = username
        endpoint_settings['password'] = password

        if not self.set_endpoint_settings(ip_address, 'cli', endpoint_settings):
            self.log.error(
                'set_imc_ssh_access',
                'Failed: %s' % (ip_address)
            )
            return False

        return True
