from lib import filter_helper


class K8sClusterRoleBindingInfo():
    def __init__(self):
        self.cluster_role_binding = None

    def get_cluster_role_binding_info(self, cluster_role_binding_mo):
        if cluster_role_binding_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cluster_role_binding_mo
        )
        info.update(metadata_info)

        info['role'] = self.get(cluster_role_binding_mo, 'roleRef')
        info['subject'] = self.get(cluster_role_binding_mo, 'subjects', on_error=[], on_none=[])
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

    def get_cluster_role_bindings_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_role_binding is not None:
                return self.cluster_role_binding

        managed_objects = self.get_cluster_role_binding_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cluster_role_binding = []
        for managed_object in managed_objects:
            cluster_role_binding_info = {}
            cluster_role_binding_info['info'] = self.get_cluster_role_binding_info(
                managed_object
            )
            cluster_role_binding_info['mo'] = managed_object
            self.cluster_role_binding.append(
                cluster_role_binding_info
            )

        return self.cluster_role_binding

    def match_cluster_role_binding(self, cluster_role_binding_info, cluster_role_binding_filter):
        if cluster_role_binding_filter is None or len(cluster_role_binding_filter) == 0:
            return True

        for ap_rule in cluster_role_binding_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cluster_role_binding_info['name']):
                    return False

            if key == 'role':
                key_found = True
                if not filter_helper.match_string(value, cluster_role_binding_info['role']):
                    return False

            if key == 'subject':
                key_found = True
                found = False
                for subject in cluster_role_binding_info['subject']:
                    if filter_helper.match_string(value, subject['description']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_cluster_role_binding',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cluster_role_bindings(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cluster_role_bindings = self.get_cluster_role_bindings_info(cache_enabled=cache_enabled)
        if all_cluster_role_bindings is None:
            return None

        cluster_role_bindings = []

        for cluster_role_binding_info in all_cluster_role_bindings:
            if not self.match_cluster_role_binding(cluster_role_binding_info['info'], object_filter):
                continue

            if return_mo:
                cluster_role_bindings.append(
                    cluster_role_binding_info['mo']
                )
                continue

            cluster_role_bindings.append(
                cluster_role_binding_info['info']
            )

        return cluster_role_bindings
