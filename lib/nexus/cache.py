import time
import os
import json
from datetime import datetime

from lib.nexus import settings


class Cache():
    def __init__(self, cache_enabled):
        settings_handler = settings.NexusSettings()
        self.cache_directory = os.path.join(
            settings_handler.get_nexus_cache_base_directory(),
            self.nexus_ip
        )

        self.cache_enabled = cache_enabled
        if not self.cache_enabled:
            self.cache_settings = {}
            self.cache_settings['Enabled'] = False
            self.cache_settings['Ttl'] = 180
            self.cache_settings['Command'] = {}

        if self.cache_enabled:
            self.cache_settings = settings_handler.get_nexus_cache_settings()

        self.cache_commands = [
            'show lacp neighbor',
            'show lldp neighbors',
            'show mac address-table',
            'show version'
        ]

    def is_cache_enabled(self):
        if not self.cache_enabled:
            return False

        if self.cache_settings is None:
            return False

        return self.cache_settings['Enabled']

    def get_command_cache_settings(self, command):
        command_cache_settings = {}
        command_cache_settings['enabled'] = self.cache_settings['Enabled']
        command_cache_settings['ttl'] = self.cache_settings['Ttl']
        if not command_cache_settings['enabled']:
            return command_cache_settings

        if command in self.cache_settings['Command']:
            command_cache_settings['enabled'] = self.cache_settings['Command'][command]['enabled']
            command_cache_settings['ttl'] = self.cache_settings['Command'][command]['ttl']

        return command_cache_settings

    def get_command_cache_filename(self, command):
        filename = os.path.join(
            self.cache_directory,
            command.replace(' ', '_').replace('-', '_')
        )
        return filename

    def get_command_cache_timestamp(self, command):
        filename = self.get_command_cache_filename(command)
        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

        except BaseException:
            return None

        return content['timestamp']

    def get_cache_commands_timestamp(self):
        now = int(time.time())
        all_valid = True
        entries = []
        for command in self.cache_commands:
            command_cache_settings = self.get_command_cache_settings(command)
            ttl = command_cache_settings['ttl']

            entry = {}
            entry['command'] = command
            entry['timestamp'] = self.get_command_cache_timestamp(command)

            if entry['timestamp'] is None:
                entry['time'] = None
                entry['valid'] = False
                all_valid = False

            if entry['timestamp'] is not None:
                entry['time'] = datetime.fromtimestamp(entry['timestamp'])
                if now - entry['timestamp'] > ttl:
                    entry['valid'] = False
                    all_valid = False
                else:
                    entry['valid'] = True

            entries.append(entry)

        response = {}
        response['valid'] = all_valid
        response['command'] = entries

        return response

    def get_command_cache(self, command):
        command_cache_settings = self.get_command_cache_settings(command)
        if not command_cache_settings['enabled']:
            return None

        filename = self.get_command_cache_filename(command)
        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

        except BaseException:
            return None

        if content['timestamp'] - int(time.time()) > command_cache_settings['ttl']:
            return None

        return content['cache']

    def set_command_cache(self, command, cache):
        filename = self.get_command_cache_filename(command)
        if filename is None:
            return False

        if not os.path.isdir(self.cache_directory):
            os.makedirs(self.cache_directory, exist_ok=True)

        content = {}
        content['command'] = command
        content['timestamp'] = int(time.time())
        content['cache'] = cache

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(content, indent=4))

        except BaseException:
            self.log.error(
                'nexus.set_command_cache',
                'Set cache failed: %s %s' % (
                    self.nexus_ip,
                    command
                )
            )
            return False

        return True
