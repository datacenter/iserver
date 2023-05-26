class PolicyGroupAccessInterfacePortApi():
    def __init__(self):
        self.policy_group_access_interface_port_mo = None

    def get_policy_group_access_interface_port_mo(self):
        if self.policy_group_access_interface_port_mo is not None:
            return self.policy_group_access_interface_port_mo

        # url: https://apic21o-eu-spdc.cisco.com/api/node/mo/uni/infra/funcprof.json?
        # query-target=subtree&target-subtree-class=infraAccPortGrp&query-target-filter=not(wcard(infraAccPortGrp.dn,"__ui_"))&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
        # &subscription=yes&order-by=infraAccPortGrp.name|asc&page=0&page-size=15

        distinguished_name = 'uni/infra/funcprof'
        children = [
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
        query = 'query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-class=%s' % (
            ','.join(children)
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
            attributes['policy'] = {}
            for child in children:
                attributes['policy'][child] = ''

            for child in managed_object['infraAccPortGrp']['children']:
                for key in child:
                    if 'infraRsAttEntP' in child:
                        attributes['aaep_name'] = child['infraRsAttEntP']['attributes']['tDn'].split('/')[2].split('-')[1]

                    if key == 'infraRsStpIfPol':
                        if 'infraRsStpIfPol' in child:
                            attributes['policy']['infraRsStpIfPol'] = self.get_policy_interface_reference_attributes(
                                child['infraRsStpIfPol']['attributes']
                            )['name']

                    if key == 'infraRsStormctrlIfPol':
                        if 'infraRsStormctrlIfPol' in child:
                            attributes['policy']['infraRsStormctrlIfPol'] = self.get_policy_interface_reference_attributes(
                                child['infraRsStormctrlIfPol']['attributes']
                            )['name']

                    if key == 'infraRsMonIfInfraPol':
                        if 'infraRsMonIfInfraPol' in child:
                            attributes['policy']['infraRsMonIfInfraPol'] = self.get_policy_interface_reference_attributes(
                                child['infraRsMonIfInfraPol']['attributes']
                            )['name']

                    if key == 'infraRsMcpIfPol':
                        if 'infraRsMcpIfPol' in child:
                            attributes['policy']['infraRsMcpIfPol'] = self.get_policy_interface_reference_attributes(
                                child['infraRsMcpIfPol']['attributes']
                            )['name']

                    if key == 'infraRsLldpIfPol':
                        if 'infraRsLldpIfPol' in child:
                            attributes['policy']['infraRsLldpIfPol'] = self.get_policy_interface_reference_attributes(
                                child['infraRsLldpIfPol']['attributes']
                            )['name']

                    if key == 'infraRsLinkFlapPol':
                        if 'infraRsLinkFlapPol' in child:
                            attributes['policy']['infraRsLinkFlapPol'] = self.get_policy_interface_reference_attributes(
                                child['infraRsLinkFlapPol']['attributes']
                            )['name']

                    if key == 'infraRsHIfPol':
                        if 'infraRsHIfPol' in child:
                            attributes['policy']['infraRsHIfPol'] = self.get_policy_interface_reference_attributes(
                                child['infraRsHIfPol']['attributes']
                            )['name']

                    if key == 'infraRsCdpIfPol':
                        if 'infraRsCdpIfPol' in child:
                            attributes['policy']['infraRsCdpIfPol'] = self.get_policy_interface_reference_attributes(
                                child['infraRsCdpIfPol']['attributes']
                            )['name']

            self.policy_group_access_interface_port_mo.append(
                attributes
            )

        self.log.apic_mo(
            'infraAccPortGrp',
            self.policy_group_access_interface_port_mo
        )

        return self.policy_group_access_interface_port_mo
