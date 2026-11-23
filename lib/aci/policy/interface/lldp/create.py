class PolicyInterfaceLldpCreate():
    def __init__(self):
        pass

    def get_create_policy_interface_lldp_body(
            self,
            policy_name,
            lldp_receive,
            lldp_transmit
        ):
        body = {}
        body['lldpIfPol'] = {}
        body['lldpIfPol']['attributes'] = {}
        body['lldpIfPol']['attributes']['dn'] = 'uni/infra/lldpIfP-%s' % (policy_name)
        body['lldpIfPol']['attributes']['name'] = policy_name
        if not lldp_receive:
            body['lldpIfPol']['attributes']['adminRxSt'] = 'disabled'
        if not lldp_transmit:
            body['lldpIfPol']['attributes']['adminTxSt'] = 'disabled'
        body['lldpIfPol']['attributes']['rn'] = 'lldpIfP-%s' % (policy_name)
        body['lldpIfPol']['attributes']['status'] = 'created'
        body['lldpIfPol']['children'] = []
        return body

    def create_policy_interface_lldp(
            self,
            policy_name,
            lldp_receive,
            lldp_transmit
        ):
        body = self.get_create_policy_interface_lldp_body(
            policy_name,
            lldp_receive,
            lldp_transmit
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
