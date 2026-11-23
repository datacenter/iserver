class L3OutExternalEpgDelete():
    def __init__(self):
        pass

    def get_delete_l3out_external_epg_subnet_body(
            self,
            tenant_name,
            l3out_name,
            epg_name,
            subnet
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
        body['l3extSubnet']['attributes']['status'] = 'deleted'
        body['l3extSubnet']['children'] = []

        return body

    def delete_l3out_external_epg_subnet(
            self,
            tenant_name,
            l3out_name,
            epg_name,
            subnet
        ):

        body = self.get_delete_l3out_external_epg_subnet_body(
            tenant_name,
            l3out_name,
            epg_name,
            subnet
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
