from lib import filter_helper
from lib import ip_helper


class K8sClusterRoleInfo():
    def __init__(self):
        self.cluster_role = None

    def get_cluster_role_info(self, cluster_role_mo):
        if cluster_role_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cluster_role_mo
        )
        info.update(metadata_info)

        info['role'] = self.get(cluster_role_mo, 'roleRef')
        info['subject'] = self.get(cluster_role_mo, 'subjects', on_error=[], on_none=[])
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

    def get_cluster_roles_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_role is not None:
                return self.cluster_role

        managed_objects = self.get_cluster_role_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cluster_role = []
        for managed_object in managed_objects:
            cluster_role_info = {}
            cluster_role_info['info'] = self.get_cluster_role_info(
                managed_object
            )
            cluster_role_info['mo'] = managed_object
            self.cluster_role.append(
                cluster_role_info
            )

        return self.cluster_role

    def match_cluster_role(self, cluster_role_info, cluster_role_filter):
        if cluster_role_filter is None or len(cluster_role_filter) == 0:
            return True

        for ap_rule in cluster_role_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cluster_role_info['name']):
                    return False

            if key == 'role':
                key_found = True
                if not filter_helper.match_string(value, cluster_role_info['role']['name']):
                    return False

            if key == 'subject':
                key_found = True
                found = False
                for subject in cluster_role_info['subject']:
                    if filter_helper.match_string(value, subject['description']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_cluster_role',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cluster_roles(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cluster_roles = self.get_cluster_roles_info(cache_enabled=cache_enabled)
        if all_cluster_roles is None:
            return None

        cluster_roles = []

        for cluster_role_info in all_cluster_roles:
            if not self.match_cluster_role(cluster_role_info['info'], object_filter):
                continue

            if return_mo:
                cluster_roles.append(
                    cluster_role_info['mo']
                )
                continue

            cluster_roles.append(
                cluster_role_info['info']
            )

        return cluster_roles

    def get_cluster_role(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        crbs = self.get_cluster_roles(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if crbs is None:
            return None

        if len(crbs) == 1:
            return crbs[0]

        return None

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

    def add_service_account_cluster_role(self, name, cluster_role_name, sa_name, sa_namespace):
        if self.is_cluster_role(name, cache_enabled=False):
            name = '%s-%s' % (name, ip_helper.get_short_uuid())

        body = {}
        body['apiVersion'] = 'rbac.authorization.k8s.io/v1'
        body['kind'] = 'ClusterRole'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['roleRef'] = {}
        body['roleRef']['apiGroup'] = 'rbac.authorization.k8s.io'
        body['roleRef']['kind'] = 'ClusterRole'
        body['roleRef']['name'] = cluster_role_name
        body['subjects'] = []

        subject = {}
        subject['kind'] = 'ServiceAccount'
        subject['name'] = sa_name
        subject['namespace'] = sa_namespace
        body['subjects'].append(
            subject
        )

        success = self.create_cluster_role_mo(body)
        if not success:
            return None

        return name

    def add_user_subject_cluster_role(self, name, username):
        crb_mo = self.get_cluster_role(name, return_mo=True, cache_enabled=False)
        if crb_mo is None:
            self.log.error(
                'add_user_subject_cluster_role',
                'Crb not found: %s' % (name)
            )
            return False

        for subject_mo in crb_mo['subjects']:
            if subject_mo['kind'] != 'User':
                continue

            if subject_mo['name'] == username:
                return True

        subject_mo = {}
        subject_mo['apiGroup'] = 'rbac.authorization.k8s.io'
        subject_mo['kind'] = 'User'
        subject_mo['name'] = username
        crb_mo['subjects'].append(
            subject_mo
        )

        return self.update_cluster_role_mo(crb_mo)

    def del_user_subject_cluster_role(self, name, username):
        crb_mo = self.get_cluster_role(name, return_mo=True, cache_enabled=False)
        if crb_mo is None:
            self.log.error(
                'del_user_subject_cluster_role',
                'Crb not found: %s' % (name)
            )
            return False

        new_subjects = []

        for subject_mo in crb_mo['subjects']:
            if subject_mo['kind'] != 'User':
                new_subjects.append(subject_mo)
                continue

            if subject_mo['name'] != username:
                new_subjects.append(subject_mo)
                continue

        crb_mo['subjects'] = new_subjects
        return self.update_cluster_role_mo(crb_mo)
