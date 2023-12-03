import os
import json
import time

from lib import log_helper

from lib.intersight.settings import IntersightSettings


class IntersightCache(IntersightSettings):
    def __init__(self, iaccount, log_id=None):
        IntersightSettings.__init__(self, log_id=log_id)

        self.iaccount = iaccount
        self.log = log_helper.Log(log_id=log_id)

        self.intersight_settings = self.get_intersight_settings()
        if self.intersight_settings is None:
            raise ValueError('Intersight settings read failed')

        self.intersight_cache_directory = self.intersight_settings['ComputeCacheDirectory']
        self.intersight_cache_ttl = self.intersight_settings['CacheTtl']

    def is_intersight_cache(self, cache_entry_name, subdirectory=None, cache_ttl=None):
        if self.get_intersight_cache_entry(cache_entry_name, subdirectory=subdirectory, cache_ttl=cache_ttl) is None:
            return False
        return True

    def get_intersight_cache_entry(self, cache_entry_name, subdirectory=None, check_ttl=True, cache_ttl=None):
        directory_name = self.intersight_cache_directory
        if subdirectory is not None:
            directory_name = os.path.join(
                directory_name,
                subdirectory
            )

        filename = os.path.join(
            directory_name,
            cache_entry_name
        )

        if not os.path.isfile(filename):
            return None

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                cache_entry = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_intersight_cache_entry', 'Cache read failed: %s' % (filename))
            return None

        for key in ['data', 'timestamp']:
            if key not in cache_entry:
                self.log.error('get_intersight_cache_entry', 'Invalid cache content: %s' % (filename))
                return None

        if check_ttl:
            if cache_ttl is None:
                if self.intersight_cache_ttl > 0:
                    entry_ttl = int(time.time()) - cache_entry['timestamp']
                    if entry_ttl > self.intersight_cache_ttl:
                        return None

            if cache_ttl is not None:
                if cache_ttl > 0:
                    entry_ttl = int(time.time()) - cache_entry['timestamp']
                    if entry_ttl > cache_ttl:
                        return None

        return cache_entry['data']

    def set_intersight_cache_entry(self, cache_entry_name, data, subdirectory=None):
        directory_name = self.intersight_cache_directory
        if subdirectory is not None:
            directory_name = os.path.join(
                directory_name,
                subdirectory
            )

        if os.path.isfile(directory_name):
            os.remove(directory_name)

        if not os.path.isdir(directory_name):
            os.makedirs(
                directory_name,
                exist_ok=True
            )

        filename = os.path.join(
            directory_name,
            cache_entry_name
        )

        content = {}
        content['timestamp'] = int(time.time())
        content['data'] = data

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(
                    json.dumps(
                        content,
                        indent=4
                    )
                )

        except BaseException:
            self.log.error('set_intersight_cache_entry', 'Cache set failed: %s' % (filename))
            return False

        return True
