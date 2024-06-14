from lib import filter_helper


class OspUserInfo():
    def __init__(self):
        self.user = None

    def get_user_info(self, user_mo):
        if user_mo is None:
            return None

        properties = user_mo.to_dict()

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'name',
            'domain_id',
            'enabled',
            'password_expires_at',
            'default_project_id'
        ]

        for key in keys:
            info[key] = None
            if key in properties:
                info[key] = properties[key]

        for key in properties['options']:
            info[key] = properties['options'][key]

        if info['enabled']:
            info['enabledTick'] = '\u2713'
            info['__Output']['enabledTick'] = 'Green'
        else:
            info['enabledTick'] = '\u2717'
            info['__Output']['enabledTick'] = 'Red'

        if info['password_expires_at'] is not None:
            info['expiresTick'] = '\u2713'
            info['__Output']['enabledTick'] = 'Red'
        else:
            info['expiresTick'] = '--'

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
            user_info = self.get_user_info(
                managed_object
            )
            self.user.append(
                user_info
            )

        self.log.osp_mo(
            'users',
            self.user
        )

        return self.user

    def match_user(self, user_info, user_filter):
        if user_filter is None or len(user_filter) == 0:
            return True

        for ap_rule in user_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, user_info['id']):
                    return False

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

    def get_users(self, object_filter=None, tenant_info=False, role_info=False, cache_enabled=True):
        all_users = self.get_users_info(cache_enabled=cache_enabled)
        if all_users is None:
            return None

        users = []

        for user_info in all_users:
            if not self.match_user(user_info, object_filter):
                continue

            if tenant_info:
                user_info['default_project_name'] = None
                if user_info['default_project_id'] is not None:
                    user_info['default_project_name'] = self.get_tenant_name(
                        user_info['default_project_id'],
                        cache_enabled=cache_enabled

                    )

                if not self.match_subnet(user_info, object_filter):
                    continue

            if role_info:
                pass

            users.append(
                user_info
            )

        users = sorted(
            users,
            key=lambda i: i['name']
        )

        return users
