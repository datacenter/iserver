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
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

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

    def get_intersight_default_settings(self):
        settings = {}
        settings['CacheEnabled'] = True
        settings['ComputeCacheDirectory'] = os.path.join(
            self.settings_dir,
            'compute'
        )
        return settings

    def print_intersight_settings(self):
        settings = self.get_intersight_settings()
        if settings is None:
            self.my_output.error('Intersight settings not found')
            return

        order = [
            'CacheEnabled',
            'ComputeCacheDirectory'
        ]

        headers = [
            'Cache Enabled',
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
