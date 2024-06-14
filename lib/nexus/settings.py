import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class NexusSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.nexus_settings_filename = os.path.join(
            self.settings_dir,
            'nexus'
        )

        self.nexus_cache_directory = os.path.join(
            self.settings_dir,
            'nx-device'
        )

        if not self.initialize_nexus_settings():
            raise ValueError('Nexus settings initialization failed')

    def get_nexus_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Cache'] = {}
        settings['Cache']['Enabled'] = False
        settings['Cache']['Ttl'] = 180
        settings['Cache']['Command'] = {}
        settings['Devices'] = []
        settings['Defaults'] = {}
        settings['Defaults']['Device'] = None
        return settings

    def initialize_nexus_settings(self):
        if not os.path.isfile(self.nexus_settings_filename):
            settings = self.get_nexus_default_settings()
            if not self.set_nexus_settings(settings):
                return False

        if not os.path.isdir(self.nexus_cache_directory):
            os.makedirs(self.nexus_cache_directory, exist_ok=True)

        return True

    def get_nexus_cache_base_directory(self):
        return self.nexus_cache_directory

    def is_nexus_cache_enabled(self):
        settings = self.get_nexus_cache_settings()
        return settings['Enabled']

    def get_nexus_cache_settings(self):
        settings = self.get_nexus_settings()
        return settings['Cache']

    def get_nexus_settings(self):
        if not os.path.isfile(self.nexus_settings_filename):
            self.log.error(
                'get_nexus_settings',
                'File not found: %s' % (
                    self.nexus_settings_filename
                )
            )
            return None

        try:
            with open(self.nexus_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_nexus_settings', traceback.format_exc())
            return None

        return settings

    def set_nexus_settings(self, settings):
        try:
            with open(self.nexus_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_nexus_settings', traceback.format_exc())
            return False

        return True

    def get_nexus_devices(self):
        settings = self.get_nexus_settings()
        if settings is None:
            return None

        devices = settings['Devices']
        for device in devices:
            device['cache_enabled'] = settings['Cache']['Enabled']
            device['cache_ttl'] = settings['Cache']['Ttl']

        return devices

    def get_nexus_domain_devices(self, domain_name):
        settings = self.get_nexus_settings()
        if settings is None:
            return None

        domain_devices = []
        for device in settings['Devices']:
            if device['domain'] == domain_name:
                domain_devices.append(
                    device
                )

        return domain_devices

    def get_nexus_device(self, nexus_name):
        devices = self.get_nexus_devices()
        if devices is None:
            return None

        for device in devices:
            if device['name'] == nexus_name:
                return device

        return None

    def set_nexus_devices(self, devices):
        settings = self.get_nexus_settings()
        if settings is None:
            return False

        settings['Devices'] = devices
        return self.set_nexus_settings(settings)

    def set_nexus_device(self, nexus_name, nexus_ip, nexus_username, nexus_password, domain=''):
        devices = self.get_nexus_devices()
        if devices is None:
            return False

        new_devices = []
        for device in devices:
            if device['name'] != nexus_name:
                new_devices.append(device)

        new_device = {}
        new_device['name'] = nexus_name
        new_device['ip'] = nexus_ip
        new_device['username'] = nexus_username
        new_device['password'] = nexus_password
        new_device['domain'] = domain
        new_devices.append(new_device)

        return self.set_nexus_devices(new_devices)

    def delete_nexus_device(self, nexus_name):
        devices = self.get_nexus_devices()
        if devices is None:
            return False

        new_devices = []
        for device in devices:
            if device['name'] != nexus_name:
                new_devices.append(device)

        return self.set_nexus_devices(new_devices)

    def get_default_nexus_device(self):
        settings = self.get_nexus_settings()
        if settings is None:
            return None

        try:
            default_device_name = settings['Defaults']['Device']
        except BaseException:
            default_device_name = None

        return default_device_name

    def set_default_nexus_device(self, name):
        settings = self.get_nexus_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Device'] = name
        return self.set_nexus_settings(settings)

    def get_nexus_device_names(self):
        devices = self.get_nexus_devices()
        if devices is None:
            return None

        names = []
        for device in devices:
            names.append(
                device['name']
            )

        return names

    def print_nexus_devices(self, devices, show_password=True):
        devices = sorted(devices, key=lambda i: i['name'])
        if not show_password:
            for device in devices:
                device['password'] = '******'

        order = [
            'name',
            'ip',
            'username',
            'password',
            'domain'
        ]

        headers = [
            'Name',
            'IP',
            'Username',
            'Password',
            'Domain'
        ]

        self.my_output.my_table(
            devices,
            order=order,
            headers=headers,
            table=True
        )
