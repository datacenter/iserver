class PolicyInterfaceL2Delete():
    def __init__(self):
        pass

    def get_delete_policy_interface_l2_body(
            self,
            policy_name
        ):
        body = {}
        body['l2IfPol'] = {}
        body['l2IfPol']['attributes'] = {}
        body['l2IfPol']['attributes']['dn'] = 'uni/infra/l2IfP-%s' % (policy_name)
        body['l2IfPol']['attributes']['status'] = 'deleted'
        body['l2IfPol']['children'] = []

        return body

    def delete_policy_interface_l2(
            self,
            policy_name
        ):
        body = self.get_delete_policy_interface_l2_body(
            policy_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/l2IfP-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_interface_l2_mo()
            self.init_policy_interface_l2()

        return success, error
