import time
import os
import json

from lib.nexus import settings


class Cache():
    def __init__(self, cache_enabled):
        self.cache_enabled = cache_enabled
        if self.cache_enabled:
            settings_handler = settings.NexusSettings()
            self.cache_settings = settings_handler.get_nexus_cache_settings()
            self.cache_directory = os.path.join(
                settings_handler.get_nexus_cache_base_directory(),
                self.nexus_ip
            )

    def is_cache_enabled(self):
        if not self.cache_enabled:
            return False

        if self.cache_settings is None:
            return False

        return self.cache_settings['Enabled']

    def is_command_cache_enabled(self, command):
        if not self.is_cache_enabled():
            return False

        if command not in self.cache_settings['Command']:
            return False

        return self.cache_settings['Command'][command]['enabled']

    def get_command_cache_filename(self, command):
        if not self.is_command_cache_enabled(command):
            return None

        filename = os.path.join(
            self.cache_directory,
            self.cache_settings['Command'][command]['filename']
        )

        return filename

    def get_command_cache(self, command):
        filename = self.get_command_cache_filename(command)
        if filename is None:
            return None

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

        except BaseException:
            return None

        if self.cache_settings['Command'][command]['ttl'] is not None:
            if content['timestamp'] - int(time.time()) > self.cache_settings['Command'][command]['ttl']:
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
