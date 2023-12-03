import os
import json
from datetime import timedelta
import shutil
import uuid
import traceback

from lib import log_helper
from lib.settings_helper import Settings


class LinuxSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

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
        settings['defaults'] = None
        settings['servers'] = []
        return settings

    def get_linux_default_cache_settings(self):
        settings = {}
        settings['enabled'] = True
        settings['ttl'] = 600
        settings['ttlT'] = '{}'.format(str(timedelta(seconds=settings['ttl'])))
        settings['object'] = []
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
            default_server_name = settings['defaults']
        except BaseException:
            default_server_name = None

        return default_server_name

    def set_default_server(self, name):
        settings = self.get_linux_settings()
        if settings is None:
            return False

        if 'defaults' not in settings:
            settings['defaults'] = None

        settings['defaults'] = name
        return self.set_linux_settings(settings)

    def get_linux_servers(self):
        settings = self.get_linux_settings()
        if settings is None:
            return None

        servers = settings['servers']
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

        settings['servers'] = servers
        return self.set_linux_settings(settings)

    def set_linux_server(self, linux_name, linux_ip, username, password=None, key_filename=None):
        servers = self.get_linux_servers()
        if servers is None:
            return False

        new_servers = []
        previous = None
        for server in servers:
            if server['name'] == linux_name:
                previous = server
            if server['name'] != linux_name:
                new_servers.append(server)

        new_server = {}
        new_server['name'] = linux_name
        new_server['address'] = linux_ip
        new_server['username'] = username
        new_server['password'] = password
        new_server['key'] = key_filename
        if previous is None:
            new_server['id'] = str(uuid.uuid4())
            new_server['cache'] = self.get_linux_default_cache_settings()
            server_directory = os.path.join(
                self.linux_settings_dir,
                new_server['id']
            )
            if not os.path.isdir(server_directory):
                os.makedirs(server_directory, exist_ok=True)
            new_server['cache']['directory'] = server_directory

        if previous is not None:
            new_server['id'] = previous['id']
            new_server['cache'] = previous['cache']

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
        server_id = None
        for server in servers:
            if server['name'] == linux_name:
                server_id = server['id']
            if server['name'] != linux_name:
                new_servers.append(server)

        if server_id is not None:
            server_directory = os.path.join(
                self.linux_settings_dir,
                server_id
            )
            if os.path.isdir(server_directory):
                shutil.rmtree(server_directory)

        return self.set_linux_servers(new_servers)
