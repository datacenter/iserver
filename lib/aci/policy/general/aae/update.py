class PolicyGeneralAaeUpdate():
    def __init__(self):
        pass

    def get_add_policy_global_aae_domain_phy_body(
            self,
            domain_name
        ):
        body = {}
        body['infraRsDomP'] = {}
        body['infraRsDomP']['attributes'] = {}
        body['infraRsDomP']['attributes']['tDn'] = 'uni/phys-%s' % (domain_name)
        body['infraRsDomP']['attributes']['status'] = 'created'
        body['infraRsDomP']['children'] = []

        return body

    def add_policy_global_aae_domain_phy(
            self,
            policy_name,
            domain_name
        ):
        body = self.get_add_policy_global_aae_domain_phy_body(
            domain_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/attentp-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_global_aae_mo()

        return success, error

    def get_delete_policy_global_aae_domain_phy_body(
            self,
            policy_name,
            domain_name
        ):
        body = {}
        body['infraRsDomP'] = {}
        body['infraRsDomP']['attributes'] = {}
        body['infraRsDomP']['attributes']['dn'] = 'uni/infra/attentp-%s/rsdomP-[uni/phys-%s]' % (
            policy_name,
            domain_name
        )
        body['infraRsDomP']['attributes']['status'] = 'deleted'
        body['infraRsDomP']['children'] = []

        return body

    def delete_policy_global_aae_domain_phy(
            self,
            policy_name,
            domain_name
        ):
        body = self.get_delete_policy_global_aae_domain_phy_body(
            policy_name,
            domain_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/attentp-%s/rsdomP-[uni/phys-%s].json' % (
            policy_name,
            domain_name
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_global_aae_mo()

        return success, error

    def get_add_policy_global_aae_domain_l3_body(
            self,
            domain_name
        ):
        body = {}
        body['infraRsDomP'] = {}
        body['infraRsDomP']['attributes'] = {}
        body['infraRsDomP']['attributes']['tDn'] = 'uni/l3dom-%s' % (domain_name)
        body['infraRsDomP']['attributes']['status'] = 'created'
        body['infraRsDomP']['children'] = []

        return body

    def add_policy_global_aae_domain_l3(
            self,
            policy_name,
            domain_name
        ):
        body = self.get_add_policy_global_aae_domain_l3_body(
            domain_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/attentp-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_global_aae_mo()

        return success, error

    def get_delete_policy_global_aae_domain_l3_body(
            self,
            policy_name,
            domain_name
        ):
        body = {}
        body['infraRsDomP'] = {}
        body['infraRsDomP']['attributes'] = {}
        body['infraRsDomP']['attributes']['dn'] = 'uni/infra/attentp-%s/rsdomP-[uni/l3dom-%s]' % (
            policy_name,
            domain_name
        )
        body['infraRsDomP']['attributes']['status'] = 'deleted'
        body['infraRsDomP']['children'] = []

        return body

    def delete_policy_global_aae_domain_l3(
            self,
            policy_name,
            domain_name
        ):
        body = self.get_delete_policy_global_aae_domain_l3_body(
            policy_name,
            domain_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/attentp-%s/rsdomP-[uni/l3dom-%s].json' % (
            policy_name,
            domain_name
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_global_aae_mo()

        return success, error
