class PolicyGroupAccessInterfaceVpcApi():
    def __init__(self):
        self.policy_group_access_interface_vpc_mo = None

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
        children = [
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
        query = 'query-target=subtree&target-subtree-class=%s&rsp-subtree=children&rsp-subtree-class=%s' % (
            'infraAccBndlGrp',
            ','.join(children)
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
            attributes['aaep_name'] = None
            attributes['policy'] = {}
            attributes['policies'] = []

            for child in children:
                if child == 'infraRsAttEntP':
                    continue

                attributes['policy'][child] = ''

                policy = {}
                policy['type'] = child
                policy['name'] = None
                attributes['policies'].append(
                    policy
                )

            for child in managed_object['infraAccBndlGrp']['children']:
                if 'infraRsAttEntP' in child:
                    attributes['aaep_name'] = child['infraRsAttEntP']['attributes']['tDn'].split('/')[2].split('-')[1]

                if 'infraRsStpIfPol' in child:
                    attributes['policy']['infraRsStpIfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsStpIfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsStpIfPol':
                            policy['name'] = attributes['policy']['infraRsStpIfPol']

                if 'infraRsCdpIfPol' in child:
                    attributes['policy']['infraRsCdpIfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsCdpIfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsCdpIfPol':
                            policy['name'] = attributes['policy']['infraRsCdpIfPol']

                if 'infraRsMcpIfPol' in child:
                    attributes['policy']['infraRsMcpIfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsMcpIfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsMcpIfPol':
                            policy['name'] = attributes['policy']['infraRsMcpIfPol']

                if 'infraRsHIfPol' in child:
                    attributes['policy']['infraRsHIfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsHIfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsHIfPol':
                            policy['name'] = attributes['policy']['infraRsHIfPol']

                if 'infraRsLinkFlapPol' in child:
                    attributes['policy']['infraRsLinkFlapPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsLinkFlapPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsLinkFlapPol':
                            policy['name'] = attributes['policy']['infraRsLinkFlapPol']

                if 'infraRsLldpIfPol' in child:
                    attributes['policy']['infraRsLldpIfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsLldpIfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsLldpIfPol':
                            policy['name'] = attributes['policy']['infraRsLldpIfPol']

                if 'infraRsLacpPol' in child:
                    attributes['policy']['infraRsLacpPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsLacpPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsLacpPol':
                            policy['name'] = attributes['policy']['infraRsLacpPol']

                if 'infraRsStormctrlIfPol' in child:
                    attributes['policy']['infraRsStormctrlIfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsStormctrlIfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsStormctrlIfPol':
                            policy['name'] = attributes['policy']['infraRsStormctrlIfPol']

                if 'infraRsMacsecIfPol' in child:
                    attributes['policy']['infraRsMacsecIfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsMacsecIfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsMacsecIfPol':
                            policy['name'] = attributes['policy']['infraRsMacsecIfPol']

                if 'infraRsL2IfPol' in child:
                    attributes['policy']['infraRsL2IfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsL2IfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsL2IfPol':
                            policy['name'] = attributes['policy']['infraRsL2IfPol']

                if 'infraRsFcIfPol' in child:
                    attributes['policy']['infraRsFcIfPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsFcIfPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsFcIfPol':
                            policy['name'] = attributes['policy']['infraRsFcIfPol']

                if 'infraRsL2PortSecurityPol' in child:
                    attributes['policy']['infraRsL2PortSecurityPol'] = self.get_policy_interface_reference_attributes(
                        child['infraRsL2PortSecurityPol']['attributes']
                    )['name']

                    for policy in attributes['policies']:
                        if policy['type'] == 'infraRsL2PortSecurityPol':
                            policy['name'] = attributes['policy']['infraRsL2PortSecurityPol']

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
