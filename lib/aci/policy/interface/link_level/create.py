class PolicyInterfaceLinkLevelCreate():
    def __init__(self):
        pass

    def get_create_policy_interface_link_level_body(
            self,
            policy_name,
            auto,
            media,
            debounce,
            delay,
            emi
        ):
        body = {}
        body['fabricHIfPol'] = {}
        body['fabricHIfPol']['attributes'] = {}
        body['fabricHIfPol']['attributes']['dn'] = 'uni/infra/hintfpol-%s' % (policy_name)
        body['fabricHIfPol']['attributes']['name'] = policy_name
        body['fabricHIfPol']['attributes']['rn'] = 'hintfpol-%s' % (policy_name)
        body['fabricHIfPol']['attributes']['status'] = 'created'

        if auto == 'off':
            body['fabricHIfPol']['attributes']['autoNeg'] = 'off'

        if auto == 'enforce':
            body['fabricHIfPol']['attributes']['autoNeg'] = 'on-enforce'

        if media == 'sfp10gtx':
            body['fabricHIfPol']['attributes']['portPhyMediaType'] = 'sfp-10g-tx'

        if debounce != 100:
            body['fabricHIfPol']['attributes']['linkDebounce'] = debounce

        if delay > 0:
            body['fabricHIfPol']['attributes']['dfeDelayMs'] = delay

        if emi:
            body['fabricHIfPol']['attributes']['emiRetrain'] = 'emable'

        body['fabricHIfPol']['children'] = []
        return body

    def create_policy_interface_link_level(
            self,
            policy_name,
            auto,
            media,
            debounce,
            delay,
            emi
        ):
        body = self.get_create_policy_interface_link_level_body(
            policy_name,
            auto,
            media,
            debounce,
            delay,
            emi
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
