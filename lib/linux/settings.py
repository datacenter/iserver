import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class LinuxSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = None

        self.linux_settings_dir = os.path.join(
            self.settings_dir,
            'linux'
        )
        self.linux_settings_filename = os.path.join(
            self.linux_settings_dir,
            'settings'
        )

        if not self.initialize_linux_settings():
            raise ValueError('K8s settings initialization failed')

    def get_linux_default_settings(self):
        settings = {}
        settings['Default'] = None
        settings['Servers'] = []
        return settings

    def initialize_linux_settings(self):
        if not os.path.isdir(self.linux_settings_dir):
            os.makedirs(self.linux_settings_dir, exist_ok=True)

        if not os.path.isfile(self.linux_settings_filename):
            settings = self.get_linux_default_settings()
            if not self.set_linux_settings(settings):
                return False

        return True

    def get_linux_settings(self):
        if not os.path.isfile(self.linux_settings_filename):
            return None

        try:
            with open(self.linux_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_linux_settings', traceback.format_exc())
            return None

        return settings

    def set_linux_settings(self, settings):
        try:
            with open(self.linux_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_linux_settings', traceback.format_exc())
            return False

        return True

    def get_default_server(self):
        settings = self.get_linux_settings()
        if settings is None:
            return None

        try:
            default_server_name = settings['Default']
        except BaseException:
            default_server_name = None

        return default_server_name

    def set_default_server(self, name):
        settings = self.get_linux_settings()
        if settings is None:
            return False

        if 'Default' not in settings:
            settings['Default'] = None

        settings['Default'] = name
        return self.set_linux_settings(settings)

    def get_linux_servers(self):
        settings = self.get_linux_settings()
        if settings is None:
            return None

        servers = settings['Servers']
        servers = sorted(
            servers,
            key=lambda i: i['name']
        )

        return servers

    def get_linux_server(self, linux_name, strict_match=True):
        servers = self.get_linux_servers()
        if servers is None:
            return None

        candidates = []
        for server in servers:
            if server['name'] == linux_name:
                return server

            if not strict_match:
                if linux_name.lower() in server['name'].lower():
                    candidates.append(server)

        if not strict_match and len(candidates) == 1:
            return candidates[0]

        return None

    def set_linux_servers(self, servers):
        settings = self.get_linux_settings()
        if settings is None:
            return False

        settings['Servers'] = servers
        return self.set_linux_settings(settings)

    def set_linux_server(self, linux_name, linux_ip, username, password=None, key_filename=None):
        servers = self.get_linux_servers()
        if servers is None:
            return False

        new_servers = []
        for server in servers:
            if server['name'] != linux_name:
                new_servers.append(server)

        new_server = {}
        new_server['name'] = linux_name
        new_server['address'] = linux_ip
        new_server['username'] = username
        new_server['password'] = password
        new_server['key'] = key_filename
        new_servers.append(new_server)

        return self.set_linux_servers(new_servers)

    def delete_linux_server(self, linux_name):
        servers = self.get_linux_servers()
        if servers is None:
            return False

        default_server = self.get_default_server()
        if default_server is not None and default_server == linux_name:
            self.set_default_server(None)

        new_servers = []
        for server in servers:
            if server['name'] != linux_name:
                new_servers.append(server)

        return self.set_linux_servers(new_servers)

    def print_linux_servers(self, servers, show_password=True):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(
                log_id=self.log_id,
                verbose=False,
                debug=False
            )

        servers = sorted(servers, key=lambda i: i['name'])
        if not show_password:
            for server in servers:
                if server['password'] is not None:
                    server['password'] = '******'

        for server in servers:
            if server['password'] is None:
                server['password'] = '--'

            if server['key'] is None:
                server['key'] = '--'

        order = [
            'name',
            'address',
            'username',
            'password',
            'key'
        ]

        headers = [
            'Name',
            'IP',
            'Username',
            'Password',
            'Key'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True
        )
