import os
import json
import traceback

from lib import log_helper
from lib.settings_helper import Settings


class PsirtSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        self.psirt_settings_filename = os.path.join(
            self.settings_dir,
            'psirt'
        )

        self.psirt_cache_directory = os.path.join(
            self.settings_dir,
            'psirt-cache'
        )

        if not self.initialize_psirt_settings():
            raise ValueError('Psirt settings initialization failed')

    def get_psirt_default_settings(self):
        settings = {}
        settings['enabled'] = False
        settings['key'] = None
        settings['secret'] = None
        settings['cache'] = True
        settings['directory'] = self.psirt_cache_directory
        settings['ttl'] = 60 * 60 * 24
        return settings

    def initialize_psirt_settings(self):
        if not os.path.isfile(self.psirt_settings_filename):
            settings = self.get_psirt_default_settings()
            if not self.set_psirt_settings(settings):
                return False

        if not os.path.isdir(self.psirt_cache_directory):
            os.makedirs(self.psirt_cache_directory, exist_ok=True)

        return True

    def get_psirt_settings(self):
        if not os.path.isfile(self.psirt_settings_filename):
            return None

        try:
            with open(self.psirt_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_psirt_settings', traceback.format_exc())
            return None

        return settings

    def set_psirt_settings(self, settings):
        try:
            with open(self.psirt_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_psirt_settings', traceback.format_exc())
            return False

        return True

    def get_psirt_credentials(self):
        settings = self.get_psirt_settings()
        if not settings['enabled']:
            return None, None
        return settings['key'], settings['secret']

    def set_psirt_credentials(self, key, secret, enabled=True):
        settings = self.get_psirt_settings()
        settings['enabled'] = enabled
        settings['key'] = key
        settings['secret'] = secret
        return self.set_psirt_settings(settings)

    def set_cache_on(self):
        settings = self.get_psirt_settings()
        settings['cache'] = True
        return self.set_psirt_settings(settings)

    def set_cache_off(self):
        settings = self.get_psirt_settings()
        settings['cache'] = False
        return self.set_psirt_settings(settings)

    def set_cache_ttl(self, ttl):
        settings = self.get_psirt_settings()
        settings['ttl'] = ttl
        return self.set_psirt_settings(settings)
