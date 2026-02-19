class PolicyInterfacePortChannelCreate():
    def __init__(self):
        pass

    def get_create_policy_interface_port_channel_body(
            self,
            policy_name,
            mode,
            members_min,
            members_max,
            lb_mode,
            suspend,
            graceful,
            symmetric,
            fast,
            hash_mode
        ):
        body = {}
        body['lacpLagPol'] = {}
        body['lacpLagPol']['attributes'] = {}
        body['lacpLagPol']['attributes']['dn'] = 'uni/infra/lacplagp-%s' % (policy_name)
        body['lacpLagPol']['attributes']['name'] = policy_name
        body['lacpLagPol']['attributes']['rn'] = 'lacplagp-%s' % (policy_name)
        body['lacpLagPol']['attributes']['status'] = 'created'

        if members_min != 1:
            body['lacpLagPol']['attributes']['minLinks'] = str(members_min)

        if members_max != 16:
            body['lacpLagPol']['attributes']['maxLinks'] = str(members_max)

        if lb_mode == 'dynamic':
            body['lacpLagPol']['attributes']['pcLB'] = 'dynamic'

        if mode == 'active':
            body['lacpLagPol']['attributes']['mode'] = 'active'

        if mode == 'passive':
            body['lacpLagPol']['attributes']['mode'] = 'passive'

        if mode == 'pinning':
            body['lacpLagPol']['attributes']['mode'] = 'mac-pin'

        if mode == 'load':
            body['lacpLagPol']['attributes']['mode'] = 'mac-pin-nicload'

        if mode == 'explicit':
            body['lacpLagPol']['attributes']['mode'] = 'explicit-failover'

        ctrl = []
        if suspend:
            ctrl.append('susp-individual')
        if graceful:
            ctrl.append('graceful-conv')
        if fast:
            ctrl.append('fast-sel-hot-stdby')
        if symmetric:
            ctrl.append('symmetric-hash')

        if suspend and graceful and fast and len(ctrl) == 3:
            pass
        else:
            body['lacpLagPol']['attributes']['ctrl'] = ','.join(ctrl)

        body['lacpLagPol']['children'] = []

        if hash_mode is not None:
            hash_mo = {}
            hash_mo['l2LoadBalancePol'] = {}
            hash_mo['l2LoadBalancePol']['attributes'] = {}
            hash_mo['l2LoadBalancePol']['attributes']['dn'] = 'uni/infra/lacplagp-%s/loadbalanceP' % (policy_name)

            if hash_mode == 'sip':
                hash_mo['l2LoadBalancePol']['attributes']['hashFields'] = 'src-ip'

            if hash_mode == 'dip':
                hash_mo['l2LoadBalancePol']['attributes']['hashFields'] = 'dst-ip'

            if hash_mode == 'sport':
                hash_mo['l2LoadBalancePol']['attributes']['hashFields'] = 'l4-src-port'

            if hash_mode == 'dport':
                hash_mo['l2LoadBalancePol']['attributes']['hashFields'] = 'l4-dst-port'

            hash_mo['l2LoadBalancePol']['attributes']['rn'] = 'loadbalanceP'
            hash_mo['l2LoadBalancePol']['attributes']['status'] = 'created'
            hash_mo['l2LoadBalancePol']['children'] = []

            body['lacpLagPol']['children'].append(
                hash_mo
            )

        return body

    def create_policy_interface_port_channel(
            self,
            policy_name,
            mode,
            members_min,
            members_max,
            lb_mode,
            suspend,
            graceful,
            symmetric,
            fast,
            hash_mode
        ):
        body = self.get_create_policy_interface_port_channel_body(
            policy_name,
            mode,
            members_min,
            members_max,
            lb_mode,
            suspend,
            graceful,
            symmetric,
            fast,
            hash_mode
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
