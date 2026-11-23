from lib import filter_helper


class K8sResourceQuotaInfo():
    def __init__(self):
        self.resource_quota = None

    def get_resource_quota_info(self, resource_quota_mo):
        if resource_quota_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            resource_quota_mo
        )
        info.update(metadata_info)

        return info

    def get_resource_quotas_info(self, cache_enabled=True):
        if cache_enabled:
            if self.resource_quota is not None:
                return self.resource_quota

        managed_objects = self.get_resource_quota_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.resource_quota = []
        for managed_object in managed_objects:
            resource_quota_info = {}
            resource_quota_info['info'] = self.get_resource_quota_info(
                managed_object
            )
            resource_quota_info['mo'] = managed_object
            self.resource_quota.append(
                resource_quota_info
            )

        return self.resource_quota

    def match_resource_quota(self, resource_quota_info, resource_quota_filter):
        if resource_quota_filter is None or len(resource_quota_filter) == 0:
            return True

        for ap_rule in resource_quota_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, resource_quota_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (resource_quota_info['namespace'], resource_quota_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_resource_quota',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_resource_quotas(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_resource_quotas = self.get_resource_quotas_info(cache_enabled=cache_enabled)
        if all_resource_quotas is None:
            return None

        resource_quotas = []

        for resource_quota_info in all_resource_quotas:
            if not self.match_resource_quota(resource_quota_info['info'], object_filter):
                continue

            if return_mo:
                resource_quotas.append(
                    resource_quota_info['mo']
                )
                continue

            resource_quotas.append(
                resource_quota_info['info']
            )

        resource_quotas = sorted(
            resource_quotas,
            key=lambda i: (
                i['namespace'],
                i['name']
            )
        )

        return resource_quotas
