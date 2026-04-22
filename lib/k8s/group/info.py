class K8sGroupInfo():
    def __init__(self):
        self.group = None

    def get_group_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['users'] = self.get(managed_object, 'users', on_error=[], on_none=[])
        info['ldap'] = self.get(info, 'label:openshift.io/ldap.host')

        info['isLdap'] = False
        info['ldapTick'] = ''
        if info['ldap'] is not None:
            info['isLdap'] = True
            info['ldapTick'] = '\u2713'

        info['ldapT'] = []
        ldap = [
            'openshift.io/ldap.uid',
            'openshift.io/ldap.sync-time'
        ]
        if info['ldap'] is not None:
            info['ldapT'].append(info['ldap'])
        for key in ldap:
            if key in info['annotation']:
                info['ldapT'].append(
                    info['annotation'][key]
                )

        return info

    def add_groups_user(self, infos, cache_enabled=False):
        users = self.get_users(cache_enabled=cache_enabled)
        for info in infos:
            info['info']['usersT'] = []
            if users is None:
                continue

            for group_user in info['info']['users']:
                found = False
                for user in users:
                    if group_user == user['name']:
                        found = True
                        break

                if found:
                    info['info']['usersT'].append('[*] %s' % (group_user))
                else:
                    info['info']['usersT'].append(group_user)

        return infos

    def get_groups(self, object_filter=None, user_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'group', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            add=dict(user=user_info)
        )
        return infos
    
    def get_group(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'group', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_group(self, name, return_mo=False, cache_enabled=True, optimized=True):
        if self.get_group(name, return_mo=return_mo, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True
