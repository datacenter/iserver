from lib import filter_helper


class K8sClusterRoleMatch():
    def __init__(self):
        pass

    def match_cluster_role(self, cluster_role_info, cluster_role_filter):
        if cluster_role_filter is None or len(cluster_role_filter) == 0:
            return True

        for ap_rule in cluster_role_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

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
