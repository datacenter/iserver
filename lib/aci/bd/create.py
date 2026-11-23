class BridgeDomainCreate():
    def __init__(self):
        pass

    def get_create_bridge_domain_body(
            self,
            tenant_name,
            bd_name,
            gateway,
            vrf_name,
            l3out_name
        ):
        body = {}
        body['fvBD'] = {}
        body['fvBD']['attributes'] = {}
        body['fvBD']['attributes']['dn'] = 'uni/tn-%s/BD-%s' % (tenant_name, bd_name)
        body['fvBD']['attributes']['arpFlood'] = 'true'
        body['fvBD']['attributes']['rn'] = 'BD-%s' % (bd_name)
        body['fvBD']['attributes']['name'] = bd_name
        body['fvBD']['attributes']['status'] = 'created'
        body['fvBD']['children'] = []

        subnet_mo = {}
        subnet_mo['fvSubnet'] = {}
        subnet_mo['fvSubnet']['attributes'] = {}
        subnet_mo['fvSubnet']['attributes']['dn'] = 'uni/tn-%s/BD-%s/subnet-[%s]' % (
            tenant_name,
            bd_name,
            gateway
        )
        subnet_mo['fvSubnet']['attributes']['ctrl'] = ''
        subnet_mo['fvSubnet']['attributes']['ip'] = gateway
        subnet_mo['fvSubnet']['attributes']['scope'] = 'public'
        subnet_mo['fvSubnet']['attributes']['rn'] = 'subnet-[%s]' % (gateway)
        subnet_mo['fvSubnet']['attributes']['status'] = 'created'
        subnet_mo['fvSubnet']['children'] = []

        body['fvBD']['children'].append(
            subnet_mo
        )

        vrf_mo = {}
        vrf_mo['fvRsCtx'] = {}
        vrf_mo['fvRsCtx']['attributes'] = {}
        vrf_mo['fvRsCtx']['attributes']['tnFvCtxName'] = vrf_name
        vrf_mo['fvRsCtx']['attributes']['status'] = 'created,modified'
        vrf_mo['fvRsCtx']['children'] = []

        body['fvBD']['children'].append(
            vrf_mo
        )


        l3out_mo = {}
        l3out_mo['fvRsBDToOut'] = {}
        l3out_mo['fvRsBDToOut']['attributes'] = {}
        l3out_mo['fvRsBDToOut']['attributes']['tnL3extOutName'] = l3out_name
        l3out_mo['fvRsBDToOut']['attributes']['status'] = 'created'
        l3out_mo['fvRsBDToOut']['children'] = []

        body['fvBD']['children'].append(
            l3out_mo
        )

        return body

    def create_bridge_domain(
            self,
            tenant_name,
            bd_name,
            gateway,
            vrf_name,
            l3out_name
        ):
        body = self.get_create_bridge_domain_body(
            tenant_name,
            bd_name,
            gateway,
            vrf_name,
            l3out_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/tn-%s/BD-%s.json' % (tenant_name, bd_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_bridge_domain_mo()
            self.init_bridge_domain()

        return success, error
