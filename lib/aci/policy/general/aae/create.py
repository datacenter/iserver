class PolicyGeneralAaeCreate():
    def __init__(self):
        pass

    def get_create_policy_global_aae_body(
            self,
            policy_name,
            phys=None,
            l3=None
        ):
        body = {}
        body['infraInfra'] = {}
        body['infraInfra']['attributes'] = {}
        body['infraInfra']['attributes']['dn'] = 'uni/infra'
        body['infraInfra']['attributes']['status'] = 'modified'

        body['infraInfra']['children'] = []

        child_mo = {}
        child_mo['infraAttEntityP'] = {}
        child_mo['infraAttEntityP']['attributes'] = {}
        child_mo['infraAttEntityP']['attributes']['dn'] = 'uni/infra/attentp-%s' % (policy_name)
        child_mo['infraAttEntityP']['attributes']['name'] = policy_name
        child_mo['infraAttEntityP']['attributes']['rn'] = 'attentp-%s' % (policy_name)
        child_mo['infraAttEntityP']['attributes']['status'] = 'created'
        child_mo['infraAttEntityP']['children'] = []

        if phys is not None:
            dom_mo = {}
            dom_mo['infraRsDomP'] = {}
            dom_mo['infraRsDomP']['attributes'] = {}
            dom_mo['infraRsDomP']['attributes']['tDn'] = 'uni/phys-%s' % (phys)
            dom_mo['infraRsDomP']['attributes']['status'] = 'created'
            dom_mo['infraRsDomP']['children'] = []

            child_mo['infraAttEntityP']['children'].append(
                dom_mo
            )

        if l3 is not None:
            dom_mo = {}
            dom_mo['infraRsDomP'] = {}
            dom_mo['infraRsDomP']['attributes'] = {}
            dom_mo['infraRsDomP']['attributes']['tDn'] = 'uni/l3dom-%s' % (l3)
            dom_mo['infraRsDomP']['attributes']['status'] = 'created'
            dom_mo['infraRsDomP']['children'] = []

            child_mo['infraAttEntityP']['children'].append(
                dom_mo
            )

        body['infraInfra']['children'].append(
            child_mo
        )

        child_mo = {}
        child_mo['infraFuncP'] = {}
        child_mo['infraFuncP']['attributes'] = {}
        child_mo['infraFuncP']['attributes']['dn'] = 'uni/infra/funcprof'
        child_mo['infraFuncP']['attributes']['status'] = 'modified'
        child_mo['infraFuncP']['children'] = []

        body['infraInfra']['children'].append(
            child_mo
        )

        return body

    def create_policy_global_aae(
            self,
            policy_name,
            phys=None,
            l3=None,
            wait=False
        ):
        body = self.get_create_policy_global_aae_body(
            policy_name,
            phys=phys,
            l3=l3
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra.json'
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_global_aae_mo()

            if wait:
                if not self.wait_policy_global_aae(policy_name):
                    return False, 'Wait time reached'

        return success, error
