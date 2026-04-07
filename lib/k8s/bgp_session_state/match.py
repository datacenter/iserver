from lib import filter_helper
from lib import ip_helper


class K8sBgpSessionStateMatch():
    def __init__(self):
        pass

    def match_bgp_session_state(self, info, filter_rules):
        if filter_rules is None or len(filter_rules) == 0:
            return True

        for ap_rule in filter_rules:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'node':
                key_found = True
                if not filter_helper.match_string(value, info['status']['node']):
                    return False

            if key == 'nodes':
                key_found = True
                value_found = False
                for name in value.split(','):
                    if filter_helper.match_string(name, info['status']['node']):
                        value_found = True
                        break

                if not value_found:
                    return False

            if key == 'peer':
                key_found = True
                if not filter_helper.match_string(value, info['status']['peer']):
                    return False

            if key == 'peers':
                key_found = True
                value_found = False
                for name in value.split(','):
                    if filter_helper.match_string(name, info['status']['peer']):
                        value_found = True
                        break

                if not value_found:
                    return False
                                
            if not key_found:
                self.log.error(
                    'match_bgp_session_state',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cluster_roles(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cluster_roles = self.get_cluster_roles_info(cache_enabled=cache_enabled)
        if all_cluster_roles is None:
            return None

        cluster_roles = []

        for info in all_cluster_roles:
            if not self.match_cluster_role(info['info'], object_filter):
                continue

            if return_mo:
                cluster_roles.append(
                    info['mo']
                )
                continue

            cluster_roles.append(
                info['info']
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

        success = self.create_resource(body)
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

        return self.replace_resource(crb_mo)

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
        return self.replace_resource(crb_mo)
