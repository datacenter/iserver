import os
import time
import json
import traceback

from lib.psirt import settings


class PsirtCache():
    def __init__(self):
        self.settings_handler = settings.PsirtSettings(log_id=self.log_id)
        psirt_settings = self.settings_handler.get_psirt_settings()

        self.psirt_cache_enabled = psirt_settings['cache']
        self.psirt_cache_directory = psirt_settings['directory']
        self.psirt_cache_ttl = psirt_settings['ttl']

    def get_psirt_cache_file(self, name):
        filename = os.path.join(
            self.psirt_cache_directory,
            name
        )
        if not os.path.isfile(filename):
            self.log.debug('get_psirt_cache_file', 'cache not found: %s' % (filename))
            return None

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_psirt_cache_file', traceback.format_exc())
            return None

        if int(time.time()) - content['timestamp'] > self.psirt_cache_ttl:
            self.log.debug('get_psirt_cache_file', 'cache miss: %s' % (name))
            return None

        return content['content']

    def set_psirt_cache_file(self, name, content):
        filename = os.path.join(
            self.psirt_cache_directory,
            name
        )

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(content, indent=4))

        except BaseException:
            self.log.error('set_psirt_cache_file', traceback.format_exc())
            return False

        return True

    def get_psirt_cache_entry(self, cache_entry_name):
        if not self.psirt_cache_enabled:
            return None
        return self.get_psirt_cache_file(cache_entry_name)

    def set_psirt_cache_entry(self, cache_entry_name, entry_content):
        content = {}
        content['content'] = entry_content
        content['timestamp'] = int(time.time())
        return self.set_psirt_cache_file(cache_entry_name, content)
