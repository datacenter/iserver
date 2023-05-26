import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class EndpointSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

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
        except BaseException:
            return False
        return True

    def get_endpoint_ids(self):
        return os.listdir(self.endpoint_directory)

    def get_endpoint_settings(self, endpoint_id):
        filename = os.path.join(
            self.endpoint_directory,
            endpoint_id
        )
        if not os.path.isfile(filename):
            return None

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_endpoint_settings', traceback.format_exc())
            return None

        return settings

    def set_endpoint_settings(self, endpoint_id, settings):
        filename = os.path.join(
            self.endpoint_directory,
            endpoint_id
        )

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(
                    json.dumps(
                        settings,
                        indent=4
                    )
                )

        except BaseException:
            self.log.error('set_endpoint_settings', traceback.format_exc())
            return False

        return True
