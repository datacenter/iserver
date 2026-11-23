class DomainL3Create():
    def __init__(self):
        pass

    def get_create_domain_l3_body(
            self,
            policy_name,
            pool=None
        ):
        body = {}
        body['l3extDomP'] = {}
        body['l3extDomP']['attributes'] = {}
        body['l3extDomP']['attributes']['dn'] = 'uni/l3dom-%s' % (policy_name)
        body['l3extDomP']['attributes']['name'] = policy_name
        body['l3extDomP']['attributes']['rn'] = 'l3dom-%s' % (policy_name)
        body['l3extDomP']['attributes']['status'] = 'created'
        body['l3extDomP']['children'] = []

        if pool is not None:
            pool_mo = {}
            pool_mo['infraRsVlanNs'] = {}
            pool_mo['infraRsVlanNs']['attributes'] = {}
            pool_mo['infraRsVlanNs']['attributes']['tDn'] = 'uni/infra/vlanns-[%s]-static' % (pool)
            pool_mo['infraRsVlanNs']['attributes']['status'] = 'created'
            pool_mo['infraRsVlanNs']['children'] = []

            body['l3extDomP']['children'].append(
                pool_mo
            )

        return body

    def create_domain_l3(
            self,
            policy_name,
            pool=None,
            wait=False
        ):
        body = self.get_create_domain_l3_body(
            policy_name,
            pool=pool
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/l3dom-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_domain_l3_mo()
            self.init_domain_l3()

            if wait:
                if not self.wait_domain_l3(policy_name):
                    return False, 'Wait time reached'

        return success, error
