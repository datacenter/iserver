import copy
from lib.nexus import nxapi


class NexusVlan():
    def __init__(self):
        self.nexus_vlan = None

    def load_pre_nexus_vlan(self):
        self.nexus_vlan = self.get_pre_cache('nexus', 'vlan')
        if self.nexus_vlan is None:
            return False
        self.analyze_nexus_sw()
        return True

    def set_post_nexus_vlan(self):
        return self.set_post_cache('nexus-vlan', self.nexus_vlan)

    def load_post_nexus_vlan(self):
        self.nexus_vlan = self.get_post_cache('nexus-vlan')
        if self.nexus_vlan is None:
            return False
        self.analyze_nexus_sw()
        return True

    def get_nexus_vlan(self):
        info = copy.deepcopy(self.nexus_vlan)
        return info

    def prepare_nexus_vlan(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_vlan = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus vlan: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_vlan:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-vlan' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_vlan[nexus_device['name']] = cache
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

            vlan = nexus_handler.get_vlans()
            if vlan is None:
                self.my_output.error('VLAN failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_vlan[nexus_device['name']] = vlan

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-vlan' % (nexus_device['name']),
                self.nexus_vlan[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def run_nexus_vlan(self):
        if not self.set_post_nexus_vlan():
            return False

        return True
