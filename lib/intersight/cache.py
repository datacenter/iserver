import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.intersight.settings import IntersightSettings


class IntersightCache(IntersightSettings):
    def __init__(self, log_id=None):
        IntersightSettings.__init__(self, log_id=log_id)
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.intersight_settings = self.get_intersight_settings()
        if self.intersight_settings is None:
            raise ValueError('Intersight settings read failed')

        self.intersight_cache_enabled = self.is_intersight_cache_enabled()
        self.intersight_cache_directory = None
        if self.intersight_cache_enabled:
            self.intersight_cache_directory = self.intersight_settings['ComputeCacheDirectory']

    def is_intersight_cache_enabled(self):
        if 'CacheEnabled' in self.intersight_settings:
            return self.intersight_settings['CacheEnabled']
        return False

    def is_intersight_cache_entry(self, cache_entry_name):
        if not self.intersight_cache_enabled:
            return False

        filename = os.path.join(
            self.intersight_cache_directory,
            cache_entry_name
        )

        return os.path.isfile(filename)

    def get_intersight_cache_entry(self, cache_entry_name):
        if not self.intersight_cache_enabled:
            return None

        filename = os.path.join(
            self.intersight_cache_directory,
            cache_entry_name
        )

        if not os.path.isfile(filename):
            return None

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                cache_entry = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_intersight_cache_entry', traceback.format_exc())
            return None

        return cache_entry

    def set_intersight_cache_entry(self, cache_entry_name, cache_entry_content):
        if not self.intersight_cache_enabled:
            return False

        filename = os.path.join(
            self.intersight_cache_directory,
            cache_entry_name
        )

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(
                    json.dumps(
                        cache_entry_content,
                        indent=4
                    )
                )

        except BaseException:
            self.log.error('set_intersight_cache_entry', traceback.format_exc())
            return False

        return True

    def get_intersight_cache_entry_property(self, cache_entry_name, property_name):
        cache_entry_content = self.get_intersight_cache_entry(
            cache_entry_name
        )

        if cache_entry_content is None:
            return None

        if property_name not in cache_entry_content:
            return None

        return cache_entry_content[property_name]

    def get_intersight_cache_entry_properties(self, cache_entry_name):
        cache_entry_content = self.get_intersight_cache_entry(
            cache_entry_name
        )

        if cache_entry_content is None:
            return None

        return cache_entry_content.keys()

    def set_intersight_cache_entry_property(self, cache_entry_name, property_name, property_value):
        cache_entry_content = self.get_intersight_cache_entry(
            cache_entry_name
        )

        if cache_entry_content is None:
            cache_entry_content = {}

        cache_entry_content[property_name] = property_value
        return self.set_intersight_cache_entry(cache_entry_name, cache_entry_content)
