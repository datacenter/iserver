class DomainPhyCreate():
    def __init__(self):
        pass

    def get_create_domain_phy_body(
            self,
            policy_name,
            pool=None
        ):
        body = {}
        body['physDomP'] = {}
        body['physDomP']['attributes'] = {}
        body['physDomP']['attributes']['dn'] = 'uni/phys-%s' % (policy_name)
        body['physDomP']['attributes']['name'] = policy_name
        body['physDomP']['attributes']['rn'] = 'phys-%s' % (policy_name)
        body['physDomP']['attributes']['status'] = 'created'
        body['physDomP']['children'] = []

        if pool is not None:
            pool_mo = {}
            pool_mo['infraRsVlanNs'] = {}
            pool_mo['infraRsVlanNs']['attributes'] = {}
            pool_mo['infraRsVlanNs']['attributes']['tDn'] = 'uni/infra/vlanns-[%s]-static' % (pool)
            pool_mo['infraRsVlanNs']['attributes']['status'] = 'created'
            pool_mo['infraRsVlanNs']['children'] = []

            body['physDomP']['children'].append(
                pool_mo
            )

        return body

    def create_domain_phy(
            self,
            policy_name,
            pool=None,
            wait=False
        ):
        body = self.get_create_domain_phy_body(
            policy_name,
            pool=pool
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/phys-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_domain_phy_mo()
            self.init_domain_phy()

            if wait:
                if not self.wait_domain_phy(policy_name):
                    return False, 'Wait time reached'

        return success, error
