import os
import json
import traceback

from lib import log_helper
from lib.redfish.settings import RedfishSettings


class RedfishCache(RedfishSettings):
    def __init__(self, log_id=None):
        RedfishSettings.__init__(self, log_id=log_id)
        self.log = log_helper.Log(log_id=log_id)

        self.redfish_settings = self.get_redfish_settings()
        if self.redfish_settings is None:
            raise ValueError('Redfish settings read failed')

        if self.is_cache_enabled():
            self.redfish_cache_directory = self.redfish_settings['CacheDirectory']
            self.redfish_cache_filename = os.path.join(
                self.redfish_cache_directory,
                'cache'
            )

            if not self.initialize_redfish_cache():
                raise ValueError('Redfish cache initialization failed')

    def get_cache_resources_filename(self, cache_entry_name):
        cache_entry = self.get_redfish_cache_entry(cache_entry_name)
        if cache_entry is None:
            return None

        redfish_cache_resources_filename = os.path.join(
            self.redfish_cache_directory,
            cache_entry['CacheFileName']
        )

        return redfish_cache_resources_filename

    def is_cache_enabled(self):
        if 'CacheEnabled' in self.redfish_settings:
            return self.redfish_settings['CacheEnabled']
        return False

    def is_redfish_cache_name(self, cache_entry_name):
        if self.get_redfish_cache_entry(cache_entry_name) is None:
            return False

        return True

    def get_redfish_cache_entry(self, cache_entry_name):
        cache_list = self.get_redfish_cache_list()
        if cache_list is None:
            return None

        for cache_entry in cache_list:
            if cache_entry['CacheName'] == cache_entry_name:
                return cache_entry

        return None

    def add_redfish_cache_entry(self, cache_entry_name, identity):
        if self.is_redfish_cache_name(cache_entry_name):
            return True

        cache_list = self.get_redfish_cache_list()
        if cache_list is None:
            cache_list = []

        cache_list_entry = identity
        cache_list_entry['CacheName'] = cache_entry_name
        cache_list.append(cache_list_entry)

        return self.set_redfish_cache_list(cache_list)

    def delete_redfish_cache_entry(self, cache_entry_name):
        cache_list = self.get_redfish_cache_list()
        if cache_list is None:
            return True

        new_cache_list = []

        for cache_list_entry in cache_list:
            if cache_list_entry['CacheName'] != cache_entry_name:
                new_cache_list.append(cache_list_entry)

            if cache_list_entry['CacheName'] == cache_entry_name:
                redfish_cache_resources_filename = os.path.join(
                    self.redfish_cache_directory,
                    cache_list_entry['CacheFileName']
                )
                if os.path.isfile(redfish_cache_resources_filename):
                    os.remove(redfish_cache_resources_filename)

        return self.set_redfish_cache_list(new_cache_list)

    def delete_redfish_cache_entries(self):
        cache_list = self.get_redfish_cache_list()
        if cache_list is None:
            return True

        for cache_list_entry in cache_list:
            if not self.delete_redfish_cache_entry(cache_list_entry['CacheName']):
                return False

        return True

    def get_redfish_cache_list(self):
        if not os.path.isfile(self.redfish_cache_filename):
            return None

        try:
            with open(self.redfish_cache_filename, 'r', encoding='utf-8') as file_handler:
                cache_list = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_redfish_cache_list', traceback.format_exc())
            return None

        cache_list = sorted(cache_list, key=lambda i: i['Product'])
        return cache_list

    def set_redfish_cache_list(self, cache_list):
        try:
            with open(self.redfish_cache_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(cache_list, indent=4))

        except BaseException:
            self.log.error('set_redfish_cache_list', traceback.format_exc())
            return False

        return True

    def set_redfish_cache_endpoint(self, identity, resources, extra_resources=None, custom_cache_name=None):
        cache_name = identity['DefaultCacheName']
        if custom_cache_name is not None and len(custom_cache_name) > 0:
            cache_name = custom_cache_name

        if not self.add_redfish_cache_entry(cache_name, identity):
            self.log.error(
                'set_redfish_cache_endpoint',
                'Failed to set redfish cache: %s' % (cache_name)
            )
            return None

        try:
            entry = {}
            entry['identity'] = identity
            entry['resources'] = resources
            entry['extra'] = extra_resources

            redfish_cache_resources_filename = os.path.join(
                self.redfish_cache_directory,
                identity['CacheFileName']
            )
            with open(redfish_cache_resources_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(
                    json.dumps(entry, indent=4)
                )

        except BaseException:
            self.log.error('set_redfish_cache_endpoint', traceback.format_exc())
            return None

        return cache_name

    def initialize_redfish_cache(self):
        if not os.path.isfile(self.redfish_cache_filename):
            if not self.set_redfish_cache_list([]):
                return False
        return True
