class PolicyInterfaceLldpDelete():
    def __init__(self):
        pass

    def get_delete_policy_interface_lldp_body(
            self,
            policy_name
        ):
        body = {}
        body['lldpIfPol'] = {}
        body['lldpIfPol']['attributes'] = {}
        body['lldpIfPol']['attributes']['dn'] = 'uni/infra/lldpIfP-%s' % (policy_name)
        body['lldpIfPol']['attributes']['status'] = 'deleted'
        body['lldpIfPol']['children'] = []

        return body

    def delete_policy_interface_lldp(
            self,
            policy_name
        ):
        body = self.get_delete_policy_interface_lldp_body(
            policy_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/lldpIfP-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_interface_lldp_mo()
            self.init_policy_interface_lldp()

        return success, error
