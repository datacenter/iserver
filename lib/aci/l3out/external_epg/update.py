class L3OutExternalEpgUpdate():
    def __init__(self):
        pass

    def get_add_l3out_external_epg_subnet_body(
            self,
            tenant_name,
            l3out_name,
            epg_name,
            subnet,
            subnet_name,
            subnet_scope
        ):
        body = {}
        body['l3extSubnet'] = {}
        body['l3extSubnet']['attributes'] = {}
        body['l3extSubnet']['attributes']['dn'] = 'uni/tn-%s/out-%s/instP-%s/extsubnet-[%s]' % (
            tenant_name,
            l3out_name,
            epg_name,
            subnet
        )
        body['l3extSubnet']['attributes']['ip'] = subnet
        body['l3extSubnet']['attributes']['name'] = subnet_name
        body['l3extSubnet']['attributes']['scope'] = subnet_scope
        body['l3extSubnet']['attributes']['aggregate'] = ''
        body['l3extSubnet']['attributes']['rn'] = 'extsubnet-[%s]' % (subnet)
        body['l3extSubnet']['attributes']['status'] = 'created'
        body['l3extSubnet']['children'] = []

        return body

    def add_l3out_external_epg_subnet(
            self,
            tenant_name,
            l3out_name,
            epg_name,
            subnet,
            subnet_name,
            subnet_scope
        ):

        body = self.get_add_l3out_external_epg_subnet_body(
            tenant_name,
            l3out_name,
            epg_name,
            subnet,
            subnet_name,
            subnet_scope
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/tn-%s/out-%s/instP-%s/extsubnet-[%s].json' % (
            tenant_name,
            l3out_name,
            epg_name,
            subnet
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_l3out_mo()
            self.init_l3out()
            self.init_l3out_external_epg()
            self.init_l3out_external_epg_mo()

        return success, error
