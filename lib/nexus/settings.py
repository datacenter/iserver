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
            'nx-switch'
        )

        if not self.initialize_nexus_settings():
            raise ValueError('Nexus settings initialization failed')

    def get_nexus_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Cache'] = {}
        settings['Cache']['Enabled'] = False
        settings['Cache']['Command'] = {}
        settings['Switches'] = []
        settings['Defaults'] = {}
        settings['Defaults']['Switch'] = None
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

    def get_nexus_cache_settings(self):
        settings = self.get_nexus_settings()
        return settings['Cache']

    def get_nexus_settings(self):
        if not os.path.isfile(self.nexus_settings_filename):
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

    def get_nexus_switches(self):
        settings = self.get_nexus_settings()
        if settings is None:
            return None

        return settings['Switches']

    def get_nexus_switch(self, nexus_name):
        switches = self.get_nexus_switches()
        if switches is None:
            return None

        for switch in switches:
            if switch['name'] == nexus_name:
                return switch

        return None

    def set_nexus_switches(self, switches):
        settings = self.get_nexus_settings()
        if settings is None:
            return False

        settings['Switches'] = switches
        return self.set_nexus_settings(settings)

    def set_nexus_switch(self, nexus_name, nexus_ip, nexus_username, nexus_password, domain=''):
        switches = self.get_nexus_switches()
        if switches is None:
            return False

        new_switches = []
        for switch in switches:
            if switch['name'] != nexus_name:
                new_switches.append(switch)

        new_switch = {}
        new_switch['name'] = nexus_name
        new_switch['ip'] = nexus_ip
        new_switch['username'] = nexus_username
        new_switch['password'] = nexus_password
        new_switch['domain'] = domain
        new_switches.append(new_switch)

        return self.set_nexus_switches(new_switches)

    def delete_nexus_switch(self, nexus_name):
        switches = self.get_nexus_switches()
        if switches is None:
            return False

        new_switches = []
        for switch in switches:
            if switch['name'] != nexus_name:
                new_switches.append(switch)

        return self.set_nexus_switches(new_switches)

    def get_default_nexus_switch(self):
        settings = self.get_nexus_settings()
        if settings is None:
            return None

        try:
            default_switch_name = settings['Defaults']['Switch']
        except BaseException:
            default_switch_name = None

        return default_switch_name

    def set_default_nexus_switch(self, name):
        settings = self.get_nexus_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Switch'] = name
        return self.set_nexus_settings(settings)

    def get_nexus_switch_names(self):
        switches = self.get_nexus_switches()
        if switches is None:
            return None

        names = []
        for switch in switches:
            names.append(
                switch['name']
            )

        return names

    def print_nexus_switches(self, switches, show_password=True):
        switches = sorted(switches, key=lambda i: i['name'])
        if not show_password:
            for switch in switches:
                switch['password'] = '******'

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
            switches,
            order=order,
            headers=headers,
            table=True
        )
