class PolicyInterfaceL2Create():
    def __init__(self):
        pass

    def get_create_policy_interface_l2_body(
            self,
            policy_name,
            qinq,
            vepa,
            vlan
        ):
        body = {}
        body['l2IfPol'] = {}
        body['l2IfPol']['attributes'] = {}
        body['l2IfPol']['attributes']['dn'] = 'uni/infra/l2IfP-%s' % (policy_name)
        body['l2IfPol']['attributes']['name'] = policy_name
        body['l2IfPol']['attributes']['rn'] = 'l2IfP-%s' % (policy_name)
        body['l2IfPol']['attributes']['status'] = 'created'
        if qinq == 'core':
            body['l2IfPol']['attributes']['qinq'] = 'corePort'
        if qinq == 'double':
            body['l2IfPol']['attributes']['qinq'] = 'doubleQtagPort'
        if qinq == 'edge':
            body['l2IfPol']['attributes']['qinq'] = 'edgePort'
        if vepa:
            body['l2IfPol']['attributes']['vepa'] = 'enabled'
        if qinq != 'edge':
            if vlan == 'local':
                body['l2IfPol']['attributes']['vlanScope'] = 'portlocal'

        body['l2IfPol']['children'] = []

        return body

    def create_policy_interface_l2(
            self,
            policy_name,
            qinq,
            vepa,
            vlan
        ):
        body = self.get_create_policy_interface_l2_body(
            policy_name,
            qinq,
            vepa,
            vlan
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
