class PolicyGeneralAaeDelete():
    def __init__(self):
        pass

    def get_delete_policy_global_aae_body(
            self,
            policy_name
        ):
        body = {}
        body['infraAttEntityP'] = {}
        body['infraAttEntityP']['attributes'] = {}
        body['infraAttEntityP']['attributes']['dn'] = 'uni/infra/attentp-%s' % (policy_name)
        body['infraAttEntityP']['attributes']['status'] = 'deleted'
        body['infraAttEntityP']['children'] = []

        return body

    def delete_policy_global_aae(
            self,
            policy_name
        ):
        body = self.get_delete_policy_global_aae_body(
            policy_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/attentp-%s.json' % (
            policy_name
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_global_aae_mo()

        return success, error
