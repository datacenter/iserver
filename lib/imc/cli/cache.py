import os
import json
import time

from lib import file_helper
from lib import log_helper

from lib.imc import settings


class ImcCliCache():
    def __init__(self, endpoint_id, cache_ttl, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.cache_ttl = cache_ttl
        self.cache_endpoint_id = endpoint_id
        self.endpoint_settings_handler = settings.ImcEndpointSettings(log_id=log_id)

    def get_icm_cli_cache_entry(self, cache_entry_name):
        if self.cache_ttl < 0:
            return None

        directory_name = self.endpoint_settings_handler.get_endpoint_directory(
            self.cache_endpoint_id
        )

        filename = os.path.join(
            directory_name,
            'cli_%s' % (cache_entry_name)
        )

        cache_entry = file_helper.get_file_json(
            filename
        )
        if cache_entry is None:
            return None

        for key in ['data', 'timestamp']:
            if key not in cache_entry:
                self.log.error('get_icm_cli_cache_entry', 'Invalid cache content: %s' % (filename))
                return None

        if self.cache_ttl > 0:
            entry_ttl = int(time.time()) - cache_entry['timestamp']
            if entry_ttl > self.cache_ttl:
                return None

        return cache_entry['data']

    def set_imc_cli_cache_entry(self, cache_entry_name, data):
        directory_name = self.endpoint_settings_handler.get_endpoint_directory(
            self.cache_endpoint_id
        )

        if not os.path.isdir(directory_name):
            os.makedirs(
                directory_name,
                exist_ok=True
            )

        filename = os.path.join(
            directory_name,
            'cli_%s' % (cache_entry_name)
        )

        content = {}
        content['timestamp'] = int(time.time())
        content['data'] = data

        success = file_helper.set_file_json(
            filename,
            content
        )
        if not success:
            self.log.error('set_imc_cli_cache_entry', 'Cache set failed: %s' % (filename))
            return False

        return True
