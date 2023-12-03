import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class IntersightSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self)

        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id
        self.my_output = None

        self.intersight_settings_filename = os.path.join(
            self.settings_dir,
            'intersight'
        )

        if not self.initialize_intersight_settings():
            raise ValueError('Intersight settings initialization failed')

    def initialize_intersight_settings(self):
        if not os.path.isfile(self.intersight_settings_filename):
            settings = self.get_intersight_default_settings()
            if not self.set_intersight_settings(settings):
                return False

            if settings['CacheEnabled']:
                os.makedirs(
                    settings['ComputeCacheDirectory'],
                    exist_ok=True
                )

        settings_changed = False
        settings = self.get_intersight_settings()

        if 'CacheEnabled' not in settings:
            settings['CacheEnabled'] = True
            settings_changed = True

        if 'CacheTtl' not in settings:
            settings['CacheTtl'] = 600
            settings_changed = True

        if 'ComputeCacheDirectory' not in settings:
            settings['ComputeCacheDirectory'] = os.path.join(
                self.settings_dir,
                'compute'
            )

        if settings_changed:
            self.set_intersight_settings(
                settings
            )

        return True

    def get_intersight_settings(self):
        if not os.path.isfile(self.intersight_settings_filename):
            return None

        try:
            with open(self.intersight_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_intersight_settings', traceback.format_exc())
            return None

        return settings

    def set_intersight_settings(self, settings):
        try:
            with open(self.intersight_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_intersight_settings', traceback.format_exc())
            return False

        return True

    def set_cache_enabled(self):
        settings = self.get_intersight_settings()
        settings['CacheEnabled'] = True
        return self.set_intersight_settings(settings)

    def set_cache_disabled(self):
        settings = self.get_intersight_settings()
        settings['CacheEnabled'] = False
        return self.set_intersight_settings(settings)

    def set_cache_ttl(self, ttl):
        if not isinstance(ttl, int):
            self.log.error('set_cache_ttl', 'ttl must be integer')
            return False

        if ttl <= 0:
            self.log.error('set_cache_ttl', 'ttl must be integer gt 0')
            return False

        settings = self.get_intersight_settings()
        settings['CacheTtl'] = ttl
        return self.set_intersight_settings(settings)

    def get_intersight_default_settings(self):
        settings = {}
        settings['CacheEnabled'] = True
        settings['CacheTtl'] = 600
        settings['ComputeCacheDirectory'] = os.path.join(
            self.settings_dir,
            'compute'
        )
        return settings

    def get_intersight_cache_ttl(self):
        settings = self.get_intersight_settings()
        if not settings['CacheEnabled']:
            return None
        return settings['CacheTtl']

    def print_intersight_settings(self):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(
                log_id=self.log_id,
                verbose=False,
                debug=False
            )

        settings = self.get_intersight_settings()
        if settings is None:
            self.my_output.error('Intersight settings not found')
            return

        order = [
            'CacheEnabled',
            'CacheTtl',
            'ComputeCacheDirectory'
        ]

        headers = [
            'Cache Enabled',
            'Cache TTL [sec]',
            'Compute Cache Directory'
        ]

        self.my_output.dictionary(
            settings,
            title='Intersight Settings',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
