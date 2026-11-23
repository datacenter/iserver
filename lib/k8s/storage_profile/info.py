from lib import filter_helper


class K8sStorageProfileInfo():
    def __init__(self):
        self.storage_profile = None

    def get_storage_profile_info(self, storage_profile_mo):
        if storage_profile_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_profile_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(storage_profile_mo, 'spec')
        info['status'] = self.get(storage_profile_mo, 'status')
        return info

    def get_storage_profiles_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_profile is not None:
                return self.storage_profile

        managed_objects = self.get_storage_profile_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_profile = []
        for managed_object in managed_objects:
            storage_profile_info = {}
            storage_profile_info['info'] = self.get_storage_profile_info(
                managed_object
            )
            storage_profile_info['mo'] = managed_object
            self.storage_profile.append(
                storage_profile_info
            )

        return self.storage_profile

    def match_storage_profile(self, storage_profile_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, storage_profile_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_storage_profile',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_profiles(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_storage_profiles = self.get_storage_profiles_info(cache_enabled=cache_enabled)
        if all_storage_profiles is None:
            return None

        storage_profiles = []

        for storage_profile_info in all_storage_profiles:
            if not self.match_storage_profile(storage_profile_info['info'], object_filter):
                continue

            if return_mo:
                storage_profiles.append(
                    storage_profile_info['mo']
                )
                continue

            storage_profiles.append(
                storage_profile_info['info']
            )

        return storage_profiles

    def is_storage_profile(self, name, cache_enabled=True):
        if self.get_storage_profile(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_storage_profile(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        storage_profiles = self.get_storage_profiles(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if storage_profiles is None:
            return None

        if len(storage_profiles) == 1:
            return storage_profiles[0]

        return None
