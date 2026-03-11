class K8sClusterRoleInfo():
    def __init__(self):
        self.cluster_role = None

    def get_cluster_role_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )

        info['role'] = self.get(managed_object, 'roleRef')
        info['subject'] = self.get(managed_object, 'subjects', on_error=[], on_none=[])
        for subject in info['subject']:
            if 'namespace' in subject:
                subject['description'] = '%s:%s/%s' % (
                    subject['kind'],
                    subject['namespace'],
                    subject['name']
                )
            else:
                subject['description'] = '%s:%s' % (
                    subject['kind'],
                    subject['name']
                )

        return info

    def get_cluster_roles(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cluster_role', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_cluster_role(self, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'cluster_role', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

    def is_cluster_role(self, name, return_mo=False, cache_enabled=True):
        if self.get_cluster_role(name, return_mo=return_mo, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_cluster_role_users(self, name, cache_enabled=True):
        binding_mo = self.get_cluster_role(name, return_mo=True, cache_enabled=cache_enabled)
        if binding_mo is None:
            return None

        users = []
        for subject_mo in binding_mo['subjects']:
            if subject_mo['kind'] == 'User':
                users.append(
                    subject_mo['name']
                )

        users = sorted(users)
        return users
