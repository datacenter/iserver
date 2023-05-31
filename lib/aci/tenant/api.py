class TenantApi():
    def __init__(self):
        self.tenant_mo = None

    def get_tenant_mo(self):
        # "attributes": {
        #     "annotation": "orchestrator:ansible",
        #     "childAction": "",
        #     "descr": "User Tenant CDC SR L3out (Managed with Ansible)",
        #     "dn": "uni/tn-MPC-E",
        #     "extMngdBy": "",
        #     "lcOwn": "local",
        #     "modTs": "2023-01-03T20:33:37.125+01:00",
        #     "monPolDn": "uni/tn-common/monepg-default",
        #     "name": "MPC-E",
        #     "nameAlias": "",
        #     "ownerKey": "",
        #     "ownerTag": "",
        #     "status": "",
        #     "uid": "15374",
        #     "userdom": ":all:"
        # }
        if self.tenant_mo is not None:
            return self.tenant_mo

        managed_objects = self.get_class(
            'fvTenant'
        )
        if managed_objects is None:
            return None

        self.tenant_mo = []
        for managed_object in managed_objects['imdata']:
            self.tenant_mo.append(
                managed_object['fvTenant']['attributes']
            )

        self.log.apic_mo(
            'fvTenant',
            self.tenant_mo
        )

        return self.tenant_mo
