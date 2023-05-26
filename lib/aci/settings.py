import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class ApicSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.apic_settings_filename = os.path.join(
            self.settings_dir,
            'apic'
        )

        self.apic_cache_directory = os.path.join(
            self.settings_dir,
            'aci-switch'
        )

        if not self.initialize_apic_settings():
            raise ValueError('APIC settings initialization failed')

    def get_apic_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Cache'] = {}
        settings['Cache']['Enabled'] = False
        settings['Cache']['Object'] = {}
        settings['Defaults'] = {}
        settings['Defaults']['Controller'] = None
        settings['Defaults']['Node'] = None
        settings['Controllers'] = []
        return settings

    def initialize_apic_settings(self):
        if not os.path.isfile(self.apic_settings_filename):
            settings = self.get_apic_default_settings()
            if not self.set_apic_settings(settings):
                return False

        if not os.path.isdir(self.apic_cache_directory):
            os.makedirs(self.apic_cache_directory, exist_ok=True)

        return True

    def get_apic_cache_base_directory(self):
        return self.apic_cache_directory

    def get_apic_cache_settings(self):
        settings = self.get_apic_settings()
        return settings['Cache']

    def get_apic_settings(self):
        if not os.path.isfile(self.apic_settings_filename):
            return None

        try:
            with open(self.apic_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_apic_settings', traceback.format_exc())
            return None

        return settings

    def set_apic_settings(self, settings):
        try:
            with open(self.apic_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_apic_settings', traceback.format_exc())
            return False

        return True

    def get_default_node(self, controller_name):
        settings = self.get_apic_settings()
        if settings is None:
            return None

        try:
            default_node_name = settings['Defaults']['Node'][controller_name]
        except BaseException:
            default_node_name = None

        return default_node_name

    def set_default_node(self, controller_name, node_name):
        settings = self.get_apic_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        if 'Node' not in settings['Defaults'] or settings['Defaults']['Node'] is None:
            settings['Defaults']['Node'] = {}

        settings['Defaults']['Node'][controller_name] = node_name
        return self.set_apic_settings(settings)

    def get_default_controller(self):
        settings = self.get_apic_settings()
        if settings is None:
            return None

        try:
            default_controller_name = settings['Defaults']['Controller']
        except BaseException:
            default_controller_name = None

        return default_controller_name

    def set_default_controller(self, name):
        settings = self.get_apic_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Controller'] = name
        return self.set_apic_settings(settings)

    def get_apic_controller_names(self):
        controllers = self.get_apic_controllers()
        if controllers is None:
            return None

        names = []
        for controller in controllers:
            names.append(
                controller['name']
            )

        return names

    def get_apic_controllers(self):
        settings = self.get_apic_settings()
        if settings is None:
            return None

        return settings['Controllers']

    def get_apic_domain_controllers(self, domain_name):
        settings = self.get_apic_settings()
        if settings is None:
            return None

        domain_controllers = []
        for controller in settings['Controllers']:
            if controller['domain'] == domain_name:
                domain_controllers.append(
                    controller
                )

        return domain_controllers

    def get_apic_controller(self, apic_name):
        controllers = self.get_apic_controllers()
        if controllers is None:
            return None

        for controller in controllers:
            if controller['name'] == apic_name:
                return controller

        return None

    def set_apic_controllers(self, controllers):
        settings = self.get_apic_settings()
        if settings is None:
            return False

        settings['Controllers'] = controllers
        return self.set_apic_settings(settings)

    def set_apic_controller(self, apic_name, apic_ip, apic_username, apic_password, domain=''):
        controllers = self.get_apic_controllers()
        if controllers is None:
            return False

        new_controllers = []
        for controller in controllers:
            if controller['name'] != apic_name:
                new_controllers.append(controller)

        new_controller = {}
        new_controller['name'] = apic_name
        new_controller['ip'] = apic_ip
        new_controller['username'] = apic_username
        new_controller['password'] = apic_password
        new_controller['domain'] = domain
        new_controllers.append(new_controller)

        return self.set_apic_controllers(new_controllers)

    def delete_apic_controller(self, apic_name):
        controllers = self.get_apic_controllers()
        if controllers is None:
            return False

        new_controllers = []
        for controller in controllers:
            if controller['name'] != apic_name:
                new_controllers.append(controller)

        return self.set_apic_controllers(new_controllers)

    def print_apic_controllers(self, controllers, show_password=True):
        controllers = sorted(controllers, key=lambda i: i['name'])
        if not show_password:
            for controller in controllers:
                controller['password'] = '******'

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
            controllers,
            order=order,
            headers=headers,
            table=True
        )
