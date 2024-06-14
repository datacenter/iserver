class PolicyGroupAccessInterfaceVpcApi():
    def __init__(self):
        self.policy_group_access_interface_vpc_mo = None
        self.policy_group_access_interface_vpc_policies = [
            'infraRsCdpIfPol',
            'infraRsMcpIfPol',
            'infraRsHIfPol',
            'infraRsLinkFlapPol',
            'infraRsLldpIfPol',
            'infraRsLacpPol',
            'infraRsMonIfInfraPol',
            'infraAccBndlSubgrp',
            'infraRsStpIfPol',
            'infraRsAttEntP',
            'infraRsSpanVSrcGrp',
            'infraRsSpanVDestGrp',
            'infraRsL2IfPol',
            'infraRsStormctrlIfPol',
            'infraRsQosEgressDppIfPol',
            'infraRsQosIngressDppIfPol',
            'infraRsQosSdIfPol',
            'infraRsQosPfcIfPol',
            'infraRsQosEgressDppIfPol',
            'infraRsL2PortSecurityPol',
            'infraRsFcIfPol',
            'infraRsMacsecIfPol'
        ]

    def get_policy_group_access_interface_vpc_mo(self):
        if self.policy_group_access_interface_vpc_mo is not None:
            return self.policy_group_access_interface_vpc_mo

        cache = self.get_object_cache(
            'infraAccBndlGrp'
        )
        if cache is not None:
            self.policy_group_access_interface_vpc_mo = cache
            self.log.apic_mo(
                'infraAccBndlGrp',
                self.policy_group_access_interface_vpc_mo
            )
            return self.policy_group_access_interface_vpc_mo

        distinguished_name = 'uni/infra/funcprof'
        query = 'query-target=subtree&target-subtree-class=%s&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=%s' % (
            'infraAccBndlGrp',
            ','.join(self.policy_group_access_interface_vpc_policies)
        )

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_policy_group_access_interface_vpc_mo',
                'API failed'
            )
            return None

        self.policy_group_access_interface_vpc_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraAccBndlGrp']['attributes']
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'infraAccBndlGrp',
                managed_object,
                'faultCounts'
            )
            for policy_name in self.policy_group_access_interface_vpc_policies:
                attributes[policy_name] = self.get_mo_child_attributes(
                    'infraAccBndlGrp',
                    managed_object,
                    policy_name
                )

            self.policy_group_access_interface_vpc_mo.append(
                attributes
            )

        self.log.apic_mo(
            'infraAccBndlGrp',
            self.policy_group_access_interface_vpc_mo
        )

        self.set_object_cache(
            'infraAccBndlGrp',
            self.policy_group_access_interface_vpc_mo
        )

        return self.policy_group_access_interface_vpc_mo
