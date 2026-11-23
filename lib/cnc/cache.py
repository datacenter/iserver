import time
import os
import json

from lib.cnc import settings


class Cache():
    def __init__(self, cnc_name, requested_ttl=-1):
        if cnc_name is None:
            self.cache_enabled = False
            self.cache_write_enabled = False
            return

        settings_handler = settings.CncSettings()

        self.cache_directory = os.path.join(
            settings_handler.get_cnc_cache_base_directory(),
            cnc_name
        )

        self.cache_settings = settings_handler.get_cnc_cache_settings(
            cnc_name
        )
        self.cache_enabled = self.cache_settings['enabled']
        self.cache_write_enabled = True

        if requested_ttl >= 0:
            self.cache_enabled = True
            self.ttl = requested_ttl

        if requested_ttl < 0:
            if self.cache_enabled:
                self.ttl = self.cache_settings['ttl']
            else:
                self.ttl = -1

    def is_cache_enabled(self):
        return self.cache_enabled

    def is_object_cache_enabled(self, object_name):
        if not self.is_cache_enabled():
            return False

        if object_name not in self.cache_settings['object']:
            return True

        return self.cache_settings['object'][object_name]['enabled']

    def get_object_cache_filename(self, object_name):
        filename = os.path.join(
            self.cache_directory,
            object_name
        )
        return filename

    def get_object_cache_ttl(self, object_name):
        if object_name in self.cache_settings['object']:
            return self.cache_settings['object'][object_name]['ttl']

        return self.cache_settings['ttl']

    def get_object_cache(self, object_name, object_selector=None):
        if not self.is_cache_enabled():
            return None

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

        cache_hit = False
        effective_ttl = 0
        age = int(time.time()) - content['timestamp']
        if self.ttl == 0:
            cache_hit = True
            effective_ttl = self.ttl

        if self.ttl > 0:
            ttl = self.get_object_cache_ttl(object_name)
            if age <= ttl:
                cache_hit = True
                effective_ttl = self.ttl

        if self.ttl < 0:
            ttl = self.get_object_cache_ttl(object_name)
            if ttl == 0:
                cache_hit = True
                effective_ttl = ttl

            if ttl > 0 and age <= ttl:
                cache_hit = True
                effective_ttl = ttl

        if not cache_hit:
            return None

        self.log.cache_hit(
            'cnc',
            self.cnc_name,
            object_name,
            filename,
            effective_ttl,
            age
        )

        return content['cache']

    def set_object_cache(self, object_name, cache, object_selector=None, enforce=False):
        if not self.cache_write_enabled:
            if not enforce:
                return False

        filename = self.get_object_cache_filename(object_name)
        if filename is None:
            return False

        if not os.path.isdir(self.cache_directory):
            os.makedirs(self.cache_directory, exist_ok=True)

        content = {}
        content['object'] = object_name
        content['selector'] = object_selector
        content['timestamp'] = int(time.time())
        content['cache'] = cache

        if object_selector is not None:
            object_selector = object_selector.replace('/', '_')
            filename = '%s.%s' % (filename, object_selector)

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(content, indent=4))

        except BaseException:
            self.log.error(
                'cnc.set_object_cache',
                'Set cache failed: %s %s %s %s' % (
                    self.cnc_name,
                    object_name,
                    object_selector,
                    filename
                )
            )
            return False

        return True
