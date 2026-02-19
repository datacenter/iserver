from lib import filter_helper


class K8sUserInfo():
    def __init__(self):
        self.user = None

    def get_user_info(self, user_mo):
        if user_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            user_mo
        )
        info.update(metadata_info)

        info['groups'] = self.get(user_mo, 'groups')
        info['identities'] = self.get(user_mo, 'identities')
        return info

    def get_users_info(self, cache_enabled=True):
        if cache_enabled:
            if self.user is not None:
                return self.user

        managed_objects = self.get_user_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.user = []
        for managed_object in managed_objects:
            user_info = {}
            user_info['info'] = self.get_user_info(
                managed_object
            )
            user_info['mo'] = managed_object
            self.user.append(
                user_info
            )

        return self.user

    def match_user(self, user_info, user_filter):
        if user_filter is None or len(user_filter) == 0:
            return True

        for ap_rule in user_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, user_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_user',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_users(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_users = self.get_users_info(cache_enabled=cache_enabled)
        if all_users is None:
            return None

        users = []

        for user_info in all_users:
            if not self.match_user(user_info['info'], object_filter):
                continue

            if return_mo:
                users.append(
                    user_info['mo']
                )
                continue

            users.append(
                user_info['info']
            )

        return users

    def get_user(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        users = self.get_users(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if users is None:
            return None

        if len(users) == 1:
            return users[0]

        return None

    def is_user(self, name, return_mo=False, cache_enabled=True):
        if self.get_user(name, return_mo=return_mo, cache_enabled=cache_enabled) is None:
            return False
        return True
