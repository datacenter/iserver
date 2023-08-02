from lib import filter_helper


class TenantInfo():
    def __init__(self):
        self.tenant = None

    def get_tenant_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'lcOwn',
            'name',
            'userdom'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        return info

    def get_tenants_info(self):
        if self.tenant is not None:
            return self.tenant

        managed_objects = self.get_tenant_mo()
        if managed_objects is None:
            return None

        self.tenant = []
        for managed_object in managed_objects:
            self.tenant.append(
                self.get_tenant_info(
                    managed_object
                )
            )

        return self.tenant

    def match_tenant(self, tenant_info, tenant_filter):
        if tenant_filter is None or len(tenant_filter) == 0:
            return True

        for aepg_rule in tenant_filter:
            (key, value) = aepg_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, tenant_info['name']):
                    return False

        return True

    def get_tenants(
            self,
            tenant_filter=None,
            count_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_tenants = self.get_tenants_info()
        if all_tenants is None:
            return None

        tenants = []

        for tenant_info in all_tenants:
            if not self.match_tenant(tenant_info, tenant_filter):
                continue

            if count_info:
                tenant_info['bdCount'] = self.get_bridge_domain_count(
                    tenant_name=tenant_info['name']
                )
                tenant_info['vrfCount'] = self.get_vrf_count(
                    tenant_name=tenant_info['name']
                )
                tenant_info['apCount'] = self.get_application_profile_count(
                    tenant_name=tenant_info['name']
                )
                tenant_info['aEpgCount'] = self.get_epg_count(
                    tenant_name=tenant_info['name']
                )
                tenant_info['l2OutCount'] = self.get_l2out_count(
                    tenant_name=tenant_info['name']
                )
                tenant_info['l3OutCount'] = self.get_l3out_count(
                    tenant_name=tenant_info['name'],
                    mpls='no'
                )
                tenant_info['mplsL3OutCount'] = self.get_l3out_count(
                    tenant_name=tenant_info['name'],
                    mpls='yes'
                )
                tenant_info['contractStandardCount'] = self.get_standard_contract_count(
                    tenant_name=tenant_info['name']
                )
                tenant_info['contractTabooCount'] = self.get_taboo_contract_count(
                    tenant_name=tenant_info['name']
                )
                tenant_info['contractFilterCount'] = self.get_contract_filter_count(
                    tenant_name=tenant_info['name']
                )
                tenant_info['endpointCount'] = self.get_endpoint_count(
                    tenant_name=tenant_info['name']
                )

            if fault_info:
                tenant_info['faultInst'] = self.get_tenant_id_fault(
                    tenant_info['name'],
                    'faultInst'
                )

            if hfault_info:
                tenant_info['faultRecord'] = self.get_tenant_id_fault(
                    tenant_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                tenant_info['eventLog'] = self.get_tenant_id_event(
                    tenant_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                tenant_info['auditLog'] = self.get_tenant_id_audit(
                    tenant_info['name'],
                    audit_filter=audit_filter
                )

            tenants.append(tenant_info)

        tenants = sorted(
            tenants,
            key=lambda i: i['name'].lower()
        )

        return tenants
