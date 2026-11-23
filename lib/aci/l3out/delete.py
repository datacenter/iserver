class L3OutDelete():
    def __init__(self):
        pass

    def get_delete_l3out_body(
            self,
            tenant_name,
            l3out_name
        ):
        body = {}
        body['l3extOut'] = {}
        body['l3extOut']['attributes'] = {}
        body['l3extOut']['attributes']['dn'] = 'uni/tn-%s/out-%s' % (
            tenant_name,
            l3out_name
        )
        body['l3extOut']['attributes']['status'] = 'deleted'
        body['l3extOut']['children'] = []

        return body

    def delete_l3out(
            self,
            tenant_name,
            l3out_name
        ):

        body = self.get_delete_l3out_body(
            tenant_name,
            l3out_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/tn-%s/out-%s.json' % (tenant_name, l3out_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_l3out_mo()
            self.init_l3out()

        return success, error
