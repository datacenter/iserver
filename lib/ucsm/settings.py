import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class UcsmSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id
        self.my_output = None

        self.ucsm_settings_filename = os.path.join(
            self.settings_dir,
            'ucsm'
        )

        if not self.initialize_ucsm_settings():
            raise ValueError('Ucsm settings initialization failed')

    def get_ucsm_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Managers'] = []
        return settings

    def initialize_ucsm_settings(self):
        if not os.path.isfile(self.ucsm_settings_filename):
            settings = self.get_ucsm_default_settings()
            if not self.set_ucsm_settings(settings):
                return False
        return True

    def get_ucsm_settings(self):
        if not os.path.isfile(self.ucsm_settings_filename):
            return None

        try:
            with open(self.ucsm_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_ucsm_settings', traceback.format_exc())
            return None

        return settings

    def set_ucsm_settings(self, settings):
        try:
            with open(self.ucsm_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_ucsm_settings', traceback.format_exc())
            return False

        return True

    def get_ucsm_managers(self):
        settings = self.get_ucsm_settings()
        if settings is None:
            return None

        return settings['Managers']

    def get_ucsm_manager(self, ucsm_name):
        managers = self.get_ucsm_managers()
        if managers is None:
            return None

        for manager in managers:
            if manager['name'] == ucsm_name:
                return manager

        return None

    def set_ucsm_managers(self, managers):
        settings = self.get_ucsm_settings()
        if settings is None:
            return False

        settings['Managers'] = managers
        return self.set_ucsm_settings(settings)

    def set_ucsm_manager(self, ucsm_name, ucsm_ip, ucsm_username, ucsm_password):
        managers = self.get_ucsm_managers()
        if managers is None:
            return False

        new_managers = []
        for manager in managers:
            if manager['name'] != ucsm_name:
                new_managers.append(manager)

        new_manager = {}
        new_manager['name'] = ucsm_name
        new_manager['ip'] = ucsm_ip
        new_manager['username'] = ucsm_username
        new_manager['password'] = ucsm_password
        new_managers.append(new_manager)

        return self.set_ucsm_managers(new_managers)

    def delete_ucsm_manager(self, ucsm_name):
        managers = self.get_ucsm_managers()
        if managers is None:
            return False

        new_managers = []
        for manager in managers:
            if manager['name'] != ucsm_name:
                new_managers.append(manager)

        return self.set_ucsm_managers(new_managers)

    def print_ucsm_managers(self, managers, show_password=True):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(
                log_id=self.log_id,
                verbose=False,
                debug=False
            )

        managers = sorted(managers, key=lambda i: i['name'])
        if not show_password:
            for manager in managers:
                manager['password'] = '******'

        order = [
            'name',
            'ip',
            'username',
            'password'
        ]

        headers = [
            'Name',
            'IP',
            'Username',
            'Password'
        ]

        self.my_output.my_table(
            managers,
            order=order,
            headers=headers,
            table=True
        )
