from lib import filter_helper


class K8sVirtualMachinePreferenceInfo():
    def __init__(self):
        self.virtual_machine_preference = None

    def get_virtual_machine_preference_info(self, virtual_machine_preference_mo):
        if virtual_machine_preference_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_preference_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_preferences_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_preference is not None:
                return self.virtual_machine_preference

        managed_objects = self.get_virtual_machine_preference_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_preference = []
        for managed_object in managed_objects:
            virtual_machine_preference_info = {}
            virtual_machine_preference_info['info'] = self.get_virtual_machine_preference_info(
                managed_object
            )
            virtual_machine_preference_info['mo'] = managed_object
            self.virtual_machine_preference.append(
                virtual_machine_preference_info
            )

        return self.virtual_machine_preference

    def match_virtual_machine_preference(self, virtual_machine_preference_info, virtual_machine_preference_filter):
        if virtual_machine_preference_filter is None or len(virtual_machine_preference_filter) == 0:
            return True

        for ap_rule in virtual_machine_preference_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_preference',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_preferences(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_preferences = self.get_virtual_machine_preferences_info(cache_enabled=cache_enabled)
        if all_virtual_machine_preferences is None:
            return None

        virtual_machine_preferences = []

        for virtual_machine_preference_info in all_virtual_machine_preferences:
            if not self.match_virtual_machine_preference(virtual_machine_preference_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_preferences.append(
                    virtual_machine_preference_info['mo']
                )
                continue

            virtual_machine_preferences.append(
                virtual_machine_preference_info['info']
            )

        return virtual_machine_preferences
