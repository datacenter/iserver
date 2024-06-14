import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class VcSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.vc_settings_filename = os.path.join(
            self.settings_dir,
            'vc'
        )

        if not self.initialize_vc_settings():
            raise ValueError('vSphere Client settings initialization failed')

    def get_vc_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Defaults'] = {}
        settings['Defaults']['Instance'] = None
        settings['Instances'] = []
        return settings

    def initialize_vc_settings(self):
        if not os.path.isfile(self.vc_settings_filename):
            settings = self.get_vc_default_settings()
            if not self.set_vc_settings(settings):
                return False
        return True

    def get_vc_settings(self):
        if not os.path.isfile(self.vc_settings_filename):
            return None

        try:
            with open(self.vc_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_vc_settings', traceback.format_exc())
            return None

        return settings

    def set_vc_settings(self, settings):
        try:
            with open(self.vc_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_vc_settings', traceback.format_exc())
            return False

        return True

    def get_default_instance(self):
        settings = self.get_vc_settings()
        if settings is None:
            return None

        try:
            default_instance_name = settings['Defaults']['Instance']
        except BaseException:
            default_instance_name = None

        return default_instance_name

    def set_default_instance(self, name):
        settings = self.get_vc_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Instance'] = name
        return self.set_vc_settings(settings)

    def get_vc_instances(self):
        settings = self.get_vc_settings()
        if settings is None:
            return None

        return settings['Instances']

    def get_vc_instance(self, vc_name):
        instances = self.get_vc_instances()
        if instances is None:
            return None

        for instance in instances:
            if instance['name'] == vc_name:
                return instance

        return None

    def set_vc_instances(self, instances):
        settings = self.get_vc_settings()
        if settings is None:
            return False

        settings['Instances'] = instances
        return self.set_vc_settings(settings)

    def set_vc_instance(self, vc_name, vc_ip, vc_port, vc_username, vc_password):
        instances = self.get_vc_instances()
        if instances is None:
            return False

        new_instances = []
        for instance in instances:
            if instance['name'] != vc_name:
                new_instances.append(instance)

        new_instance = {}
        new_instance['name'] = vc_name
        new_instance['ip'] = vc_ip
        new_instance['port'] = vc_port
        new_instance['username'] = vc_username
        new_instance['password'] = vc_password
        new_instances.append(new_instance)

        return self.set_vc_instances(new_instances)

    def delete_vc_instance(self, vc_name):
        instances = self.get_vc_instances()
        if instances is None:
            return False

        new_instances = []
        for instance in instances:
            if instance['name'] != vc_name:
                new_instances.append(instance)

        return self.set_vc_instances(new_instances)

    def print_vc_instances(self, instances, show_password=True):
        instances = sorted(instances, key=lambda i: i['name'])
        if not show_password:
            for instance in instances:
                instance['password'] = '******'

        order = [
            'name',
            'ip',
            'port',
            'username',
            'password'
        ]

        headers = [
            'Name',
            'IP',
            'Port',
            'Username',
            'Password'
        ]

        self.my_output.my_table(
            instances,
            order=order,
            headers=headers,
            table=True
        )
