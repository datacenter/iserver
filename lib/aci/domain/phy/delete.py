class DomainPhyDelete():
    def __init__(self):
        pass

    def get_delete_domain_phy_body(
            self,
            domain_name
        ):
        body = {}
        body['physDomP'] = {}
        body['physDomP']['attributes'] = {}
        body['physDomP']['attributes']['dn'] = 'uni/phys-%s' % (domain_name)
        body['physDomP']['attributes']['status'] = 'deleted'
        body['physDomP']['children'] = []

        return body

    def delete_domain_phy(
            self,
            domain_name
        ):
        body = self.get_delete_domain_phy_body(
            domain_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/phys-%s.json' % (domain_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_domain_phy_mo()
            self.init_domain_phy()

        return success, error
