class PolicyInterfaceLinkLevelDelete():
    def __init__(self):
        pass

    def get_delete_policy_interface_link_level_body(
            self,
            policy_name
        ):
        body = {}
        body['fabricHIfPol'] = {}
        body['fabricHIfPol']['attributes'] = {}
        body['fabricHIfPol']['attributes']['dn'] = 'uni/infra/hintfpol-%s' % (policy_name)
        body['fabricHIfPol']['attributes']['status'] = 'deleted'
        body['fabricHIfPol']['children'] = []

        return body

    def delete_policy_interface_link_level(
            self,
            policy_name
        ):
        body = self.get_delete_policy_interface_link_level_body(
            policy_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/hintfpol-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_interface_link_level_mo()
            self.init_policy_interface_link_level()

        return success, error
