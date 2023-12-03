from lib import filter_helper


class OspTenantInfo():
    def __init__(self):
        self.tenant = None

    def get_tenant_info(self, tenant_mo):
        if tenant_mo is None:
            return None

        info = tenant_mo.to_dict()
        info['__Output'] = {}

        return info

    def get_tenants_info(self, cache_enabled=True):
        if cache_enabled:
            if self.tenant is not None:
                return self.tenant

        managed_objects = self.get_tenant_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.tenant = []
        for managed_object in managed_objects:
            tenant_info = self.get_tenant_info(
                managed_object
            )
            self.tenant.append(
                tenant_info
            )

        self.log.osp_mo(
            'tenants',
            self.tenant
        )

        return self.tenant

    def match_tenant(self, tenant_info, tenant_filter):
        if tenant_filter is None or len(tenant_filter) == 0:
            return True

        for ap_rule in tenant_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, tenant_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, tenant_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_tenant',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_tenants(self, object_filter=None, cache_enabled=True):
        all_tenants = self.get_tenants_info(cache_enabled=cache_enabled)
        if all_tenants is None:
            return None

        tenants = []

        for tenant_info in all_tenants:
            if not self.match_tenant(tenant_info, object_filter):
                continue

            tenants.append(
                tenant_info
            )

        return tenants

    def get_tenant_ids(self, cache_enabled=True):
        tenants = self.get_tenants(cache_enabled=cache_enabled)
        if tenants is None:
            return None

        ids = []
        for tenant in tenants:
            ids.append(
                tenant['id']
            )

        return ids

    def get_tenant(self, tenant_id=None, tenant_name=None, cache_enabled=True):
        object_filter = []
        if tenant_id is not None:
            object_filter.append(
                'id:%s' % (tenant_id)
            )
        if tenant_name is not None:
            object_filter.append(
                'name:%s' % (tenant_name)
            )

        tenants = self.get_tenants(
            object_filter=object_filter,
            cache_enabled=cache_enabled
        )
        if tenants is None or len(tenants) != 1:
            return None

        return tenants[0]

    def get_tenant_name(self, tenant_id, cache_enabled=True):
        tenant_info = self.get_tenant(
            tenant_id=tenant_id,
            cache_enabled=cache_enabled
        )
        if tenant_info is None:
            return None
        return tenant_info['name']
