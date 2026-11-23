from lib import filter_helper


class OspRoleInfo():
    def __init__(self):
        self.role = None

    def get_role_info(self, role_mo):
        if role_mo is None:
            return None

        info = role_mo.to_dict()
        info['__Output'] = {}

        return info

    def get_roles_info(self, cache_enabled=True):
        if cache_enabled:
            if self.role is not None:
                return self.role

        managed_objects = self.get_role_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.role = []
        for managed_object in managed_objects:
            role_info = self.get_role_info(
                managed_object
            )
            self.role.append(
                role_info
            )

        self.log.osp_mo(
            'roles',
            self.role
        )

        return self.role

    def match_role(self, role_info, role_filter):
        if role_filter is None or len(role_filter) == 0:
            return True

        for ap_rule in role_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_role',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_roles(self, object_filter=None, cache_enabled=True):
        all_roles = self.get_roles_info(cache_enabled=cache_enabled)
        if all_roles is None:
            return None

        roles = []

        for role_info in all_roles:
            if not self.match_role(role_info, object_filter):
                continue

            roles.append(
                role_info
            )

        return roles
