import copy
from lib import log_helper
from lib import file_helper
from lib import ip_helper
from lib.nexus import settings as nexus_settings
from lib.nexus import nxapi


class NexusVersion():
    def __init__(self):
        self.nexus_version = None
        self.nexus_sw = None

    def load_pre_nexus_version(self):
        self.nexus_version = self.get_pre_cache('nexus', 'version')
        if self.nexus_version is None:
            return False
        self.analyze_nexus_sw()
        return True

    def set_post_nexus_version(self):
        return self.set_post_cache('nexus-version', self.nexus_version)

    def load_post_nexus_version(self):
        self.nexus_version = self.get_post_cache('nexus-version')
        if self.nexus_version is None:
            return False
        self.analyze_nexus_sw()
        return True

    def get_nexus_version(self):
        info = copy.deepcopy(self.nexus_version)
        return info

    def analyze_nexus_sw(self):
        self.nexus_sw = {}
        for nexus_device_name in self.nexus_version:
            self.nexus_sw[nexus_device_name] = None
            if self.nexus_version[nexus_device_name] is not None:
                self.nexus_sw[nexus_device_name] = self.nexus_version[nexus_device_name]['nxos_ver_str']

    def prepare_nexus_version(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_version = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus version: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_version:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-version' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_version[nexus_device['name']] = cache
                    self.my_output.debug('L3 Cache hit')
                    continue

            self.my_output.debug('Cache miss')

            if 'handler' in nexus_device:
                nexus_handler = nexus_device['handler']
            else:
                nexus_handler = nxapi.NxApi(
                    nexus_device['ip'],
                    nexus_device['username'],
                    nexus_device['password'],
                    nexus_device['nxapi'],
                    name=nexus_device['name'],
                    log_id=self.log_id,
                    cache_enabled=False,
                    debug=True,
                    paranoid=self.paranoid
                )

            version = nexus_handler.get_version()
            if version is None:
                self.my_output.error('Version failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_version[nexus_device['name']] = version

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-version' % (nexus_device['name']),
                self.nexus_version[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        self.analyze_nexus_sw()
        return success

    def run_nexus_version(self):
        if not self.set_post_nexus_version():
            return False

        return True
