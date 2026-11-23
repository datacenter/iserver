class DomainL3Delete():
    def __init__(self):
        pass

    def get_delete_domain_l3_body(
            self,
            domain_name
        ):
        body = {}
        body['l3extDomP'] = {}
        body['l3extDomP']['attributes'] = {}
        body['l3extDomP']['attributes']['dn'] = 'uni/l3dom-%s' % (domain_name)
        body['l3extDomP']['attributes']['status'] = 'deleted'
        body['l3extDomP']['children'] = []

        return body

    def delete_domain_l3(
            self,
            domain_name
        ):
        body = self.get_delete_domain_l3_body(
            domain_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/l3dom-%s.json' % (domain_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_domain_l3_mo()
            self.init_domain_l3()

        return success, error
