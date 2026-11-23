from lib import filter_helper


class OspQuotaInfo():
    def __init__(self):
        self.quota = {}

    def get_quota_info(self, quota_mo):
        if quota_mo is None:
            return None

        info = quota_mo.to_dict()
        info['__Output'] = {}

        return info

    def serialize_quota(self):
        quota = []
        for tenant_id in self.quota:
            item = self.quota[tenant_id]
            item['tenant_id'] = tenant_id
            quota.append(
                item
            )

        return quota

    def get_quotas_info(self, tenant_ids, cache_enabled=True):
        if cache_enabled:
            cache_ready = True
            for tenant_id in tenant_ids:
                if tenant_id not in self.quota or self.quota[tenant_id] is None:
                    cache_ready = False
                    break

            if cache_ready:
                return self.serialize_quota()

        managed_objects = self.get_quota_mo(tenant_ids, cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        for tenant_id in managed_objects:
            self.quota[tenant_id] = self.get_quota_info(
                managed_objects[tenant_id]
            )

        self.log.osp_mo(
            'quotas',
            self.serialize_quota()
        )

        return self.serialize_quota()

    def match_quota(self, quota_info, quota_filter):
        if quota_filter is None or len(quota_filter) == 0:
            return True

        for ap_rule in quota_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, quota_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in quota_info:
                    if not filter_helper.match_string(value, quota_info['tenant_name']):
                        return False

            if not key_found:
                self.log.error(
                    'match_quota',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_quotas(self, object_filter=None, tenant_info=False, cache_enabled=True):
        tenant_ids = self.get_tenant_ids()
        if tenant_ids is None:
            return None

        all_quotas = self.get_quotas_info(tenant_ids, cache_enabled=cache_enabled)
        if all_quotas is None:
            return None

        quotas = []

        for quota_info in all_quotas:
            if not self.match_quota(quota_info, object_filter):
                continue

            if tenant_info:
                quota_info['tenant_name'] = self.get_tenant_name(
                    quota_info['tenant_id'],
                    cache_enabled=cache_enabled
                )

                if not self.match_quota(quota_info, object_filter):
                    continue

            quotas.append(
                quota_info
            )

        if tenant_info:
            quotas = sorted(
                quotas,
                key=lambda i: i['tenant_name']
            )

        return quotas
