from lib import filter_helper


class K8sTunedInfo():
    def __init__(self):
        self.tuned = None

    def get_tuned_info(self, tuned_mo):
        if tuned_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['namespace'] = self.get(
            tuned_mo,
            'metadata:namespace'
        )

        info['name'] = self.get(
            tuned_mo,
            'metadata:name'
        )

        owner = self.get_owner(
            tuned_mo,
            'metadata:ownerReferences'
        )
        info.update(owner)

        info['profile'] = self.get(
            tuned_mo,
            'spec:profile',
            on_error=[],
            on_none=[]
        )

        info['profile_names'] = []
        for profile_info in info['profile']:
            if profile_info['name'] not in info['profile_names']:
                info['profile_names'].append(
                    profile_info['name']
                )

        info['recommend'] = self.get(
            tuned_mo,
            'spec:recommend',
            on_error=[],
            on_none=[]
        )

        info['age'] = self.convert_timestamp_to_age(
            self.get(tuned_mo, 'metadata:creationTimestamp'),
            on_error='--'
        )

        return info

    def get_tuneds_info(self, cache_enabled=True):
        if cache_enabled:
            if self.tuned is not None:
                return self.tuned

        managed_objects = self.get_tuned_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.tuned = []
        for managed_object in managed_objects:
            tuned_info = {}
            tuned_info['info'] = self.get_tuned_info(
                managed_object
            )
            tuned_info['mo'] = managed_object
            self.tuned.append(
                tuned_info
            )

        return self.tuned

    def match_tuned(self, tuned_info, tuned_filter):
        if tuned_filter is None or len(tuned_filter) == 0:
            return True

        for ap_rule in tuned_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, tuned_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, tuned_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_tuned',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_tuneds(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_tuneds = self.get_tuneds_info(cache_enabled=cache_enabled)
        if all_tuneds is None:
            return None

        tuneds = []

        for tuned_info in all_tuneds:
            if not self.match_tuned(tuned_info['info'], object_filter):
                continue

            if return_mo:
                tuneds.append(
                    tuned_info['mo']
                )
                continue

            tuneds.append(
                tuned_info['info']
            )

        return tuneds
