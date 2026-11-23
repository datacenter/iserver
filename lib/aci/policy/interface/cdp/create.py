class PolicyInterfaceCdpCreate():
    def __init__(self):
        pass

    def get_create_policy_interface_cdp_body(
            self,
            policy_name,
            enabled
        ):
        body = {}
        body['cdpIfPol'] = {}
        body['cdpIfPol']['attributes'] = {}
        body['cdpIfPol']['attributes']['dn'] = 'uni/infra/cdpIfP-%s' % (policy_name)
        body['cdpIfPol']['attributes']['name'] = policy_name
        if not enabled:
            body['cdpIfPol']['attributes']['adminSt'] = 'disabled'
        body['cdpIfPol']['attributes']['rn'] = 'cdpIfP-%s' % (policy_name)
        body['cdpIfPol']['attributes']['status'] = 'created'
        body['cdpIfPol']['children'] = []
        return body

    def create_policy_interface_cdp(
            self,
            policy_name,
            enabled
        ):
        body = self.get_create_policy_interface_cdp_body(
            policy_name,
            enabled
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
