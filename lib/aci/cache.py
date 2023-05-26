import time
import os
import json

from lib.aci import settings


class Cache():
    def __init__(self, cache_enabled):
        self.cache_enabled = cache_enabled
        if self.cache_enabled:
            settings_handler = settings.ApicSettings()
            self.cache_settings = settings_handler.get_apic_cache_settings()
            self.cache_directory = os.path.join(
                settings_handler.get_apic_cache_base_directory(),
                self.apic_name
            )

    def is_cache_enabled(self):
        if not self.cache_enabled:
            return False

        if self.cache_settings is None:
            return False

        return self.cache_settings['Enabled']

    def is_object_cache_enabled(self, object_name):
        if not self.is_cache_enabled():
            return False

        if object_name not in self.cache_settings['Object']:
            return False

        return self.cache_settings['Object'][object_name]['enabled']

    def get_object_cache_filename(self, object_name):
        if not self.is_object_cache_enabled(object_name):
            return None

        filename = os.path.join(
            self.cache_directory,
            self.cache_settings['Object'][object_name]['filename']
        )

        return filename

    def get_object_cache(self, object_name, object_selector=None):
        filename = self.get_object_cache_filename(object_name)
        if filename is None:
            return None

        if object_selector is not None:
            filename = '%s.%s' % (filename, object_selector)

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

        except BaseException:
            return None

        if self.cache_settings['Object'][object_name]['ttl'] is not None:
            if content['timestamp'] - int(time.time()) > self.cache_settings['Object'][object_name]['ttl']:
                return None

        return content['cache']

    def set_object_cache(self, object_name, cache, object_selector=None):
        filename = self.get_object_cache_filename(object_name)
        if filename is None:
            return False

        if not os.path.isdir(self.cache_directory):
            os.makedirs(self.cache_directory, exist_ok=True)

        content = {}
        content['object'] = object_name
        content['timestamp'] = int(time.time())
        content['cache'] = cache

        if object_selector is not None:
            filename = '%s.%s' % (filename, object_selector)

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(content, indent=4))

        except BaseException:
            self.log.error(
                'apic.set_object_cache',
                'Set cache failed: %s %s' % (
                    self.nexus_ip,
                    object
                )
            )
            return False

        return True
