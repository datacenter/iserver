from lib import filter_helper


class K8sOvirtVolumePopulatorInfo():
    def __init__(self):
        self.ovirt_volume_populator = None

    def get_ovirt_volume_populator_info(self, ovirt_volume_populator_mo):
        if ovirt_volume_populator_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ovirt_volume_populator_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(ovirt_volume_populator_mo, 'spec')
        info['status'] = self.get(ovirt_volume_populator_mo, 'status')
        return info

    def get_ovirt_volume_populators_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ovirt_volume_populator is not None:
                return self.ovirt_volume_populator

        managed_objects = self.get_ovirt_volume_populator_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ovirt_volume_populator = []
        for managed_object in managed_objects:
            ovirt_volume_populator_info = {}
            ovirt_volume_populator_info['info'] = self.get_ovirt_volume_populator_info(
                managed_object
            )
            ovirt_volume_populator_info['mo'] = managed_object
            self.ovirt_volume_populator.append(
                ovirt_volume_populator_info
            )

        return self.ovirt_volume_populator

    def match_ovirt_volume_populator(self, ovirt_volume_populator_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, ovirt_volume_populator_info['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, ovirt_volume_populator_info['namespace']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_ovirt_volume_populator',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ovirt_volume_populators(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_ovirt_volume_populators = self.get_ovirt_volume_populators_info(cache_enabled=cache_enabled)
        if all_ovirt_volume_populators is None:
            return None

        ovirt_volume_populators = []

        for ovirt_volume_populator_info in all_ovirt_volume_populators:
            if not self.match_ovirt_volume_populator(ovirt_volume_populator_info['info'], object_filter):
                continue

            if return_mo:
                ovirt_volume_populators.append(
                    ovirt_volume_populator_info['mo']
                )
                continue

            ovirt_volume_populators.append(
                ovirt_volume_populator_info['info']
            )

        return ovirt_volume_populators

    def is_ovirt_volume_populator(self, namespace, name, cache_enabled=True):
        if self.get_ovirt_volume_populator(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_ovirt_volume_populator(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        ovirt_volume_populators = self.get_ovirt_volume_populators(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if ovirt_volume_populators is None:
            return None

        if len(ovirt_volume_populators) == 1:
            return ovirt_volume_populators[0]

        return None
