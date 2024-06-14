import os

from lib import log_helper
from lib import file_helper
from lib import output_helper
from lib.settings_helper import Settings


class OpenShiftSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.openshift_settings_directory = os.path.join(
            self.settings_dir,
            'openshift'
        )

        self.openshift_api_token_filename = os.path.join(
            self.openshift_settings_directory,
            'token'
        )

        self.openshift_pull_secret_filename = os.path.join(
            self.openshift_settings_directory,
            'pull_secret.txt'
        )

        if not self.initialize_openshift_settings():
            raise ValueError('OpenShift settings initialization failed')

    def initialize_openshift_settings(self):
        if not os.path.isdir(self.openshift_settings_directory):
            os.makedirs(self.openshift_settings_directory, exist_ok=True)
        return True

    def is_configured(self):
        if self.get_api_token() is None:
            return False

        if self.get_pull_secret() is None:
            return False

        return True

    def get_api_token(self):
        return file_helper.get_file_text(self.openshift_api_token_filename)

    def set_api_token(self, token):
        return file_helper.set_file(self.openshift_api_token_filename, token)

    def get_pull_secret(self):
        return file_helper.get_file_text(self.openshift_pull_secret_filename)

    def set_pull_secret(self, filename):
        pull_secret = self.get_file_text(filename)
        if pull_secret is None:
            return False

        return file_helper.set_file(self.openshift_pull_secret_filename, pull_secret)
