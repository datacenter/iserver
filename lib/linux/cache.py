import time
import os
import json

from lib.linux import settings


class Cache():
    def __init__(self, server_name, no_cache=False):
        if server_name is None:
            self.cache_enabled = False
            return

        settings_handler = settings.LinuxSettings()
        server_settings = settings_handler.get_linux_server(server_name)
        if server_settings is None:
            self.cache_enabled = False
            return

        self.cache_server_name = server_name
        self.cache_enabled = server_settings['cache']['enabled']
        self.cache_directory = server_settings['cache']['directory']
        self.cache_ttl = server_settings['cache']['ttl']

        if no_cache:
            self.cache_enabled = False

    def is_cache_enabled(self):
        return self.cache_enabled

    def get_cmd_cache_filename(self, cmd_name):
        filename = os.path.join(
            self.cache_directory,
            cmd_name
        )
        return filename

    def get_cmd_cache(self, cmd_name, cmd_selector=None):
        if not self.is_cache_enabled():
            return None

        filename = self.get_cmd_cache_filename(cmd_name)
        if filename is None:
            return None

        if cmd_selector is not None:
            filename = '%s.%s' % (filename, cmd_selector)

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

        except BaseException:
            return None

        age = int(time.time()) - content['timestamp']
        if age > self.cache_ttl:
            return None

        return content['cache']

    def set_cmd_cache(self, cmd_name, cache, cmd_selector=None):
        filename = self.get_cmd_cache_filename(cmd_name)
        if filename is None:
            return False

        if not os.path.isdir(self.cache_directory):
            os.makedirs(self.cache_directory, exist_ok=True)

        content = {}
        content['cmd'] = cmd_name
        content['selector'] = cmd_selector
        content['timestamp'] = int(time.time())
        content['cache'] = cache

        if cmd_selector is not None:
            filename = '%s.%s' % (filename, cmd_selector)

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(content, indent=4))

        except BaseException:
            self.log.error(
                'set_cmd_cache.set_object_cache',
                'Set cache failed: %s %s %s %s' % (
                    self.cache_server_name,
                    cmd_name,
                    cmd_selector,
                    filename
                )
            )
            return False

        return True
