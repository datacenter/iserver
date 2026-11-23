import copy
from lib.nexus import nxapi


class NexusVrf():
    def __init__(self):
        self.nexus_vrf = None

    def load_pre_nexus_vrf(self):
        self.nexus_vrf = self.get_pre_cache('nexus', 'vrf')
        if self.nexus_vrf is None:
            return False
        return True

    def set_post_nexus_vrf(self):
        return self.set_post_cache('nexus-vrf', self.nexus_vrf)

    def load_post_nexus_vrf(self):
        self.nexus_vrf = self.get_post_cache('nexus-vrf')
        if self.nexus_vrf is None:
            return False
        return True

    def get_nexus_vrf(self):
        info = copy.deepcopy(self.nexus_vrf)
        return info

    def prepare_nexus_vrf(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_vrf = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus vrf: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_vrf:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-vrf' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_vrf[nexus_device['name']] = cache
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

            vrf = nexus_handler.get_vrfs()
            if vrf is None:
                self.my_output.error('VRF failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_vrf[nexus_device['name']] = vrf

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-vrf' % (nexus_device['name']),
                self.nexus_vrf[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def run_nexus_vrf(self):
        if not self.set_post_nexus_vrf():
            return False

        return True
