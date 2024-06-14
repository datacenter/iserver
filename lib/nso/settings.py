import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class NsoSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.nso_settings_filename = os.path.join(
            self.settings_dir,
            'nso'
        )

        if not self.initialize_nso_settings():
            raise ValueError('NSO settings initialization failed')

    def get_nso_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Defaults'] = {}
        settings['Defaults']['Ncs'] = None
        settings['Ncs'] = []
        return settings

    def initialize_nso_settings(self):
        if not os.path.isfile(self.nso_settings_filename):
            settings = self.get_nso_default_settings()
            if not self.set_nso_settings(settings):
                return False
        return True

    def get_nso_settings(self):
        if not os.path.isfile(self.nso_settings_filename):
            return None

        try:
            with open(self.nso_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_nso_settings', traceback.format_exc())
            return None

        return settings

    def set_nso_settings(self, settings):
        try:
            with open(self.nso_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_nso_settings', traceback.format_exc())
            return False

        return True

    def get_default_ncs(self):
        settings = self.get_nso_settings()
        if settings is None:
            return None

        try:
            default_ncs_name = settings['Defaults']['Ncs']
        except BaseException:
            default_ncs_name = None

        return default_ncs_name

    def set_default_ncs(self, name):
        settings = self.get_nso_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Ncs'] = name
        return self.set_nso_settings(settings)

    def get_nso_ncss(self):
        settings = self.get_nso_settings()
        if settings is None:
            return None

        return settings['Ncs']

    def get_nso_ncs(self, nso_name):
        ncss = self.get_nso_ncss()
        if ncss is None:
            return None

        for ncs in ncss:
            if ncs['name'] == nso_name:
                return ncs

        return None

    def set_nso_ncss(self, ncss):
        settings = self.get_nso_settings()
        if settings is None:
            return False

        settings['Ncs'] = ncss
        return self.set_nso_settings(settings)

    def set_nso_ncs(self, nso_name, rest_protocol, nso_ip, nso_port, nso_username, nso_password, restconf_enabled, nfvo):
        ncss = self.get_nso_ncss()
        if ncss is None:
            return False

        new_ncss = []
        for ncs in ncss:
            if ncs['name'] != nso_name:
                new_ncss.append(ncs)

        new_ncs = {}
        new_ncs['name'] = nso_name
        new_ncs['protocol'] = rest_protocol
        new_ncs['ip'] = nso_ip
        new_ncs['port'] = nso_port
        new_ncs['username'] = nso_username
        new_ncs['password'] = nso_password
        new_ncs['restconf_enabled'] = restconf_enabled
        new_ncs['nfvo'] = nfvo
        new_ncss.append(new_ncs)

        return self.set_nso_ncss(new_ncss)

    def delete_nso_ncs(self, nso_name):
        ncss = self.get_nso_ncss()
        if ncss is None:
            return False

        new_ncss = []
        for ncs in ncss:
            if ncs['name'] != nso_name:
                new_ncss.append(ncs)

        return self.set_nso_ncss(new_ncss)

    def print_nso_ncss(self, ncss, show_password=True):
        ncss = sorted(ncss, key=lambda i: i['name'])
        if not show_password:
            for ncs in ncss:
                ncs['password'] = '******'

        order = [
            'name',
            'protocol',
            'ip',
            'port',
            'username',
            'password',
            'restconf_enabled',
            'nfvo'
        ]

        headers = [
            'Name',
            'REST Protocol',
            'IP',
            'Port',
            'Username',
            'Password',
            'RESTCONF',
            'NFVO'
        ]

        self.my_output.my_table(
            ncss,
            order=order,
            headers=headers,
            table=True
        )
