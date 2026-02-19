class DomainL3Update():
    def __init__(self):
        pass

    def get_delete_domain_l3_vlan_pool_body(
            self,
            domain_name
        ):
        body = {}
        body['infraRsVlanNs'] = {}
        body['infraRsVlanNs']['attributes'] = {}
        body['infraRsVlanNs']['attributes']['dn'] = 'uni/l3dom-%s/rsvlanNs' % (domain_name)
        body['infraRsVlanNs']['attributes']['status'] = 'deleted'
        body['infraRsVlanNs']['children'] = []

        return body

    def delete_domain_l3_vlan_pool(
            self,
            domain_name
        ):
        body = self.get_delete_domain_l3_vlan_pool_body(
            domain_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/l3dom-%s/rsvlanNs.json' % (domain_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_domain_l3_mo()
            self.init_domain_l3()

        return success, error

    def get_add_domain_l3_vlan_pool_body(
            self,
            pool_name,
            pool_type
        ):
        body = {}
        body['infraRsVlanNs'] = {}
        body['infraRsVlanNs']['attributes'] = {}
        body['infraRsVlanNs']['attributes']['tDn'] = 'uni/infra/vlanns-[%s]-%s' % (
            pool_name,
            pool_type
        )
        body['infraRsVlanNs']['children'] = []

        return body

    def add_domain_l3_vlan_pool(
            self,
            domain_name,
            pool_name,
            pool_type
        ):
        body = self.get_add_domain_l3_vlan_pool_body(
            pool_name,
            pool_type
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/l3dom-%s/rsvlanNs.json' % (domain_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_domain_l3_mo()
            self.init_domain_l3()

        return success, error
