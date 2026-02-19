class BridgeDomainDelete():
    def __init__(self):
        pass

    def get_delete_bridge_domain_body(
            self,
            tenant_name,
            bd_name
        ):
        body = {}
        body['fvBD'] = {}
        body['fvBD']['attributes'] = {}
        body['fvBD']['attributes']['dn'] = 'uni/tn-%s/BD-%s' % (tenant_name, bd_name)
        body['fvBD']['attributes']['status'] = 'deleted'
        body['fvBD']['children'] = []

        return body

    def delete_bridge_domain(
            self,
            tenant_name,
            bd_name
        ):
        body = self.get_delete_bridge_domain_body(
            tenant_name,
            bd_name
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
