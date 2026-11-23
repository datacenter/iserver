from lib import filter_helper


class K8sOpenstackVolumePopulatorInfo():
    def __init__(self):
        self.openstack_volume_populator = None

    def get_openstack_volume_populator_info(self, openstack_volume_populator_mo):
        if openstack_volume_populator_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            openstack_volume_populator_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(openstack_volume_populator_mo, 'spec')
        info['status'] = self.get(openstack_volume_populator_mo, 'status')
        return info

    def get_openstack_volume_populators_info(self, cache_enabled=True):
        if cache_enabled:
            if self.openstack_volume_populator is not None:
                return self.openstack_volume_populator

        managed_objects = self.get_openstack_volume_populator_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.openstack_volume_populator = []
        for managed_object in managed_objects:
            openstack_volume_populator_info = {}
            openstack_volume_populator_info['info'] = self.get_openstack_volume_populator_info(
                managed_object
            )
            openstack_volume_populator_info['mo'] = managed_object
            self.openstack_volume_populator.append(
                openstack_volume_populator_info
            )

        return self.openstack_volume_populator

    def match_openstack_volume_populator(self, openstack_volume_populator_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, openstack_volume_populator_info['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, openstack_volume_populator_info['namespace']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_openstack_volume_populator',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_openstack_volume_populators(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_openstack_volume_populators = self.get_openstack_volume_populators_info(cache_enabled=cache_enabled)
        if all_openstack_volume_populators is None:
            return None

        openstack_volume_populators = []

        for openstack_volume_populator_info in all_openstack_volume_populators:
            if not self.match_openstack_volume_populator(openstack_volume_populator_info['info'], object_filter):
                continue

            if return_mo:
                openstack_volume_populators.append(
                    openstack_volume_populator_info['mo']
                )
                continue

            openstack_volume_populators.append(
                openstack_volume_populator_info['info']
            )

        return openstack_volume_populators

    def is_openstack_volume_populator(self, namespace, name, cache_enabled=True):
        if self.get_openstack_volume_populator(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_openstack_volume_populator(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        openstack_volume_populators = self.get_openstack_volume_populators(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if openstack_volume_populators is None:
            return None

        if len(openstack_volume_populators) == 1:
            return openstack_volume_populators[0]

        return None
