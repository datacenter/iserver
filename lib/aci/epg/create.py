class EpgCreate():
    def __init__(self):
        pass

    def get_create_epg_body(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            bd_name
        ):
        body = {}
        body['fvAEPg'] = {}
        body['fvAEPg']['attributes'] = {}
        body['fvAEPg']['attributes']['dn'] = 'uni/tn-%s/ap-%s/epg-%s' % (
            epg_tenant,
            epg_ap,
            epg_name
        )
        body['fvAEPg']['attributes']['prio'] = 'level3'
        body['fvAEPg']['attributes']['name'] = epg_name
        body['fvAEPg']['attributes']['rn'] = 'epg-%s' % (epg_name)
        body['fvAEPg']['attributes']['status'] = 'created'
        body['fvAEPg']['children'] = []

        bd_mo = {}
        bd_mo['fvRsBd'] = {}
        bd_mo['fvRsBd']['attributes'] = {}
        bd_mo['fvRsBd']['attributes']['tnFvBDName'] = bd_name
        bd_mo['fvRsBd']['attributes']['status'] = 'created,modified'
        bd_mo['fvRsBd']['children'] = []

        body['fvAEPg']['children'].append(
            bd_mo
        )

        return body

    def create_epg(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            bd_name,
            wait=False
        ):
        body = self.get_create_epg_body(
            epg_tenant,
            epg_ap,
            epg_name,
            bd_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/tn-%s/ap-%s/epg-%s.json' % (
            epg_tenant,
            epg_ap,
            epg_name
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_epg_mo()
            self.init_epg()

            if wait:
                if not self.wait_epg(epg_tenant, epg_ap, epg_name):
                    return False, 'Wait time reached'

        return success, error
