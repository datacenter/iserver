import copy
import os
import json
import traceback
from datetime import timedelta

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class ApicSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.apic_settings_filename = os.path.join(
            self.settings_dir,
            'apic'
        )

        self.apic_cache_directory = os.path.join(
            self.settings_dir,
            'aci-switch'
        )

        if not self.initialize_apic_settings():
            raise ValueError('APIC settings initialization failed')

    def get_apic_offline_cache_settings(self):
        settings = {}
        settings['enabled'] = True
        settings['ttl'] = -1
        settings['ttlT'] = '--'
        settings['object'] = []
        return settings

    def get_apic_default_cache_settings(self):
        settings = {}
        settings['enabled'] = True
        settings['ttl'] = 180
        settings['ttlT'] = '{}'.format(str(timedelta(seconds=settings['ttl'])))
        settings['object'] = []
        return settings

    def get_apic_default_settings(self):
        settings = {}
        settings['enabled'] = True
        settings['cache'] = self.get_apic_default_cache_settings()
        settings['controllers'] = []
        settings['defaults'] = {}
        settings['defaults']['controller'] = None
        settings['defaults']['node'] = {}
        return settings

    def initialize_apic_settings(self):
        if not os.path.isfile(self.apic_settings_filename):
            settings = self.get_apic_default_settings()
            if not self.set_apic_settings(settings):
                return False

        if not os.path.isdir(self.apic_cache_directory):
            os.makedirs(self.apic_cache_directory, exist_ok=True)

        return True

    def fixup_apic_settings(self, settings):
        fixup = False

        # upper case old-style
        if 'Enabled' in settings:
            settings['enabled'] = settings['Enabled']
            del settings['Enabled']
            fixup = True

        if 'Cache' in settings:
            settings['cache'] = {}
            settings['cache']['enabled'] = settings['Cache']['Enabled']
            if 'ttl' in settings['Cache']:
                settings['cache']['ttl'] = settings['Cache']['ttl']
            else:
                settings['cache']['ttl'] = 180
            settings['cache']['ttlT'] = '{}'.format(str(timedelta(seconds=settings['cache']['ttl'])))

            if 'Object' in settings['Cache']:
                settings['cache']['object'] = copy.deepcopy(
                    settings['Cache']['Object']
                )
            else:
                settings['cache']['object'] = {}

            del settings['Cache']
            fixup = True

        if 'Controllers' in settings:
            settings['controllers'] = copy.deepcopy(
                settings['Controllers']
            )
            del settings['Controllers']
            fixup = True

        if 'Defaults' in settings:
            settings['defaults'] = {}
            settings['defaults']['controller'] = settings['Defaults']['Controller']
            settings['defaults']['node'] = copy.deepcopy(
                settings['Defaults']['Node']
            )
            del settings['Defaults']
            fixup = True

        # cache fix-up

        if 'cache' not in settings:
            settings['cache'] = self.get_apic_default_cache_settings()
            fixup = True

        if 'ttlT' not in settings['cache']:
            if settings['cache']['ttl'] <= 0:
                settings['cache']['ttlT'] = '--'
            else:
                settings['cache']['ttlT'] = '{}'.format(str(timedelta(seconds=settings['cache']['ttl'])))
            fixup = True

        global_cache_settings = settings['cache']
        for controller in settings['controllers']:
            if 'port' not in controller:
                controller['port'] = 443

            if 'cache' not in controller:
                controller['cache'] = copy.deepcopy(global_cache_settings)
                fixup = True

            if 'ttlT' not in controller['cache']:
                if controller['cache']['ttl'] <= 0:
                    controller['cache']['ttlT'] = '--'
                else:
                    controller['cache']['ttlT'] = '{}'.format(str(timedelta(seconds=controller['cache']['ttl'])))
                fixup = True

        # online mode fix-up
        for controller in settings['controllers']:
            if 'online' not in controller:
                controller['online'] = True
                fixup = True

        if fixup:
            return settings

        return None

    def get_apic_settings(self):
        if not os.path.isfile(self.apic_settings_filename):
            return None

        try:
            with open(self.apic_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_apic_settings', traceback.format_exc())
            return None

        new_settings = self.fixup_apic_settings(
            settings
        )
        if new_settings is not None:
            if not self.set_apic_settings(new_settings):
                return None
            return new_settings

        return settings

    def set_apic_settings(self, settings):
        try:
            with open(self.apic_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_apic_settings', traceback.format_exc())
            return False

        return True

    def set_apic_mode_online(self, apic_name=None):
        settings = self.get_apic_settings()

        for controller in settings['controllers']:
            if apic_name is None or controller['name'] == apic_name:
                controller['online'] = True
                controller['cache'] = settings['cache']

        return self.set_apic_settings(settings)

    def set_apic_mode_offline(self, apic_name=None):
        settings = self.get_apic_settings()

        for controller in settings['controllers']:
            if apic_name is None or controller['name'] == apic_name:
                controller['online'] = False
                controller['cache'] = self.get_apic_offline_cache_settings()

        return self.set_apic_settings(settings)

    def get_apic_cache_base_directory(self):
        return self.apic_cache_directory

    def get_apic_cache_default_settings(self):
        settings = self.get_apic_settings()
        return settings['cache']

    def get_apic_cache_settings(self, apic_name):
        settings = self.get_apic_settings()
        for controller in settings['controllers']:
            if controller['name'] == apic_name:
                return controller['cache']

        self.log.error(
            'get_apic_cache_settings',
            'apic not found: %s' % (apic_name)
        )

        return None

    def is_cache_enabled(self, apic_name):
        cache_settings = self.get_apic_cache_settings(
            apic_name
        )
        if cache_settings is None:
            return False

        return cache_settings['enabled']

    def set_apic_cache_on(self, apic_name=None):
        settings = self.get_apic_settings()
        for controller in settings['controllers']:
            if apic_name is None or controller['name'] == apic_name:
                controller['cache']['enabled'] = True

        return self.set_apic_settings(settings)

    def set_apic_cache_off(self, apic_name=None):
        settings = self.get_apic_settings()
        for controller in settings['controllers']:
            if apic_name is None or controller['name'] == apic_name:
                if controller['online']:
                    controller['cache']['enabled'] = False
        return self.set_apic_settings(settings)

    def set_apic_cache_ttl(self, ttl, apic_name=None):
        settings = self.get_apic_settings()
        for controller in settings['controllers']:
            if apic_name is None or controller['name'] == apic_name:
                controller['cache']['ttl'] = ttl
                if ttl <= 0:
                    controller['cache']['ttlT'] = '--'
                else:
                    controller['cache']['ttlT'] = '{}'.format(str(timedelta(seconds=controller['cache']['ttl'])))
        return self.set_apic_settings(settings)

    def get_default_node(self, controller_name):
        settings = self.get_apic_settings()
        if settings is None:
            return None

        if controller_name not in settings['defaults']['node']:
            return None

        default_node_name = settings['defaults']['node'][controller_name]
        return default_node_name

    def set_default_node(self, controller_name, node_name):
        settings = self.get_apic_settings()
        if settings is None:
            return False

        settings['defaults']['node'][controller_name] = node_name
        return self.set_apic_settings(settings)

    def get_default_controller(self):
        settings = self.get_apic_settings()
        if settings is None:
            return None

        default_controller_name = settings['defaults']['controller']
        return default_controller_name

    def set_default_controller(self, name):
        settings = self.get_apic_settings()
        if settings is None:
            return False

        settings['defaults']['controller'] = name
        return self.set_apic_settings(settings)

    def get_apic_controller_names(self):
        controllers = self.get_apic_controllers()
        if controllers is None:
            return None

        names = []
        for controller in controllers:
            names.append(
                controller['name']
            )

        return names

    def get_apic_controllers(self):
        settings = self.get_apic_settings()
        if settings is None:
            return None

        return settings['controllers']

    def get_apic_domain_controllers(self, domain_name):
        settings = self.get_apic_settings()
        if settings is None:
            return None

        domain_controllers = []
        for controller in settings['controllers']:
            if controller['domain'] == domain_name:
                domain_controllers.append(
                    controller
                )

        return domain_controllers

    def is_apic_online(self, apic_name):
        controller = self.get_apic_controller(apic_name)
        if controller is None:
            return False
        return controller['online']

    def get_apic_controller_label(self, apic_name):
        controller = self.get_apic_controller(apic_name)
        if controller is None:
            return 'Apic: %s (adhoc, mode:online, cache:off)' % (apic_name)

        label = 'Apic: %s (' % (apic_name)
        if self.is_apic_online(apic_name):
            label = '%smode:online, ' % (label)
        else:
            label = '%smode:offline, ' % (label)

        if self.is_cache_enabled(apic_name):
            label = '%scache:on)' % (label)
        else:
            label = '%scache:off)' % (label)

        return label

    def get_apic_controller(self, apic_name):
        controllers = self.get_apic_controllers()
        if controllers is None:
            return None

        for controller in controllers:
            if controller['name'] == apic_name:
                return controller

        return None

    def set_apic_controllers(self, controllers):
        settings = self.get_apic_settings()
        if settings is None:
            return False

        settings['controllers'] = controllers
        return self.set_apic_settings(settings)

    def set_apic_controller(self, apic_name, apic_ip, apic_port, apic_username, apic_password, domain=''):
        controllers = self.get_apic_controllers()
        if controllers is None:
            return False

        new_controllers = []
        cache_settings = self.get_apic_cache_default_settings()
        online_mode = True
        for controller in controllers:
            if controller['name'] == apic_name:
                cache_settings = controller['cache']
                online_mode = controller['online']
            else:
                new_controllers.append(controller)

        new_controller = {}
        new_controller['name'] = apic_name
        new_controller['ip'] = apic_ip
        new_controller['port'] = apic_port
        new_controller['username'] = apic_username
        new_controller['password'] = apic_password
        new_controller['domain'] = domain
        new_controller['cache'] = cache_settings
        new_controller['online'] = online_mode
        new_controllers.append(new_controller)

        return self.set_apic_controllers(new_controllers)

    def delete_apic_controller(self, apic_name):
        controllers = self.get_apic_controllers()
        if controllers is None:
            return False

        new_controllers = []
        for controller in controllers:
            if controller['name'] != apic_name:
                new_controllers.append(controller)

        return self.set_apic_controllers(new_controllers)
