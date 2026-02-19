class ApplicationProfileCreate():
    def __init__(self):
        pass

    def get_create_application_profile_body(
            self,
            tenant_name,
            ap_name
        ):
        body = {}
        body['fvAp'] = {}
        body['fvAp']['attributes'] = {}
        body['fvAp']['attributes']['dn'] = 'uni/tn-%s/ap-%s' % (tenant_name, ap_name)
        body['fvAp']['attributes']['rn'] = 'ap-%s' % (ap_name)
        body['fvAp']['attributes']['name'] = ap_name
        body['fvAp']['attributes']['status'] = 'created'
        body['fvAp']['children'] = []
        return body

    def create_application_profile(
            self,
            tenant_name,
            ap_name
        ):
        body = self.get_create_application_profile_body(
            tenant_name,
            ap_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/tn-%s/ap-%s.json' % (tenant_name, ap_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_application_profile_mo()
            self.init_application_profile()

        return success, error
