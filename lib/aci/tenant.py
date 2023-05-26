class Tenant():
    def __init__(self, log_id=None):
        self.mo_tenants = None

    def get_tenants(self):
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
        if self.mo_tenants is None:
            managed_objects = self.get_class(
                'fvTenant'
            )
            if managed_objects is None:
                return None

            self.mo_tenants = managed_objects

        tenants = []

        for managed_object in self.mo_tenants['imdata']:
            keys = [
                'descr',
                'dn',
                'lcOwn',
                'name',
                'userdom'
            ]

            tenant = {}
            for key in keys:
                tenant[key] = None
                if key in managed_object['fvTenant']['attributes']:
                    tenant[key] = managed_object['fvTenant']['attributes'][key]

            tenant['bdCount'] = self.get_bridge_domain_count(
                tenant_name=tenant['name']
            )
            tenant['vrfCount'] = self.get_vrf_count(
                tenant_name=tenant['name']
            )
            tenant['apCount'] = self.get_application_profile_count(
                tenant_name=tenant['name']
            )
            tenant['aEpgCount'] = self.get_epg_count(
                tenant_name=tenant['name']
            )
            tenant['l2OutCount'] = self.get_l2out_count(
                tenant_name=tenant['name']
            )
            tenant['l3OutCount'] = self.get_l3out_count(
                tenant_name=tenant['name'],
                mpls='no'
            )
            tenant['mplsL3OutCount'] = self.get_l3out_count(
                tenant_name=tenant['name'],
                mpls='yes'
            )
            tenant['contractCount'] = self.get_contract_count(
                tenant_name=tenant['name']
            )
            tenant['endpointCount'] = self.get_endpoint_count(
                tenant_name=tenant['name']
            )
            tenants.append(tenant)

        tenants = sorted(
            tenants,
            key=lambda i: i['name'].lower()
        )

        return tenants

    def print_tenants(self, tenants):
        order = [
            'name',
            'apCount',
            'aEpgCount',
            'bdCount',
            'vrfCount',
            'l2OutCount',
            'l3OutCount',
            'mplsL3OutCount',
            'contractCount',
            'endpointCount'
        ]

        headers = [
            'Name',
            'App Profile',
            'EPG',
            'Bridge Domain',
            'VRF',
            'L2Out',
            'L3Out',
            'MPLS-SR L3Out',
            'Contract',
            'Endpoint'
        ]

        self.my_output.my_table(
            tenants,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
