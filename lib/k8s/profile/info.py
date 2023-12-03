from lib import filter_helper


class K8sProfileInfo():
    def __init__(self):
        self.profile = None

    def get_profile_info(self, profile_mo):
        if profile_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            profile_mo
        )
        info.update(metadata_info)

        info['uid'] = self.get(
            profile_mo,
            'metadata:uid'
        )

        info['profile'] = self.get(
            profile_mo,
            'spec:config:tunedProfile'
        )

        info['bootcmdline'] = self.get(
            profile_mo,
            'status:bootcmdline'
        )

        if info['bootcmdline'] is not None and len(info['bootcmdline']) > 0:
            info['bootcmdlineTick'] = '\u2713'
            info['__Output']['bootcmdlineTick'] = 'Green'
        else:
            info['bootcmdlineTick'] = '--'

        info['applied'] = False
        info['appliedTick'] = '--'

        info['degraded'] = False
        info['degradedTick'] = '--'

        info['error'] = None

        conditions = self.get(
            profile_mo,
            'status:conditions',
            on_error=[],
            on_none=[]
        )
        for condition in conditions:
            if condition['type'] == 'Applied':
                if condition['status'] == 'True':
                    info['applied'] = True
                    info['appliedTick'] = '\u2713'
                    info['__Output']['appliedTick'] = 'Green'
                if condition['status'] == 'False':
                    info['applied'] = False
                    info['appliedTick'] = '\u2717'
                    info['__Output']['appliedTick'] = 'Red'
            if condition['type'] == 'Degraded':
                if condition['status'] == 'True':
                    info['degraded'] = True
                    info['degradedTick'] = '\u2713'
                    info['__Output']['degradedTick'] = 'Red'
                    if len(condition['message']) > 0:
                        info['error'] = condition['message']
                if condition['status'] == 'False':
                    info['degraded'] = False
                    info['degradedTick'] = '\u2717'
                    info['__Output']['degradedTick'] = 'Green'

        if info['error'] is not None:
            info['errorTick'] = '\u2713'
            info['__Output']['errorTick'] = 'Red'
        else:
            info['errorTick'] = '--'

        return info

    def get_profiles_info(self, cache_enabled=True):
        if cache_enabled:
            if self.profile is not None:
                return self.profile

        managed_objects = self.get_profile_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.profile = []
        for managed_object in managed_objects:
            profile_info = {}
            profile_info['info'] = self.get_profile_info(
                managed_object
            )
            profile_info['mo'] = managed_object
            self.profile.append(
                profile_info
            )

        return self.profile

    def match_profile(self, profile_info, profile_filter):
        if profile_filter is None or len(profile_filter) == 0:
            return True

        for ap_rule in profile_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, profile_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (profile_info['namespace'], profile_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_profile',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_profiles(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_profiles = self.get_profiles_info(cache_enabled=cache_enabled)
        if all_profiles is None:
            return None

        profiles = []

        for profile_info in all_profiles:
            if not self.match_profile(profile_info['info'], object_filter):
                continue

            if return_mo:
                profiles.append(
                    profile_info['mo']
                )
                continue

            profiles.append(
                profile_info['info']
            )

        return profiles
