class PolicyGroupAccessInterfacePortApi():
    def __init__(self):
        self.policy_group_access_interface_port_mo = None
        self.policy_group_access_interface_port_policies = [
            'infraRsAttEntP',
            'infraRsCdpIfPol',
            'infraRsHIfPol',
            'infraRsLinkFlapPol',
            'infraRsLldpIfPol',
            'infraRsMonIfInfraPol',
            'infraRsStpIfPol',
            'infraRsMcpIfPol',
            'infraRsStormctrlIfPol'
        ]

    def get_policy_group_access_interface_port_mo(self):
        if self.policy_group_access_interface_port_mo is not None:
            return self.policy_group_access_interface_port_mo

        cache = self.get_object_cache(
            'infraAccPortGrp'
        )
        if cache is not None:
            self.policy_group_access_interface_port_mo = cache
            self.log.apic_mo(
                'infraAccPortGrp',
                self.policy_group_access_interface_port_mo
            )
            return self.policy_group_access_interface_port_mo

        # url: https://<apic>/api/node/mo/uni/infra/funcprof.json?
        # query-target=subtree&target-subtree-class=infraAccPortGrp&query-target-filter=not(wcard(infraAccPortGrp.dn,"__ui_"))&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
        # &subscription=yes&order-by=infraAccPortGrp.name|asc&page=0&page-size=15

        distinguished_name = 'uni/infra/funcprof'
        query = 'query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=%s' % (
            ','.join(self.policy_group_access_interface_port_policies)
        )

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_policy_group_access_interface_port_mo',
                'API failed'
            )
            return None

        self.log.apic_mo(
            'infraAccPortGrp.mo',
            managed_objects
        )

        self.policy_group_access_interface_port_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraAccPortGrp']['attributes']
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'infraAccPortGrp',
                managed_object,
                'faultCounts'
            )
            for policy_name in self.policy_group_access_interface_port_policies:
                attributes[policy_name] = self.get_mo_child_attributes(
                    'infraAccPortGrp',
                    managed_object,
                    policy_name
                )

            self.policy_group_access_interface_port_mo.append(
                attributes
            )

        self.log.apic_mo(
            'infraAccPortGrp',
            self.policy_group_access_interface_port_mo
        )

        self.set_object_cache(
            'infraAccPortGrp',
            self.policy_group_access_interface_port_mo
        )

        return self.policy_group_access_interface_port_mo
