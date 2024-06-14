import json
import os
import subprocess
import traceback
from pathlib import Path

from lib import log_helper


class Settings():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.home_dir = self.get_home_directory()

        self.settings_dir = os.path.join(
            self.home_dir,
            '.itool'
        )

        self.iaccount_dir = os.path.join(
            self.settings_dir,
            'iaccount'
        )

        self.ssh_dir = os.path.join(
            self.settings_dir,
            'ssh'
        )

        self.settings_filename = os.path.join(
            self.settings_dir,
            'settings'
        )

    def get_home_directory(self):
        return str(Path.home())

    def get_settings_dir(self):
        return self.settings_dir

    def initialize_settings(self):
        for directory in [self.settings_dir, self.iaccount_dir, self.ssh_dir]:
            if not os.path.isdir(directory):
                os.makedirs(directory)

        if not self.is_settings() or self.get_settings() is None:
            if not self.rfd_settings():
                return False
        else:
            if not self.fixup_settings():
                return False

        return True

    def run(self, command):
        try:
            with subprocess.Popen(
                args=command,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                shell=True,
                env=os.environ
            ) as process:
                output, error = process.communicate()
                return process.returncode, output.decode('utf-8')
        except BaseException:
            return 1, 'Traceback'

    def is_settings(self):
        '''
        Returns True if $HOME/.iwectl/settings file exists
        Returns False otherwise
        '''
        return os.path.isfile(self.settings_filename)

    def get_default_settings(self):
        settings = {}
        settings['iaccount'] = None

        return settings

    def rfd_settings(self):
        settings = self.get_default_settings()
        return self.set_settings(settings)

    def fixup_settings(self):
        settings = self.get_settings()
        default_settings = self.get_default_settings()

        fixup_required = False
        for default_setting in default_settings:
            if default_setting not in settings:
                fixup_required = True
                break

        for setting in settings:
            if setting not in default_settings:
                fixup_required = True
                break

        if fixup_required:
            new_settings = {}

            # First copy valid settings
            for setting in settings:
                if setting in default_settings:
                    new_settings[setting] = settings[setting]

            # Add default settings only if not defined
            for default_setting in default_settings:
                if default_setting not in new_settings:
                    new_settings[default_setting] = default_settings[default_setting]

            return self.set_settings(new_settings)

        return True

    def get_settings(self):
        if self.is_settings():
            try:
                with open(self.settings_filename, 'r', encoding='utf-8') as file_handler:
                    settings = json.loads(file_handler.read())
                return settings
            except BaseException:
                self.log.error('settings_helper.get_settings', traceback.format_exc())
        return None

    def set_settings(self, settings):
        '''
        Returns True/False
        '''
        try:
            with open(self.settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))
        except BaseException:
            self.log.error('settings_helper.set_settings', traceback.format_exc())
            return False
        return True

    def get_setting(self, key, default=None):
        settings = self.get_settings()
        if settings is not None:
            if key in settings:
                return settings[key]
        if default is not None:
            return default
        return None

    def set_setting(self, key, value):
        settings = self.get_settings()
        if settings is not None:
            settings[key] = value
            return self.set_settings(settings)
        return False
