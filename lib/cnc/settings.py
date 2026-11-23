import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class CncSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.cnc_settings_filename = os.path.join(
            self.settings_dir,
            'cnc'
        )

        self.cnc_cache_directory = os.path.join(
            self.settings_dir,
            'cnc-cache'
        )

        if not self.initialize_cnc_settings():
            raise ValueError('CNC settings initialization failed')

    def get_cnc_default_cache_settings(self):
        settings = {}
        settings['enabled'] = True
        settings['ttl'] = 0
        settings['ttlT'] = '--'
        settings['object'] = []
        return settings

    def get_cnc_default_settings(self):
        settings = {}
        settings['enabled'] = True
        settings['cache'] = self.get_cnc_default_cache_settings()
        settings['controllers'] = []
        settings['defaults'] = {}
        settings['defaults']['controller'] = None
        return settings

    def get_cnc_controller_label(self, cnc_name, requested_ttl=-1):
        controller = self.get_cnc_controller(cnc_name)
        if controller is None:
            return 'CNC: %s (adhoc, mode:online, cache:off)' % (cnc_name)

        label = 'CNC: %s (' % (cnc_name)

        if requested_ttl < 0:
            if self.is_cache_enabled(cnc_name):
                label = '%scache:on)' % (label)
            else:
                label = '%scache:off)' % (label)
        else:
            if requested_ttl == 0:
                label = '%scache:on, ttl:any)' % (label)
            else:
                label = '%scache:on, ttl:%s)' % (label, requested_ttl)

        return label

    def initialize_cnc_settings(self):
        if not os.path.isfile(self.cnc_settings_filename):
            settings = self.get_cnc_default_settings()
            if not self.set_cnc_settings(settings):
                return False

        return True

    def get_cnc_settings(self):
        if not os.path.isfile(self.cnc_settings_filename):
            return None

        try:
            with open(self.cnc_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_cnc_settings', traceback.format_exc())
            return None

        return settings

    def set_cnc_settings(self, settings):
        try:
            with open(self.cnc_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_cnc_settings', traceback.format_exc())
            return False

        return True

    def get_cnc_cache_base_directory(self):
        return self.cnc_cache_directory

    def get_cnc_cache_default_settings(self):
        settings = self.get_cnc_settings()
        return settings['cache']

    def get_cnc_cache_settings(self, cnc_name):
        settings = self.get_cnc_settings()
        for controller in settings['controllers']:
            if controller['name'] == cnc_name:
                return controller['cache']

        self.log.error(
            'get_cnc_cache_settings',
            'cnc not found: %s' % (cnc_name)
        )

        return None

    def is_cache_enabled(self, cnc_name):
        cache_settings = self.get_cnc_cache_settings(
            cnc_name
        )
        if cache_settings is None:
            return False

        return cache_settings['enabled']

    def get_default_controller(self):
        settings = self.get_cnc_settings()
        if settings is None:
            return None

        default_controller_name = settings['defaults']['controller']
        return default_controller_name

    def set_default_controller(self, name):
        settings = self.get_cnc_settings()
        if settings is None:
            return False

        settings['defaults']['controller'] = name
        return self.set_cnc_settings(settings)

    def get_cnc_controller_names(self):
        controllers = self.get_cnc_controllers()
        if controllers is None:
            return None

        names = []
        for controller in controllers:
            names.append(
                controller['name']
            )

        return names

    def get_cnc_controllers(self):
        settings = self.get_cnc_settings()
        if settings is None:
            return None

        return settings['controllers']

    def get_cnc_domain_controllers(self, domain_name):
        settings = self.get_cnc_settings()
        if settings is None:
            return None

        domain_controllers = []
        for controller in settings['controllers']:
            if controller['domain'] == domain_name:
                domain_controllers.append(
                    controller
                )

        return domain_controllers

    def get_cnc_controller(self, cnc_name):
        controllers = self.get_cnc_controllers()
        if controllers is None:
            return None

        for controller in controllers:
            if controller['name'] == cnc_name:
                return controller

        return None

    def set_cnc_controllers(self, controllers):
        settings = self.get_cnc_settings()
        if settings is None:
            return False

        settings['controllers'] = controllers
        return self.set_cnc_settings(settings)

    def set_cnc_controller(self, cnc_name, cnc_ip, cnc_port, cnc_username, cnc_password, domain=''):
        controllers = self.get_cnc_controllers()
        if controllers is None:
            return False

        new_controllers = []
        cache_settings = self.get_cnc_cache_default_settings()
        for controller in controllers:
            if controller['name'] == cnc_name:
                cache_settings = controller['cache']
            else:
                new_controllers.append(controller)

        new_controller = {}
        new_controller['name'] = cnc_name
        new_controller['ip'] = cnc_ip
        new_controller['port'] = cnc_port
        new_controller['username'] = cnc_username
        new_controller['password'] = cnc_password
        new_controller['domain'] = domain
        new_controller['cache'] = cache_settings
        new_controllers.append(new_controller)

        return self.set_cnc_controllers(new_controllers)

    def delete_cnc_controller(self, cnc_name):
        controllers = self.get_cnc_controllers()
        if controllers is None:
            return False

        new_controllers = []
        for controller in controllers:
            if controller['name'] != cnc_name:
                new_controllers.append(controller)

        return self.set_cnc_controllers(new_controllers)
