import copy
from lib.nexus import nxapi


class NexusFeature():
    def __init__(self):
        self.nexus_feature = None

    def load_pre_nexus_feature(self):
        self.nexus_feature = self.get_pre_cache('nexus', 'feature')
        if self.nexus_feature is None:
            return False
        return True

    def set_post_nexus_feature(self):
        return self.set_post_cache('nexus-feature', self.nexus_feature)

    def load_post_nexus_feature(self):
        self.nexus_feature = self.get_post_cache('nexus-feature')
        if self.nexus_feature is None:
            return False
        return True

    def get_enabled_feature_names(self, device_names):
        features = []
        for device_name in device_names:
            for feature in self.nexus_feature[device_name]:
                if feature['status'] == 'enabled':
                    if feature['name'] not in features:
                        features.append(
                            feature['name']
                        )

        features = sorted(features)
        return features

    def get_nexus_feature(self):
        info = copy.deepcopy(self.nexus_feature)
        return info

    def prepare_nexus_feature(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_feature = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus feature: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_feature:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-feature' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_feature[nexus_device['name']] = cache
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

            feature = nexus_handler.get_features()
            if feature is None:
                self.my_output.error('Feature failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_feature[nexus_device['name']] = feature

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-feature' % (nexus_device['name']),
                self.nexus_feature[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        return success

    def run_nexus_feature(self):
        if not self.set_post_nexus_feature():
            return False

        return True
