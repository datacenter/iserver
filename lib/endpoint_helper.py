import os
import json
import traceback

from lib import log_helper
from lib.settings_helper import Settings


class EndpointSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.endpoint_directory = os.path.join(
            self.settings_dir,
            'endpoint'
        )

        if not self.initialize_endpoint_directory():
            raise ValueError('Endpoints initialization failed')

    def initialize_endpoint_directory(self):
        try:
            if not os.path.isdir(self.endpoint_directory):
                os.makedirs(self.endpoint_directory)

            for filename in os.listdir(self.endpoint_directory):
                filename_path = os.path.join(
                    self.endpoint_directory,
                    filename
                )
                if os.path.isdir(filename_path):
                    continue

                try:
                    with open(filename_path, 'r', encoding='utf-8') as file_handler:
                        settings = json.loads(file_handler.read())

                except BaseException:
                    self.log.error(
                        'initialize_endpoint_directory',
                        'File read failed: %s' % (filename_path)
                    )
                    continue

                os.remove(filename_path)
                os.makedirs(filename_path, exist_ok=True)

                settings_filename = os.path.join(
                    filename_path,
                    'settings'
                )

                try:
                    with open(settings_filename, 'w', encoding='utf-8') as file_handler:
                        file_handler.write(
                            json.dumps(
                                settings,
                                indent=4
                            )
                        )

                except BaseException:
                    self.log.error(
                        'initialize_endpoint_directory',
                        'File write failed: %s' % (settings_filename)
                    )

        except BaseException:
            return False
        return True

    def get_endpoint_ids(self):
        return os.listdir(self.endpoint_directory)

    def get_endpoint_settings(self, endpoint_id, filename='settings'):
        endpoint_directory = os.path.join(
            self.endpoint_directory,
            endpoint_id
        )
        endpoint_filename = os.path.join(
            endpoint_directory,
            filename
        )
        if not os.path.isfile(endpoint_filename):
            return None

        try:
            with open(endpoint_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error(
                'get_endpoint_settings',
                'File read failed: %s' % (endpoint_filename)
            )
            return None

        return settings

    def set_endpoint_settings(self, endpoint_id, settings, filename='settings'):
        endpoint_directory = os.path.join(
            self.endpoint_directory,
            endpoint_id
        )
        if not os.path.isdir(endpoint_directory):
            os.makedirs(endpoint_directory, exist_ok=True)

        endpoint_filename = os.path.join(
            endpoint_directory,
            filename
        )

        try:
            with open(endpoint_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(
                    json.dumps(
                        settings,
                        indent=4
                    )
                )

        except BaseException:
            self.log.error(
                'set_endpoint_settings',
                'File write failed: %s' % (endpoint_filename)
            )
            return False

        return True
