class PolicyGroupAccessInterfaceVpcCreate():
    def __init__(self):
        pass

    def get_create_policy_group_access_interface_vpc_body(
            self,
            policy_name,
            aaep=None,
            port_channel=None,
            cdp=None,
            lldp=None,
            l2=None,
            link_level=None
        ):
        body = {}
        body['infraAccBndlGrp'] = {}
        body['infraAccBndlGrp']['attributes'] = {}
        body['infraAccBndlGrp']['attributes']['dn'] = 'uni/infra/funcprof/accbundle-%s' % (policy_name)
        body['infraAccBndlGrp']['attributes']['lagT'] = 'node'
        body['infraAccBndlGrp']['attributes']['name'] = policy_name
        body['infraAccBndlGrp']['attributes']['rn'] = 'accbundle-%s' % (policy_name)
        body['infraAccBndlGrp']['attributes']['status'] = 'created'

        body['infraAccBndlGrp']['children'] = []

        if aaep is not None:
            child_mo = {}
            child_mo['infraRsAttEntP'] = {}
            child_mo['infraRsAttEntP']['attributes'] = {}
            child_mo['infraRsAttEntP']['attributes']['tDn'] = 'uni/infra/attentp-%s' % (aaep)
            child_mo['infraRsAttEntP']['attributes']['status'] = 'created,modified'
            child_mo['infraRsAttEntP']['children'] = []
            body['infraAccBndlGrp']['children'].append(
                child_mo
            )

        if l2 is not None:
            child_mo = {}
            child_mo['infraRsL2IfPol'] = {}
            child_mo['infraRsL2IfPol']['attributes'] = {}
            child_mo['infraRsL2IfPol']['attributes']['tnL2IfPolName'] = l2
            child_mo['infraRsL2IfPol']['attributes']['status'] = 'created,modified'
            child_mo['infraRsL2IfPol']['children'] = []
            body['infraAccBndlGrp']['children'].append(
                child_mo
            )

        if cdp is not None:
            child_mo = {}
            child_mo['infraRsCdpIfPol'] = {}
            child_mo['infraRsCdpIfPol']['attributes'] = {}
            child_mo['infraRsCdpIfPol']['attributes']['tnCdpIfPolName'] = cdp
            child_mo['infraRsCdpIfPol']['attributes']['status'] = 'created,modified'
            child_mo['infraRsCdpIfPol']['children'] = []
            body['infraAccBndlGrp']['children'].append(
                child_mo
            )

        if link_level is not None:
            child_mo = {}
            child_mo['infraRsHIfPol'] = {}
            child_mo['infraRsHIfPol']['attributes'] = {}
            child_mo['infraRsHIfPol']['attributes']['tnFabricHIfPolName'] = link_level
            child_mo['infraRsHIfPol']['attributes']['status'] = 'created,modified'
            child_mo['infraRsHIfPol']['children'] = []
            body['infraAccBndlGrp']['children'].append(
                child_mo
            )

        if lldp is not None:
            child_mo = {}
            child_mo['infraRsLldpIfPol'] = {}
            child_mo['infraRsLldpIfPol']['attributes'] = {}
            child_mo['infraRsLldpIfPol']['attributes']['tnLldpIfPolName'] = lldp
            child_mo['infraRsLldpIfPol']['attributes']['status'] = 'created,modified'
            child_mo['infraRsLldpIfPol']['children'] = []
            body['infraAccBndlGrp']['children'].append(
                child_mo
            )

        if port_channel is not None:
            child_mo = {}
            child_mo['infraRsLacpPol'] = {}
            child_mo['infraRsLacpPol']['attributes'] = {}
            child_mo['infraRsLacpPol']['attributes']['tnLacpLagPolName'] = port_channel
            child_mo['infraRsLacpPol']['attributes']['status'] = 'created,modified'
            child_mo['infraRsLacpPol']['children'] = []
            body['infraAccBndlGrp']['children'].append(
                child_mo
            )

        return body

    def create_policy_group_access_interface_vpc(
            self,
            policy_name,
            aaep=None,
            port_channel=None,
            cdp=None,
            lldp=None,
            l2=None,
            link_level=None,
            wait=False
        ):
        body = self.get_create_policy_group_access_interface_vpc_body(
            policy_name,
            aaep=aaep,
            port_channel=port_channel,
            cdp=cdp,
            lldp=lldp,
            l2=l2,
            link_level=link_level
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra.json'
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_group_access_interface_vpc_mo()
            self.init_policy_group_access_interface_vpc()

            if wait:
                if not self.wait_policy_group_access_interface_vpc(policy_name):
                    return False, 'Wait time reached'

        return success, error
