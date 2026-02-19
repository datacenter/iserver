class PolicyInterfacePortChannelDelete():
    def __init__(self):
        pass

    def get_delete_policy_interface_port_channel_body(
            self,
            policy_name
        ):
        body = {}
        body['lacpLagPol'] = {}
        body['lacpLagPol']['attributes'] = {}
        body['lacpLagPol']['attributes']['dn'] = 'uni/infra/lacplagp-%s' % (policy_name)
        body['lacpLagPol']['attributes']['status'] = 'deleted'
        body['lacpLagPol']['children'] = []

        return body

    def delete_policy_interface_port_channel(
            self,
            policy_name
        ):
        body = self.get_delete_policy_interface_port_channel_body(
            policy_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/lacplagp-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_interface_port_channel_mo()
            self.init_policy_interface_port_channel()

        return success, error
