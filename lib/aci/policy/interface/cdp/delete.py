class PolicyInterfaceCdpDelete():
    def __init__(self):
        pass

    def get_delete_policy_interface_cdp_body(
            self,
            policy_name
        ):
        body = {}
        body['cdpIfPol'] = {}
        body['cdpIfPol']['attributes'] = {}
        body['cdpIfPol']['attributes']['dn'] = 'uni/infra/cdpIfP-%s' % (policy_name)
        body['cdpIfPol']['attributes']['status'] = 'deleted'
        body['cdpIfPol']['children'] = []

        return body

    def delete_policy_interface_cdp(
            self,
            policy_name
        ):
        body = self.get_delete_policy_interface_cdp_body(
            policy_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/cdpIfP-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_interface_cdp_mo()
            self.init_policy_interface_cdp()

        return success, error
