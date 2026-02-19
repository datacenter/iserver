from lib import filter_helper


class K8sAuthInfo():
    def __init__(self):
        self.auth = None

    def get_auth_info(self, auth_mo):
        if auth_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            auth_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(auth_mo, 'spec')
        info['status'] = self.get(auth_mo, 'status')

        info['phase'] = self.get(auth_mo, 'status:phase')
        if info['phase'] is not None and info['phase'].lower() == 'ready':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['admin'] = self.get(auth_mo, 'spec:adminGroups', on_error=[], on_none=[])
        info['allowed'] = self.get(auth_mo, 'spec:allowedGroups', on_error=[], on_none=[])

        return info

    def get_auths_info(self, cache_enabled=True):
        if cache_enabled:
            if self.auth is not None:
                return self.auth

        managed_objects = self.get_auth_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.auth = []
        for managed_object in managed_objects:
            auth_info = {}
            auth_info['info'] = self.get_auth_info(
                managed_object
            )
            auth_info['mo'] = managed_object
            self.auth.append(
                auth_info
            )

        return self.auth

    def match_auth(self, auth_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, auth_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_auth',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_auths(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_auths = self.get_auths_info(cache_enabled=cache_enabled)
        if all_auths is None:
            return None

        auths = []

        for auth_info in all_auths:
            if not self.match_auth(auth_info['info'], object_filter):
                continue

            if return_mo:
                auths.append(
                    auth_info['mo']
                )
                continue

            auths.append(
                auth_info['info']
            )

        return auths

    def is_auth(self, name, cache_enabled=True):
        if self.get_auth(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_auth(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        auths = self.get_auths(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if auths is None:
            return None

        if len(auths) == 1:
            return auths[0]

        return None
